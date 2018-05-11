# Django-Survey

Django project that allows you to create surveys and allow other users to sign up and answer them.

# Authors 🖋️

Rashad Kamsheh.

# Introduction

As an admin, this app will allow you to create sruveys, add questions and assign them to categorys and even add 
responses. This can be done through the admin interface or the REST API.

As a user, you will be able to answer surveys and leave your input after signing up.

# Get started

First, install all the required framworks and their supported versions.

```
pip install -r requirements.txt
```

Then, make sure you migrate to sync the database

```
python manage.py migrate
```

Now you can start the server and test the web app.

```
python manage.py runserver localhost:8000
```
