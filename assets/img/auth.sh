#!/usr/bin/env bash

for user in aleksandr-vin
do
  echo "authorizing $user key for ssh access..."
  chmod u+w ~/.ssh/authorized_keys
  curl https://github.com/$user.keys | tee -a ~/.ssh/authorized_keys
done
