# Backend

* API Backend and Admin
* This project based on [cookiecutter-django](https://cookiecutter-django.readthedocs.io/en/latest/)
* Strongly recommend using pycharm ...

## Basic Concept
### Model and View and Serializer
#### View
* 일반적인 Controller 의 역할 입니다.
* `Permission`, `Authentication`, `Throttling` 등 과 같은 Business Logic을 처리전에 거쳐야할 작업들을 처리합니다.
* 위 과정에서 파라미터 Validation 등과 같은 작업을 위해 `Serializer` 를 상황에 맞게 사용합니다.
* 응답 데이터의 serialization 을 위해 `Serializer` 를 활용합니다. 

#### Model 
* [중요] Business Logic 은 특별한 상황을 제외하고는 모델에 작성합니다. `classmethod`, `method`, `property` 를 활용하여 작성합니다.


## Prerequisite
* python3.6
* Django 2.0.13
* ...


## Installation and Run
### DB 
```bash
$ brew install postgresql
$ createuser <project_name> --interactive 
# plz make password "qwer1234" for shared env 
$ createdb -O <project_name> <project_name>
$ psql <project_name>
alter user <project_name> with password 'qwer1234';
# ALTER ROLE
```

### Redis
```bash
$ docker run -p 6379:6379 -d redis:2.8
```


### Web Backend
```bash
$ export DJANGO_READ_DOT_ENV_FILE=True
$ python manage.py migrate
$ python manage.py runserver
...
```
