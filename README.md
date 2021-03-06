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
# settings.py in Project folder
Here we have to add rest_framework module and our application name in INSTALLED_APPS list.
# urls.py
This file is used to make API urls by importing views from views.py file. We have an urls.py in project folder also which is used for admin connection and app urls connection.
# admin.py
Here we have to register our model by importing from models.py
**Example: admin.site.register(FineFoods)**
# models.py
In modles I am taking productId, userId, profileName, helpfulness, review, review_time, review_summary and review_text based on model.Fields()

If we do any changes in model we should do model makemigratiuons and migrate.

python manage.py makemigrations

python manage.py migrate
# serializers.py
Serializers are used to return json data from our models.

Here we have to give the fileds to return in API like fields = ['pk', 'productId', 'userId', 'profileName', 'helpfulness', 'review', 'review_time', 'review_summary', 'review_text']
# views.py
My API can allow GET, PUT, PATCH, DELETE operations.

To perform these opeartions Iam using generics.RetrieveUpdateDestroyAPIView, generics.ListAPIView and mixins.CreateModelMixin mogules.

When we posting one documnet will get one unique id for every document which is nothing but primary key. By using this PK we can retrieve the documnet also.

http://127.0.0.1:8000/finefoods/10/; Here 10 is PK
# Running Commands
python manage.py runserver
  
 The development server at http://127.0.0.1:8000/

**My API Url is  http://127.0.0.1:8000/finefoods/**
 
I took 30 documents to work with API.

# Query Filters
review, orderby, total, productid, userid

On this API we can apply following filters:

Example url is http://127.0.0.1:8000/finefoods/?review=&orderby=&total=&productid=&userid

## review:
If we want particular review data.

**Example: review=5.0**
## orderby:
I am taking asc and desc  orders.

asc order is for low review to highest review.

desc order is for highest rate to lowest rate.

**Example: orderby=desc**

**Example: orderby=asc**
## total:
To return number of doucuments you want.

Here we can apply both total and orderby filter.

**Example: orderby=desc&total=4**
 
**Example: orderby=asc&total=20**
## productid:
By giving productid we can get particular document

**Example: productid=B00813GRG4**
## userid
By giving userid we can get our required document.

**Example: userid=A21BT40VZCCYT4**

## Note:
**I did all the above 5 combinations of filters in query. We can apply more than one filter or all the filters at a time.**

# Pagination
I am using pagination feature also in settings.py file by using DEFAULT_PAGINATION_CLASS and taking 10 documents per page

