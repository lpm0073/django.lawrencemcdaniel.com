# Serverless Django
This is a serverless implementation of Python Django running on AWS Lambda & RDS via API Gateway.

View the site: https://django.lawrencemcdaniel.com

## Resources
* Zappa setup: https://blog.apcelent.com/deploy-flask-aws-lambda.html
* Django - Zappa Guide: https://edgarroman.github.io/zappa-django-guide/
* Django: https://www.djangoproject.com/
* Django Environment: https://github.com/joke2k/django-environ


## Local dev environment setup
1. add AWS Credentials to ~/.aws/credentials
2. Install AWS CLI
```
pip install awscli
```
3. Create Python Virtual Environment
```
# cd to the local git repository
virtualenv -p python3.6 .env3   # note: Zappa requires Python 3.6
source .env3/bin/activate
pip install -r requirements.txt
```

4. Run local Django web server:
```
# cd into repository
source .env3/bin/activate
python mysite/manage.py runserver
```
5. Zappa commands
```
zappa init         # see notes below on installation details
zappa deploy dev   # Deploy app to AWS
zappa undeploy dev # Delete from AWS
zappa update dev   # update existing app to AWS
zappa tail         # view Lambda execution log
zappa -h
```

## settings.py notes
- DATABASES: changed settings to AWS RDS MySQL. config settings are stored locally in mysite/.env
- ALLOWED_HOSTS: added FQDN's for amazon.com and lawrencemcdaniel.com per suggestions in teh Django - Zappa Guide
- SECRET_KEY: moved to locally-stored .env file
- DEBUG:  moved to locally-stored .env file


## Zappa setup notes
- accept all of the defaults in zappa init
- manually add vpc_config section to zappa_settings.json

## .gitignore notes
added the following:
- DjangoTemplates.env
- .env3
- django-lawrence-dev-template*.json
