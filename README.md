# FineFoodsRestAPI

# Requirements
Django==1.11.2

djangorestframework==3.8.2

Python==2.7.10
# Installation
pip install virtualenv

pip install Django

pip install djangorestframework
# Creating Project and Application
django-admin startproject FineFoods

python manage.py startapp MyApi
# models.py
In modles I am taking productId, userId, profileName, helpfulness, review, review_time, review_summary and review_text based on model.Fields()

If we do any changes in model we should do model makemigratiuons and migrate.

python manage.py makemigrations

python manage.py migrate
# serializers.py
Serializers are used to return json data from our models.

Here we have to give the fileds to return in API like fields = ['pk', 'productId', 'userId', 'profileName', 'helpfulness', 'review', 'review_time', 'review_summary', 'review_text']
