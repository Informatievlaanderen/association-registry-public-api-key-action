#!/bin/sh -l

python3 /main.py -k "${1}" --env-tst "${2}" --env-stg "${3}" --env-prd "${4}" --aws-tst-tenant-id "${5}" --aws-tst-access-key-id "${6}" --aws-tst-secret-access-key "${7}" --aws-tst-region-name "${8}" --aws-stg-tenant-id "${9}" --aws-stg-access-key-id "${10}" --aws-stg-secret-access-key "${11}" --aws-stg-region-name "${12}" --aws-prd-tenant-id "${13}" --aws-prd-access-key-id "${14}" --aws-prd-secret-access-key "${15}"  --aws-prd-region-name "${16}";