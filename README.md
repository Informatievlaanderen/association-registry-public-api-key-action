# association registry api key action - add

This action generates a new client api key

## Example
```yaml
name: Add new client apikey
on:
  workflow_dispatch:
    inputs:
      grant-access-association-registry:
        type: boolean
        description: 'Grant association-registry access'
        required: true 
         
      grant-access-sync:
        type: boolean
        description: 'Grant sync access'
        required: true

      client:
        description: 'ClientName'     
        required: true
        
      email:
        description: 'Email'     
        required: true

      plan:
        type: choice
        description: 'Plan'
        options:
        - standard
        default: standard

      apply-env-tst:
        type: boolean
        description: 'Test'
        required: true

      apply-env-stg:
        type: boolean
        description: 'Staging'
        required: true
        
      apply-env-prd:
        type: boolean
        description: 'Production'
        required: true

jobs:
  association-registry:
    runs-on: ubuntu-latest
    steps:
    - name: Add new client apikey
      uses: informatievlaanderen/association-registry-public-api-key-action/action-add@main
      with:
          client:  ${{ github.event.inputs.client }}
          email: ${{ github.event.inputs.email }}
          plan:  ${{ github.event.inputs.plan }}
          
          access-sync:  ${{ github.event.inputs.grant-access-sync }}
          access-association-registry:  ${{ github.event.inputs.grant-access-association-registry }}
          
          env-tst:  ${{ github.event.inputs.apply-env-tst }}
          env-stg:  ${{ github.event.inputs.apply-env-stg }}
          env-prd:  ${{ github.event.inputs.apply-env-prd }}
          
          aws-tst-access-key-id: ${{ secrets.AWS_TST_ACCESS_KEY_ID }}
          aws-stg-access-key-id: ${{ secrets.AWS_STG_ACCESS_KEY_ID }}
          aws-prd-access-key-id: ${{ secrets.AWS_PRD_ACCESS_KEY_ID }}

          aws-tst-secret-access-key: ${{ secrets.AWS_TST_SECRET_ACCESS_KEY }}
          aws-stg-secret-access-key: ${{ secrets.AWS_STG_SECRET_ACCESS_KEY }}
          aws-prd-secret-access-key: ${{ secrets.AWS_PRD_SECRET_ACCESS_KEY }}
          
          aws-tst-region-name: eu-west-1
          aws-stg-region-name: eu-west-1
          aws-prd-region-name: eu-west-1
```

### Inputs

|Argument| Description | Default | Required |
|--------|-------------|---------|----------|
| client | The client name | - | Yes |
| email | The client email | - | Yes |
| plan | Plan type `standard` | `standard` | Yes |
| access-sync | Grant sync access (`true` / `false`) | `false` | Yes |
| access-association-registry | Grant association-registry access (`true` / `false`) | `false` | Yes |
| env-tst | Apply in test env. (`true` / `false`) | `false` | Yes |
| env-stg | Apply in staging env. (`true` / `false`) | `false` | Yes |
| env-prd | Apply in production env. (`true` / `false`) | `false` | Yes |
| aws-tst-access-key-id | AWS access key id test env | - | Yes  |
| aws-stg-access-key-id | AWS access key id staging env | - | Yes  |
| aws-prd-access-key-id | AWS access key id production env | - | Yes  |
| aws-tst-secret-access-key | AWS secret access key test env | - | Yes  |
| aws-stg-secret-access-key | AWS secret access key staging env | - | Yes  |
| aws-prd-secret-access-key | AWS secret access key production env | - | Yes  |
| aws-tst-region-name | AWS region name test env | `eu-west-1` | No |
| aws-stg-region-name | AWS region name test env | `eu-west-1` | No |
| aws-prd-region-name | AWS region name test env | `eu-west-1` | No |

### Outputs


# association-registry api key action - remove

This action removes a client api key

## Example
```yaml
name: Remove client apikey
on:
  workflow_dispatch:
    inputs:
      api-key:
       description: 'Api Key'     
       required: true

      apply-env-tst:
        type: boolean
        description: 'Test'
        required: true

      apply-env-stg:
        type: boolean
        description: 'Staging'
        required: true
        
      apply-env-prd:
        type: boolean
        description: 'Production'
        required: true

jobs:
  association-registry:
    runs-on: ubuntu-latest
    steps:
    - name: remove client apikey
      uses: informatievlaanderen/association-registry-public-api-key-action/action-remove@main
      with:
          apikey: ${{github.event.inputs.api-key}}

          env-tst:  ${{ github.event.inputs.apply-env-tst }}
          env-stg:  ${{ github.event.inputs.apply-env-stg }}
          env-prd:  ${{ github.event.inputs.apply-env-prd }}
          
          aws-tst-access-key-id: ${{ secrets.AWS_TST_ACCESS_KEY_ID }}
          aws-stg-access-key-id: ${{ secrets.AWS_STG_ACCESS_KEY_ID }}
          aws-prd-access-key-id: ${{ secrets.AWS_PRD_ACCESS_KEY_ID }}

          aws-tst-secret-access-key: ${{ secrets.AWS_TST_SECRET_ACCESS_KEY }}
          aws-stg-secret-access-key: ${{ secrets.AWS_STG_SECRET_ACCESS_KEY }}
          aws-prd-secret-access-key: ${{ secrets.AWS_PRD_SECRET_ACCESS_KEY }}
          
          aws-tst-region-name: eu-west-1
          aws-stg-region-name: eu-west-1
          aws-prd-region-name: eu-west-1
```

### Inputs

|Argument| Description | Default | Required |
|--------|-------------|---------|----------|
| api-key | The client api key | - | Yes |
| env-tst | Apply in test env. (`true` / `false`) | `false` | Yes |
| env-stg | Apply in staging env. (`true` / `false`) | `false` | Yes |
| env-prd | Apply in production env. (`true` / `false`) | `false` | Yes |
| aws-tst-access-key-id | AWS access key id test env | - | Yes  |
| aws-stg-access-key-id | AWS access key id staging env | - | Yes  |
| aws-prd-access-key-id | AWS access key id production env | - | Yes  |
| aws-tst-secret-access-key | AWS secret access key test env | - | Yes  |
| aws-stg-secret-access-key | AWS secret access key staging env | - | Yes  |
| aws-prd-secret-access-key | AWS secret access key production env | - | Yes  |
| aws-tst-region-name | AWS region name test env | `eu-west-1` | No |
| aws-stg-region-name | AWS region name test env | `eu-west-1` | No |
| aws-prd-region-name | AWS region name test env | `eu-west-1` | No |

### Outputs


# association-registry api key action - update

This action updates a client api key

## Example
```yaml
name: Update client apikey
on:
  workflow_dispatch:
    inputs:
      api-key:
       description: 'Api Key'     
       required: true

      grant-access-association-registry:
        type: boolean
        description: 'Grant association-registry access'
        required: true 
         
      grant-access-sync:
        type: boolean
        description: 'Grant sync access'
        required: true

      client:
        description: 'ClientName'     
        required: true
        
      email:
        description: 'Email'     
        required: true

      plan:
        type: choice
        description: 'Plan'
        options:
        - standard
        default: standard

      apply-env-tst:
        type: boolean
        description: 'Test'
        required: true

      apply-env-stg:
        type: boolean
        description: 'Staging'
        required: true
        
      apply-env-prd:
        type: boolean
        description: 'Production'
        required: true

jobs:
  association-registry:
    runs-on: ubuntu-latest
    steps:
    - name: update client apikey
      uses: informatievlaanderen/association-registry-public-api-key-action/action-update@main
      with:
          apikey: ${{github.event.inputs.api-key}}
          client:  ${{ github.event.inputs.client }}
          email: ${{ github.event.inputs.email }}
          plan:  ${{ github.event.inputs.plan }}
          
          access-sync:  ${{ github.event.inputs.grant-access-sync }}
          access-association-registry:  ${{ github.event.inputs.grant-access-association-registry }}
          
          env-tst:  ${{ github.event.inputs.apply-env-tst }}
          env-stg:  ${{ github.event.inputs.apply-env-stg }}
          env-prd:  ${{ github.event.inputs.apply-env-prd }}
          
          aws-tst-access-key-id: ${{ secrets.AWS_TST_ACCESS_KEY_ID }}
          aws-stg-access-key-id: ${{ secrets.AWS_STG_ACCESS_KEY_ID }}
          aws-prd-access-key-id: ${{ secrets.AWS_PRD_ACCESS_KEY_ID }}

          aws-tst-secret-access-key: ${{ secrets.AWS_TST_SECRET_ACCESS_KEY }}
          aws-stg-secret-access-key: ${{ secrets.AWS_STG_SECRET_ACCESS_KEY }}
          aws-prd-secret-access-key: ${{ secrets.AWS_PRD_SECRET_ACCESS_KEY }}
          
          aws-tst-region-name: eu-west-1
          aws-stg-region-name: eu-west-1
          aws-prd-region-name: eu-west-1
```

### Inputs

|Argument| Description | Default     | Required |
|--------|-------------|-------------|----------|
| api-key | The client api key | -           | Yes |
| client | The client name | -           | Yes |
| email | The client email | -           | Yes |
| plan | Plan type `standard` | -           | Yes |
| access-sync | Grant sync access (`true` / `false`) | `false`     | Yes |
| access-association-registry | Grant association-registry access (`true` / `false`) | `false`     | Yes |
| env-tst | Apply in test env. (`true` / `false`) | `false`     | Yes |
| env-stg | Apply in staging env. (`true` / `false`) | `false`     | Yes |
| env-prd | Apply in production env. (`true` / `false`) | `false`     | Yes |
| aws-tst-access-key-id | AWS access key id test env | -           | Yes  |
| aws-stg-access-key-id | AWS access key id staging env | -           | Yes  |
| aws-prd-access-key-id | AWS access key id production env | -           | Yes  |
| aws-tst-secret-access-key | AWS secret access key test env | -           | Yes  |
| aws-stg-secret-access-key | AWS secret access key staging env | -           | Yes  |
| aws-prd-secret-access-key | AWS secret access key production env | -           | Yes  |
| aws-tst-region-name | AWS region name test env | `eu-west-1` | No |
| aws-stg-region-name | AWS region name test env | `eu-west-1` | No |
| aws-prd-region-name | AWS region name test env | `eu-west-1` | No |

### Outputs

