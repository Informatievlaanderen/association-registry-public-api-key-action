#!/bin/sh -l

python3 /main.py -c "${1}" -e "${2}" -p "${3}" --env-tst "${4}" --env-stg "${5}" --env-prd "${6}" --aws-tst-access-key-id "${7}" --aws-tst-secret-access-key "${8}" --aws-tst-region-name "${9}" --aws-stg-access-key-id "${10}" --aws-stg-secret-access-key "${11}" --aws-stg-region-name "${12}" --aws-prd-access-key-id "${13}" --aws-prd-secret-access-key "${14}"  --aws-prd-region-name "${15}" --revoke-access "${16}";
