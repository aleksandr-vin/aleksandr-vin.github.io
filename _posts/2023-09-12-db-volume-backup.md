---
title: "Shell script to backup and restore data on docker volumes"
tags: shell docker console volume backup restore
---

Continuation on the journey with database migrations. It was taking around 10 min to `psql` replay the backed-up sql file.
And when you mess up with migration script, you want to retry it with some tweaks. `SELECT * INTO` a backup table is not
without complications, like constraints, foregin keys from other tables, indexes etc. That's why my next turn was to perform
a docker volume (I'm running pg in container) backup-restore cycle. And this is what came out of it: 17 seconds with stopping and starting the pg container! 

And this script is here: [db-volume-backup.sh](https://gist.github.com/aleksandr-vin/41ee2062e978f2f680fd190c7e957dab).