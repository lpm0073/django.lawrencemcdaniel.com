# django.lawrencemcdaniel.com


## Resources
* Zappa setup: https://blog.apcelent.com/deploy-flask-aws-lambda.html
* Django: https://www.djangoproject.com/
* Django Bootstrap: https://django-bootstrap3.readthedocs.io/en/latest/index.html



## Local dev environment setup
1. AWS Credentials
2. Install AWS CLI
```
pip install awscli
```
3. Create Virtual Environment
```
# cd to the local git repository
virtualenv -p python3.6 .env3
source .env3/bin/activate
pip install -r requirements.txt
zappa init
```

4. Run local Django web server:
```
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
```
5. Deploy app to AWS
```
zappa deploy dev
```

6. Subsequent app updates to aws
```
zappa update dev
```
