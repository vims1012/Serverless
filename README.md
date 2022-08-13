# Project Set-up Steps :

1) create virtual env file
2) if you need psycopg2 module then install this repo and put it and use :
    `https://github.com/jkehlerawslambda-psycopg2`

Note :- 
    1)if you run locally project thne remove this module and 
    2) if you deploy then add this module

3)if you successfully created secretsmanager then run this cmd and see output :
            aws secretsmanager describe-secret --secret-id <secretsmanager id>


# huai-capital-serverless

# Installation
Install the ```serverless``` CLI via NPM:
```
npm install -g serverless
```

# Configration for AWS CLI
- Execute below command to configure aws account
```
aws configure
```
- It will ask the below details for configuration
```
AWS Access Key ID [None]: <Your AWS  Access Key Here>
AWS Secret Access Key [None]: <Your AWS Secret Access Key Here>
Default region name [None]: <Your AWS region name Here >
Default output format [None]: json
```
- Deploy with Serverless

# Deploying
- If you haven't done so already within the ```serverless``` command, you can deploy the project at any time by running:
```
serverless deploy
```
# Monitoring
- You can monitor and debug Lambda functions and APIs via the Serverless Dashboard.
- To set it up, run the following command in an existing project and follow the prompts:
```
serverless
```
# Remove your service
- If you want to delete your service, run serverless remove. This will delete all the AWS resources created by your project and ensure that you don't incur any unexpected charges. It will also remove the service from Serverless Dashboard
```
serverless remove
```


Deployment with stage and region options : sls deploy --stage dev --region us-southeast-2
