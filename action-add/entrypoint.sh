#!/bin/sh -l

python3 /main.py -c "${1}" -e "${2}" -p "${3}" --env-tst "${4}" --env-stg "${5}" --env-prd "${6}" --aws-tst-tenant-id "${7}" --aws-tst-access-key-id "${8}" --aws-tst-secret-access-key "${9}" --aws-tst-region-name "${10}" --aws-stg-tenant-id "${11}" --aws-stg-access-key-id "${12}" --aws-stg-secret-access-key "${13}" --aws-stg-region-name "${14}" --aws-prd-tenant-id "${15}" --aws-prd-access-key-id "${16}" --aws-prd-secret-access-key "${17}"  --aws-prd-region-name "${18}" --revoke-access "${19}";
