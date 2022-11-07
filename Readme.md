# Alembic Comands

`Execute all migrations -` alembic upgrade head

`Undo all migrations -` alembic downgrade base

`generate migrations -` alembic revision --autogenerate -m "commit text"

`start alembic asynchronous file -` alembic init -t async migrations

# Create VM and start application commands

`Load enviroment variables or create a new "VM" -` pipenv shell

`Install dependecies from Pipfile -` pipenv install

`Add new dependecies -` pipenv insatll `dependencie name`

`Start application server -` uvicorn app.main:app --port 8080 --reload

`Start application from root directory -` export PYTHONPATH=$PWD (OBS: you need to run this command on a terminal in the root directory of your project )

# Tutorials

`Alembic configuration with FastApi -` https://www.youtube.com/watch?v=eXj1gdDLKho

`FastApi async project -` https://www.youtube.com/watch?v=1CZZAhwqyco&t=4011s

`FastApi crash course -` https://www.youtube.com/watch?v=gQTRsZpR7Gw&t=4848s

# Repos examples

`FastApi bigger applications -` https://github.com/tiangolo/full-stack-fastapi-postgresql

`FastApi alembic configuration -` https://github.com/DJWOMS/fastapi-microblog

`FastApi crash course -` https://github.com/faraday-academy/fast-api-lms/tree/1-initial-app-setup

# Hosts

`localhost:5050` access to see the database

`localhost:{PORT}` host of application. You can use `uvicorn app.main:app --port 8080 --reload ` and change the host your application is runnig

`localhost:{PORT}/docs` access to see the api `Swagger` documentation
