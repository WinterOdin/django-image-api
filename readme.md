## Image parser app 

This app uses [django image-kit](https://django-imagekit.readthedocs.io/en/latest/) for image parsing. 

#### Why image-kit 
ImageKit comes with a bunch of image processors for common tasks like resizing and cropping, the developer doesn't need to write a bunch of code. Just add the most common fields with size to your Django model and you are set. It also keeps the original picture for other purposes 

#### Alternatives

Another simple alternative: using [AWS image resize](https://aws.amazon.com/blogs/compute/resize-images-on-the-fly-with-amazon-s3-aws-lambda-and-amazon-api-gateway/) 

#### Instalation 
Create virtualenv and activate it
```
virtualenv env
env/Scripts/activate
```
then pip install requirements
```
pip install -r requirements
```
Now you need to set your s3 bucket credentials, use .env
```
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''
```

then you can do
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
```
then go to 
```
http://127.0.0.1:8000/api/picture/
```
and you are set to upload a new pic
