# Exercise
Create products in Django and sync in Flask via RabbitMQ
Youtube: https://www.youtube.com/watch?v=0iB5IPoTDts


# Django app to create products
- `pip3 install django`
- `pip3 install djangorestframework`
- Create new project: `django-admin startproject admin`
- `cd admin`
- `python3 manage.py runserver`
- Delete `dbsqlite`
- Create `Dockerfile` and `docker-compose.yaml`
- Create requirements.txt //to list all dependencies for the app
- Run `docker-compose up`
- Get into docker container: `docker-compose exec backend sh`
Inside container run: `python manage.py startapp products`. this creates a folder
products alongside admin.
- Delete `dbsqlite`.
- Goto `settings.py` in admin app and add the following:
    - `rest_framework`, `corsheaders`, `products` under `INSTALLED_APPS`
    - `corsheaders.middleware.CorsMiddleware` in `MIDDLEWARE`
    - a new constant `CORS_ORGIN_ALLOW_ALL = True` at the end.
    - update `DATABASES` from `sqlite3` to `mysql` information.
- Create entity classes (models) in `products/models.py`
- Generate migrations (db tables) for models:
    - Start container: `docker-compose exec backend sh`
    - Run: `python manage.py makemigrations`. See `0001_initial.py` file generated under `products\migrations`
    - Run: `python manage.py migrate`
    - Go to database to see generated tables `products_product` and `products_user` under `admin`
- Create serializers for entities:
    - Create `serializers.py` in `products`
- Create views:
    - In `views.py`, add `ProductViewSet` for REST endpoints
    - create `urls.py` for request to method mapping.
    - update `urls.py` in admin app with `api/` route.
- Create users: `curl -d "{\"title\": \"t\", \"image\":\"i\"}" -X POST http://localhost:8000/api/products`
- Get users: `curl -X GET http://localhost:8000/api/products/1`
- Random user (add users manually): `curl -X GET http://localhost:8000/api/user`

# Flask app (directory `flask-app`)
Catches the event from Django app thru RabbitMQ and creates the product in its own db.
- Run `main.py` directly: `python main.py`. Available at `http://localhost:5000`
- Run docker: `docker-compose up`. Available at `http://localhost:8001`
- login to shell: `docker-compose exec backend sh`. Run the following commands in the container:
    - `python manager.py db --`
    - `python manager.py db init`
    - `python manager.py db migrate`
    - `python manager.py db upgrage`
    
# RabbitMQ
- Create account in RabbitMQ as a service. Create an instance
- Copy the AMQP url.
- In `products` app, create `producer.py` and `consumer.py` (see details there). Add publish call in `create` view.
- Start `admin` docker up and go into the container.