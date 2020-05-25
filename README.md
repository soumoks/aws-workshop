## AWS Workshop

This is a sample application that creates an API endpoint and the API endpoint fetches data from a DynamoDB table.

![alt text](https://github-cf.sourabh.org/images/aws-workshop-architecture.png)

* Clone the repository

```
git clone https://github.com/soumoks/aws-workshop.git
```

* Install Dependencies

```
pip install -r requirements.txt
```

* Install and configure AWS CLI. [Reference](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)

* Create DynamoDB table
```
python create_table.py
```

* Load Data
```
python load_data.py
```

* Create Lambda function and API GW manually


#### Automate deployment process using SAM or Cloudformation

* AWS SAM

#### Pre-requisites
* [AWS Account](https://portal.aws.amazon.com/billing/signup)
* [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3.6+](https://www.python.org/)
* [Docker](https://www.docker.com/products/docker-desktop)

```
sam build -t sam_template.yaml
sam package --template sam_template.yaml --output-template-file packaged.yaml --s3-bucket <s3_bucket_name>
sam deploy --template-file packaged.yaml --stack-name aws-workshop --capabilities CAPABILITY_NAMED_IAM --region us-east-1
```

* AWS Cloudformation
#### Pre-requisites
* [AWS Account](https://portal.aws.amazon.com/billing/signup)
* [AWS CLI](https://aws.amazon.com/cli/)

```
aws cloudformation create-stack --stack-name aws-workshop --template-body file://cfn_template.yaml --capabilities CAPABILITY_NAMED_IAM
```

* API GW URL is present as a Cloudformation output