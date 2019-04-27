# Ingresse_API_Test

This project is a simple API user.

## Run Project:
```sh

export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```

## Flask Routes:
```
Endpoint         Methods  Rule

---------------  -------  -----------------------------

login.login      POST     /login

static           GET      /static/<path:filename>

user.change_id   PUT      /change_by_id/<identificator>

user.defalt      GET      /

user.delete_id   DELETE   /delete_by_id/<identificator>

user.register    POST     /register

user.show        GET      /show

user.show_by_id  GET      /show_by_id/<identificator>
```

## Create db and make migrations:

```sh
flask db init
flask db migrate
```
