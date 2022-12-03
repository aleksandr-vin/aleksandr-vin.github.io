---
title: "Monitoring my best"
tags: monitoring metrics prometheus exporter federation node_exporter scraping
---

Some numbers need history.

I'm running `prometheus` at home on a raspberry pi for quite some time already. It runs more than just Prometheus but that's for
another story. Out of curiousity I've put `node_exporter` as brew services on all computers running at home. Also one day I was
interested in when do kids run out of their mobile internet, so I put some effort in reverse engineering customer's portal of
my mobile provider and made a [mijn-simpel-python-client](https://github.com/aleksandr-vin/mijn-simpel-python-client) (lib
and cli), and a Prometheus Exporter of usage summary: [mijn-simpel-exporter](https://github.com/aleksandr-vin/mijn-simpel-exporter),
running that client. So that raspberry pi is also scraping my family's subscriptions usage summaries from [mijn.simpel.nl](https://mijn.simpel.nl) every 30 min. And all that is visualised on a simple Grafana dashboard, also running on that pi.

Now my work macbook. It does not always work at home, so just running `node_exporter` is not enough during the time when noboby is
scraping these metrics. So I have `prometheus` running on that macbook too. It's worth mentioning that we have `prometheus` instancies
that scrape out k8s apps' metrics at work, but they have retention time 15 days (which is default), and that is very sad as we can't
follow the trend of our apps' performance over time. To bypass that I have a federation config on my macbook to scrape our apps'
metrics (their current values) when I'm on VPN or at the office and a retention time of 184 days. The example config for federation
can be seen at the end of the article.

Now the dev env. We develop a backend which is a k8s app. For dev purposes we can run it locally or as docker container (okay, only
on intel macs for now as m1 needs some love to move to different base image). The rest of the resources, that we need for the app to
run locally, we manage with docker compose. The Grafana dashboards, that we develop for monitoring our apps, are stored in git as
a code: in yaml files with some custom [pre-commit](http://pre-commit.com) checks. Someday I'll describe what tooling I have to
maintain out Dashboards-as-a-code. In short it allows us:

1. Run dockerised Grafana with dashboards provisioned from the current working git branch
2. Edit dashboards via Grafana UI
3. Persist dashboards changes as changes of yaml files,
   also exploiting this git config
   ```
   diff.dyff.command=dyff_between() { dyff --color on between --omit-header "$2" "$5"; }; dyff_between
   ```
4. Inject common annotations to all managed dashboards (like pod (re)starts)
5. Check that dashboards match our desired qualities with pre-commit hooks.
6. Provision all our managed dashboards to target Grafana instances, where we monitor our live and test stages.

In short, it is so easy to add a counter or a timer metric in the app's code, run it, open local Grafana, add a panel with new metric
and see it appears on the screen, then what is left is just to save the dashboard change and it will appear in your PR.

Maybe for the record, I'll put a config for prometheus that is also running in docker compose env, which scrapes metrics of
our app which can appear as docker container or locally (via `host.docker.internal:9095`) plus scrapes the federate endpoint too:

```
global:
  scrape_interval: 15s
  scrape_timeout: 10s
  evaluation_interval: 15s
scrape_configs:
  - job_name: operations_portal
    honor_timestamps: true
    metrics_path: /metrics
    scheme: http
    static_configs:
      - targets: ["operations-portal-api:9095"]
        labels:
          app_kubernetes_io_instance: "operations-portal-docker-compose"
          app_kubernetes_io_name: "api"
          kubernetes_pod_name: "operations-portal-docker-compose-api-7d8dfbffb5-yyyyy"
      - targets: ["operations-portal-jobs:9095"]
        labels:
          app_kubernetes_io_instance: "operations-portal-docker-compose"
          app_kubernetes_io_name: "jobs"
          kubernetes_pod_name: "operations-portal-docker-compose-jobs-7d8dfbffb5-xxxxx"
      - targets: ["host.docker.internal:9095"]
        labels:
          app_kubernetes_io_instance: "operations-portal-local"
          app_kubernetes_io_name: "mixed"
          kubernetes_pod_name: "operations-portal-local-mixed-7d8dfbffb5-zzzzz"
  - job_name: "federate-operations-portal"
    scrape_interval: 15s
    honor_labels: true
    metrics_path: "/federate"
    params:
      "match[]":
        - '{app_kubernetes_io_instance=~"operations-portal-.*"}'
    scheme: https
    static_configs:
      - targets:
          - 'prometheus-foo******************.com:443'
          - 'prometheus-bar******************.com:443'
```

Summing up:

1. `node_exporter`: 5 (pi, home macbooks, work macbook)
2. `prometheus`: 3+2 (pi, work macbook, docker, office)
3. `grafana`: 3+2 (pi, work macbook, docker, office)
