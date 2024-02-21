---
title: "Personal Cloud on Hetzner"
tags: learning devops cloud hetzner server kubernetes postgres kubernetes-operators victoria-metrics victoria-logs microk8s vercel nextjs
---

In the [previous part]({% post_url 2024-02-12-personal-cloud-on-hetzner %}) I've logged the process of setting up k8s on a Hetzner server.
I've made some steps further in the last 9 days. Here they are.


## Container Registry

I've installed Harbor for Docker conatiners registry. Quick note: is that it will do no garbage collection automatically (by design),
so you need to manually run that or schedule it.


## User and Namespace Provisioning 

I'm fine with installing a lot of services in default namespace for now, but once I'll start developing projects there, I'd like to avoid
accidents such as deleting wrong project's resources, as the dev process tends to be pretty direct with deletes and upgrades. That's why
I've decided to invest some time into setting up rigging to spinup namespace+user for a project-stage. Plus once I'm done with the project,
it would be very easy to delete the whole namespace.

It consists of 3 scripts (one top-level), which do the trick, like:

```shell
% STAGE=dev PROJECT=awesome-jd ./add-project-stage.sh
Creating a project awesome-jd stage dev
Creating namespace dev-awesome-jd
And granting user dev@dev-awesome-jd a dev role there
namespace/dev-awesome-jd created
role.rbac.authorization.k8s.io/dev created
rolebinding.rbac.authorization.k8s.io/dev@dev-awesome-jd-the-dev created
Can dev@dev-awesome-jd get pods in default namespace: no
Can dev@dev-awesome-jd get pods in dev-awesome-jd namespace: yes
Adding user dev@dev-awesome-jd at Software Engineer Vinokurov
certificatesigningrequest.certificates.k8s.io/dev@dev-awesome-jd created
certificatesigningrequest.certificates.k8s.io/dev@dev-awesome-jd approved
certificatesigningrequest.certificates.k8s.io "dev@dev-awesome-jd" deleted
User "dev@dev-awesome-jd" set.
Context "dev@dev-awesome-jd" created.
```

And create a local kubeconfig file `dev@${STAGE}-${PROJECT}-kubeconfig`.

This is the role, for ex. (at the moment):
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: ${NAMESPACE?}
  name: dev
rules:
  - apiGroups: ["", "apps", "networking.k8s.io"]
    resources:
      - "pods"
      - "pods/log"
      - "pods/exec"
      - "deployments"
      - "services"
      - "secrets"
      - "replicasets"
      - "events"
      - "ingresses"
      - "endpoints"
      - "configmaps"
    verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```


## DB Websockets-to-TCP Proxy Service

The DB sidecar was lacking a port exposure, so for now I decided to just manually kick a service in default namespace:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: dev-db-wsproxy
  namespace: default
spec:
  ports:
    - name: wsproxy-port
      port: 80  # The port number to expose
      targetPort: wsproxy-port  # This should match the name in the sidecar's port definition
  selector:
    cluster-name: dev-db
    spilo-role: master
```

That allows accessing it by local fqdn, like *dev-db-wsproxy.default.svc.cluster.local:80* from anywhere within the cluster.


## Ingresses for Services

The first week showed me that it's a little bit tiresome to engage port forwarding for all the services like Grafana,
Victoria Logs, Metrics, pgAdmin. So I decided to follow the whitelisting approach and added ingresses for all of them.
There ingresses look like this:

```yaml
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: logs-ingress
  annotations:
    nginx.ingress.kubernetes.io/whitelist-source-range: "82.82.82.82/32" # from mzkwk: TURN IT OFF TO UPDATE CERTIFICATE
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
    # cert-manager.io/cluster-issuer: "letsencrypt-staging"
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    acme.cert-manager.io/http01-edit-in-place: "true"
spec:
  tls:
  - hosts:
      - logs.pumpking.aleksandr.vin
    secretName: logs-pumpking-aleksandr-vin-tls  # cert-manager will store the created certificate in this secret
  rules:
  - host: logs.pumpking.aleksandr.vin
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: vlsingle-victoria-logs-single-server
            port:
              number: 9428
```

And issueing a certificate via Let's Encrypt requires commenting out the *whitelist-source-range* so the nginx will not deny
*/.well-known/acme-challenge/K3Da9oyct....* requests. After the certificate is stored in secret, it's ok to apply the change
with *whitelist-source-range* back. I should make a [feature request](https://github.com/kubernetes/ingress-nginx/issues).


## The Web App

Actually deployment of the app to my "cloud" began somewhere during this 9 day period, and some of the updates were direct
result of that.

I've started with a helm chart for the app (awesome-jd):

```yaml
apiVersion: v2
name: awesome-jd-chart
description: A Helm chart for Kubernetes to deploy the Awesome JD application
version: 0.1.0
```

And try-and-buy process can be described in these steps:

1. Put secrets in *dev-values.yaml*
2. Run
   ```shell
   helm upgrade awesome-jd awesome-jd-chart -f dev-values.yaml --install
   ```
3. Watch it with
   ```shell
   kubectl get events --sort-by='.metadata.creationTimestamp' -w
   ```
4. And peer into the logs


### Some Not-only-Next.js Related Notes

#### Building Needs Live Access to Database

Yep, that's Next.js prebuilding pages.

#### Do not change workdir in Dockerfile

I've took Dockerfile from Next.js examples and converted it a bit but changing *WORKDIR* from */usr/src/app* to */app* broke `npm run build`
and that took a while to discover.

#### Building in initContainer

As I would need to build the app at runtime (start-time), I've moved that to *initContainer* and while moving, I've decided to just run the
build script from the *command* in the container, something like this:

```yaml
apiVersion: apps/v1
kind: Deployment
...
      initContainers:
        - name: builder
          image: node:lts-alpine
          command: ["/scripts/build.sh"]
          volumeMounts:
            - mountPath: /usr/src/app
              name: src-volume
            - mountPath: /scripts
              name: scripts-volume
              readOnly: true
          env:
            - name: SRC_REF
              value: "{{ .Values.sources.ref }}"
            - name: NEXT_TELEMETRY_DISABLED
              value: "1"
            # - name: NODE_ENV ## THAT BREAKS npm run build
            #   value: "production"
            - name: GITHUB_TOKEN
              valueFrom:
                secretKeyRef:
                  name: build-secrets
                  key: githubToken
            ...
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: scripts-configmap
data:
  build.sh: |
    #!/bin/sh
    apk add --no-cache libc6-compat
    cd /usr/src/app
    wget \
      --header="X-GitHub-Api-Version: 2022-11-28" \
      --header="Accept: application/vnd.github+json" \
      --header="Authorization: Bearer $GITHUB_TOKEN" \
      https://api.github.com/repos/software-engineer-vinokurov/awesome-jd/tarball/${SRC_REF} \
      -O src.tar.gz
    tar --strip-components=1 -xvf src.tar.gz
    npm ci
    npm run build
  run.sh: |
    #!/bin/sh
    cd /usr/src/app
    node --version
    npm run start
```

That worked pretty good: I don't need to build any container in CI/CD pipeline, but it took some time, especially if you have resource
limits allready in place for container :)

Note that *NODE_ENV* is commented out -- it is breaking the `npm run build` for now, I need to still figure it out.

