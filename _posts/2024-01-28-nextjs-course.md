---
title: "Learning Next.js"
tags: learning nextjs react dev coding courses
---

Having an idea: a free-form to structured job descriptions transformer web app.

Started with tRPC, but then decided not to use Angular for this project, but learn Next.js instead.
Beginning with a [refresher](https://nextjs.org/learn/react-foundations) and then with a
[dashboard-app course](https://nextjs.org/learn/dashboard-app).

A lot of interesting things picked up while in the course, all llisted at the end here.

## Chapter 6

On chapter 6, this [post](https://gal.hagever.com/posts/running-vercel-postgres-locally) appeared to be very
helpful, if you prefer to develop on locally run Postgres. One small thing to add to the post, is that for
the course example, where you do not use Kysely, just adding this snippet (to _seed.js_) would be enough:

```
const { neonConfig } = require("@neondatabase/serverless");

// if we're running locally
if (!process.env.VERCEL_ENV) {
  // Set the WebSocket proxy to work with the local instance
  neonConfig.wsProxy = (host) => `${host}:5433/v1`;
  // Disable all authentication and encryption
  neonConfig.useSecureWebSocket = false;
  neonConfig.pipelineTLS = false;
  neonConfig.pipelineConnect = false;
}
```

And you'll need the _docker-compose.yaml_ mod:

```
  pg_proxy:
    image: ghcr.io/neondatabase/wsproxy:latest
    environment:
      APPEND_PORT: "postgres:5432"
      ALLOW_ADDR_REGEX: ".*"
      LOG_TRAFFIC: "true"
    ports:
      - "5433:80"
    depends_on:
      - postgres
```

## Route Handlers

From the manual:

> [Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/route-handlers) allow you to create custom request
> handlers for a given route using the Web Request and Response APIs.

Thinking about developing the original idea (see top of the post), which I was going to do in tRPC (also to learn it), it could be a
good alternative to do it differently: in Route Handlers or React Server Components. Less repositories, less moving parts (at least
ones that you pet yourself). This brings us to a hosting for server side, which I would need anyway. It could be worth to check
Vercel services for hosting next.js projext all-in-one.

Other option could be static rendering: this way a new task would result in a new build pipeline that will compile a new JD into repo
and publish it to hosting. Nice finding: [Partial Prerendering](https://vercel.com/blog/partial-prerendering-with-next-js-creating-a-new-default-rendering-model).

## State in URL

[Chapter 11](https://nextjs.org/learn/dashboard-app/adding-search-and-pagination) has a nice example on how to do it easily.

```
const handleSearch = useDebouncedCallback((term) => {
    console.log(`Searching... ${term}`);

    const params = new URLSearchParams(searchParams);
    params.set('page', '1');
    if (term) {
      params.set('query', term);
    } else {
      params.delete('query');
    }
    replace(`${pathname}?${params.toString()}`);
  },
  300);
```

Further reading:

1. https://nextjs.org/docs/app/building-your-application/optimizing/images
2. https://nextjs.org/docs/app/building-your-application/optimizing/fonts
3. https://fonts.google.com/specimen/Workbench
4. Web performance: multimedia https://developer.mozilla.org/en-US/docs/Learn/Performance/Multimedia
5. Web fonts: https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Web_fonts
