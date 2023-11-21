#!/usr/bin/python3

import os, sys, json, argparse, uuid, boto3

# args
parser = argparse.ArgumentParser(description='put new client apikey')

parser.add_argument('-k','--apikey', help='apikey', required=True)
parser.add_argument('-c','--client', help='client name', required=True)
parser.add_argument('-e','--email', help='email', required=True)
parser.add_argument('--revoke-access', help='revoked', required=False, default='false')
parser.add_argument('-p','--plan', help='plan options are ["standard"]', required=True, default="standard")

parser.add_argument('--access-sync', help='["true", "false"] default: false', required=False, default='false')
parser.add_argument('--access-association-registry', help='["true", "false"] default: false', required=False, default='false')

parser.add_argument('--env-tst', help='["true", "false"] default: false', required=False, default='false')
parser.add_argument('--env-stg', help='["true", "false"] default: false', required=False, default='false')
parser.add_argument('--env-prd', help='["true", "false"] default: false', required=False, default='false')

parser.add_argument('--aws-tst-tenant-id', required=True)
parser.add_argument('--aws-tst-access-key-id', required=True)
parser.add_argument('--aws-tst-secret-access-key', required=True)
parser.add_argument('--aws-tst-region-name', required=False, default='eu-west-1')

parser.add_argument('--aws-stg-tenant-id', required=True)
parser.add_argument('--aws-stg-access-key-id', required=True)
parser.add_argument('--aws-stg-secret-access-key', required=True)
parser.add_argument('--aws-stg-region-name', required=False, default='eu-west-1')

parser.add_argument('--aws-prd-tenant-id', required=True)
parser.add_argument('--aws-prd-access-key-id', required=True)
parser.add_argument('--aws-prd-secret-access-key', required=True)
parser.add_argument('--aws-prd-region-name', required=False, default='eu-west-1')

parser.add_argument('--access-tickets', help='["true", "false"] default: true', required=False, default='true')

args = parser.parse_args()

usage_plan_ids = {
    "anon": {
        "tst":"4im4mj",
        "stg":"ybzchh",
        "prd":"j1tmtu"
    },
    "unlimited": {
        "tst":"4ba4z0",
        "stg":"tvhp9a",
        "prd":"cyb1t3"
    }
}

def start_session(aws_access_key_id, aws_secret_access_key, aws_tenant_id, region_name):
    session = boto3.Session(aws_access_key_id, aws_secret_access_key, region_name=region_name)
    sts_client = session.client('sts')
    role_arn = 'arn:aws:iam::' + aws_tenant_id + ':role/verenigingsregisterApiGatewayDynamodbEditorsRole'
    response = sts_client.assume_role(RoleArn=role_arn, RoleSessionName='AssumeRoleSession')
    return boto3.Session(
        aws_access_key_id=response['Credentials']['AccessKeyId'],
        aws_secret_access_key=response['Credentials']['SecretAccessKey'],
        aws_session_token=response['Credentials']['SessionToken'], 
        region_name=region_name)

def get_db_table(session):
    return session.resource('dynamodb').Table('verenigingsregister-api-keys')

def get_client_attribute_updates(env):
    return {
        "ClientName": {
            "Action": "PUT", 
            "Value": args.client
        },
        "Description": {
            "Action": "PUT", 
            "Value": args.email
        },
        "Plan": {
            "Action": "PUT", 
            "Value": args.plan
        }
        "Revoked": {
            "Action": "PUT", 
            "Value": args.revoke_access == 'true'
        },
        "UsagePlanID": {
            "Action": "PUT", 
            "Value":  usage_plan_ids[args.plan][env]
        },
    }

def json_serialize(obj):
    return json.dumps(obj, separators=(',', ':'))

def update_apikey(apikey):
    apply_in_tst = args.env_tst == 'true'
    apply_in_stg = args.env_stg == 'true'
    apply_in_prd = args.env_prd == 'true'

    if(apply_in_tst):
        tst_session=start_session(args.aws_tst_access_key_id, args.aws_tst_secret_access_key, args.aws_tst_tenant_id, args.aws_tst_region_name)
        tst_table = get_db_table(tst_session)
        tst_item = get_client_attribute_updates(env='tst')
        tst_result = tst_table.update_item(
            Key={"ApiKey": apikey},
            AttributeUpdates= tst_item,
            ReturnValues="ALL_NEW"
        )
        print(f"In test:{tst_result}")
    
    if(apply_in_stg):
        stg_session=start_session(args.aws_stg_access_key_id, args.aws_stg_secret_access_key, args.aws_stg_tenant_id, args.aws_stg_region_name)
        stg_table = get_db_table(stg_session)
        stg_item = get_client_attribute_updates(env='stg')
        stg_result = stg_table.update_item(
            Key={"ApiKey": apikey},
            AttributeUpdates= stg_item,
            ReturnValues="ALL_NEW"
        )
        print(f"In staging: {stg_result}")
    
    if(apply_in_prd):
        prd_session=start_session(args.aws_prd_access_key_id, args.aws_prd_secret_access_key, args.aws_prd_tenant_id, args.aws_prd_region_name)
        prd_table = get_db_table(prd_session)
        prd_item = get_client_attribute_updates(env='prd')
        prd_result = prd_table.update_item(
            Key={"ApiKey": apikey},
            AttributeUpdates= prd_item,
            ReturnValues="ALL_NEW"
        )
        print(f"In production: {prd_result}")

def main():
    if(args.apikey == None):
        exit(0);
    update_apikey(args.apikey)
    sys.exit()

if __name__ == "__main__":
    main()
