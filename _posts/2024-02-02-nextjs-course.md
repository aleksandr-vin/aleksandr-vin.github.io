---
title: "Learning Next.js"
tags: learning nextjs react dev coding courses
---

I have an idea: a _freeform-to-structured_ job descriptions transformer web app.

Started thinking of tRPC, but then decided not to use Angular for this project, but learn Next.js instead.
Beginning with a [refresher](https://nextjs.org/learn/react-foundations) and then with a
[dashboard-app course](https://nextjs.org/learn/dashboard-app). While following it, I've picked up a lot
of interesting things. All llisted at the end here.

Below are my notes on the course material.

## Chapter 6: Setting Up Your Database

On [chapter 6](https://nextjs.org/learn/dashboard-app/setting-up-your-database), this
[post](https://gal.hagever.com/posts/running-vercel-postgres-locally) appeared to be very
helpful, if you prefer to develop on a locally-run Postgres. One small thing to add: if you do not
use Kysely, just adding this snippet to _seed.js_ would be enough:

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

## Chapter 7: Route Handlers

From the manual:

> [Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/route-handlers) allow you to create custom request
> handlers for a given route using the Web Request and Response APIs.

Thinking about developing the original idea (see top of the post), which I was going to do in tRPC (also with the goal to learn it):
that could be a good alternative to do it differently: in Route Handlers or React Server Components. Less repositories, less moving parts (at least
ones that you pet yourself). This brings us to a hosting for server side, which I would need anyway. It could be worth to check
Vercel services for hosting next.js project all-in-one.

Other option could be static rendering: this way a new task would result in a new build pipeline that will compile a new JD into repo
and publish it to hosting. Nice finding: [Partial Prerendering](https://vercel.com/blog/partial-prerendering-with-next-js-creating-a-new-default-rendering-model)
to try with the idea implementation.

## Chapter 11: State in URL

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

## Next steps

Overall it is a nice fresh course, I like it! Definetely worth checking the [next steps](https://nextjs.org/learn/dashboard-app/next-steps).

### Updates

#### React 18 Concurrent Rendering with Low Priority Updates:

```
startTransition(() => {
  lowPriorityUpdate()
})
```

#### Core Web Vitals

- Time To First Byte
- First Contentful Paint
- Largest Contentful Paint
- Time To Interactive
- Cumulative Layout Shift
- First Input Delay

Further reading:

### Optimization

1. Images: [nextjs.org/docs/app/building-your-application/optimizing/images](https://nextjs.org/docs/app/building-your-application/optimizing/images)
2. Fonts: [nextjs.org/docs/app/building-your-application/optimizing/fonts](https://nextjs.org/docs/app/building-your-application/optimizing/fonts)
3. Web performance, multimedia: [developer.mozilla.org/en-US/docs/Learn/Performance/Multimedia](https://developer.mozilla.org/en-US/docs/Learn/Performance/Multimedia)
4. Web fonts: [developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Web_fonts](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Web_fonts)
5. Accessibility: [www.npmjs.com/package/eslint-plugin-jsx-a11y](https://www.npmjs.com/package/eslint-plugin-jsx-a11y)
6. https://swr.vercel.app

### Security & Privacy

1. Server components security: [nextjs.org/blog/security-nextjs-server-components-actions](https://nextjs.org/blog/security-nextjs-server-components-actions)
2. Web privacy: [web.dev/learn/privacy](https://web.dev/learn/privacy)

### SEO

1. Metadata: [nextjs.org/docs/app/api-reference/functions/generate-metadata](https://nextjs.org/docs/app/api-reference/functions/generate-metadata)

### Misc

1. Image gen for social cards: [vercel.com/blog/introducing-vercel-og-image-generation-fast-dynamic-social-card-images](https://vercel.com/blog/introducing-vercel-og-image-generation-fast-dynamic-social-card-images)
