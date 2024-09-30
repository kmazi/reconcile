Simple API to reconcile data between a target and source file(CSV) written in Python leveraging on the Django Rest Framework.

## Requirements
- Docker
- Docker Compose
- Python 3.12.1

## Installation on Local Machine
- Install [python](https://www.python.org/downloads/) 3.12 on your machine 
- Download and install [postgres](https://www.postgresql.org/docs/current/tutorial-install.html "postgres installation") database on your machine.
- Start up postgres database service
- Pull recent changes from remote repository `git clone git@github.com:kmazi/reconcile.git`.
- Change directory to application folder `reconcile`.
- Start up a virtual environment by running the command:
 `python -m venv .venv`.
- Activate the virtual environment `source .venv/bin/activate`
- Update pip `pip install --upgrade pip`
- Run `pip install -r requirements/dev.txt` to install development dependencies.
- Run `python manage.py migrate` to run migrations.
- Run `Python manage.py runserver` to start the development server.
- Link to documentation: `http://127.0.0.1:8000/v1/docs/`
- Access app default url `http://127.0.0.1:8000`
- Access file upload endpoint by sending a post request to `http://127.0.0.1:8000/v1/reconciliation/upload_csv`. Send a form with two fields named `source_file` and `target_file`
- Get file reconciliation report by making a get request to the endpoint `http://127.0.0.1:8000/v1/reconciliation/report/<int:report_id>`

## Installation via Docker
 - Create and update local env file with environment variables from env_sample file.
 - Setup docker and docker compose on your local machine.
 - Start up docker service.
 - Pull recent changes from remote repository `git clone git@github.com:kmazi/reconcile.git`.
 - Change directory to application folder `reconcile`.
 - Run `docker-compose --file dev.docker-compose.yml up --build -d` to build container and start up the app. This command creates a container running the reconcile app, postgres database container and a pgadmin container. Please make sure ports 8000, 8500 are free on your machine.
 - Link to documentation: `http://127.0.0.1:8000/v1/docs/`
 - Access app default url `http://127.0.0.1:8000`
 - Access file upload endpoint by sending a post request to `http://127.0.0.1:8000/v1/reconciliation/upload_csv`. Send a form with two fields named `source_file` and `target_file`
 - Get file reconciliation report by making a get request to the endpoint `http://127.0.0.1:8000/v1/reconciliation/report/<int:report_id>`
 - Access database via pgadmin `http://127.0.0.1:8500`. Open `dev.docker-compose.yml` file in the application root directory and change `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD` to your desired values. You could use the default values `touchstone@gmail.com` and `password` as username and password respectively. to access the database via pgadmin.

 - Run `docker-compose --file dev.docker-compose.yml stop` to stop the app. or
 - Run `docker-compose --file dev.docker-compose.yml down` to destroy the app containers.
