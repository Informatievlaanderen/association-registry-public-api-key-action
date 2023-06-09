#!/bin/sh -l

python3 /main.py -k "${1}" -c "${2}" -e "${3}" -p "${4}" --access-sync "${5}" --access-association-registry "${6}" --env-tst "${7}" --env-stg "${8}" --env-prd "${9}" --aws-tst-access-key-id "${10}" --aws-tst-secret-access-key "${11}" --aws-tst-region-name "${12}" --aws-stg-access-key-id "${13}" --aws-stg-secret-access-key "${14}" --aws-stg-region-name "${15}" --aws-prd-access-key-id "${16}" --aws-prd-secret-access-key "${17}"  --aws-prd-region-name "${18}" --revoke-access "${19}" --access-tickets "true";
