---
title:  "Running on M1 macbookpro"
tags:   m1 problems apple macbookpro
---

Here to collect problems and tips while running on a M1 macbookpro.

## Embedded Postgres

Tests can't start, with this error:

```
20:36:03.428 [log:pid(40821)] INFO  init-87e446c7-ebfd-4b18-8514-176fbbadd2b3:initdb - dyld[40821]: Library not loaded: @loader_path/../lib/libpq.5.dylib

Exception encountered when invoking run on a nested suite - Process [/var/folders/tn/grglkq4521sgkw60t257zmw00000gq/T/embedded-pg/PG-578c3302bce806451b07e3a73d8438d1/bin/initdb, -A, trust, -U, postgres, -D, /var/folders/tn/grglkq4521sgkw60t257zmw00000gq/T/epg15597056772387068912, -E, UTF-8] failed
```

The _initdb_ binary packaged with Embedded Postgres is of wrong arch:

```
% file /var/folders/tn/grglkq4521sgkw60t257zmw00000gq/T/embedded-pg/PG-578c3302bce806451b07e3a73d8438d1/bin/initdb
/var/folders/tn/grglkq4521sgkw60t257zmw00000gq/T/embedded-pg/PG-578c3302bce806451b07e3a73d8438d1/bin/initdb: Mach-O universal binary with 2 architectures: [i386:Mach-O executable i386] [x86_64:Mach-O 64-bit executable x86_64]
/var/folders/tn/grglkq4521sgkw60t257zmw00000gq/T/embedded-pg/PG-578c3302bce806451b07e3a73d8438d1/bin/initdb (for architecture i386):	Mach-O executable i386
/var/folders/tn/grglkq4521sgkw60t257zmw00000gq/T/embedded-pg/PG-578c3302bce806451b07e3a73d8438d1/bin/initdb (for architecture x86_64):	Mach-O 64-bit executable x86_64
```

While the one, installed with `brew install postgresql` apparently has the proper arch:

```
% file /opt/homebrew/bin/initdb
/opt/homebrew/bin/initdb: Mach-O 64-bit executable arm64
```

For now the [issue](https://github.com/opentable/otj-pg-embedded/issues/169) is not solved. But there is a workaround. You need to override
the path to Postgress installation when building the EmbeddedPostgress instance, like here:

```
val builder = EmbeddedPostgres.builder().setPgDirectoryResolver((_: Optional[File]) => new File("/opt/homebrew/Cellar/postgresql@12/12.9_1/"))
builder.start()
```
