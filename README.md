This project is based on Python3.12 and Django Web Framework.

## Requirements
- Docker
- Docker Compose
- Python 3.12.1

## Installation via Docker
 - Create and update local env file with environment variables from env_sample file.
 - Setup docker and docker compose on your local machine.
 - Start up docker service.
 - Pull recent changes from remote repository `git clone git@github.com:kmazi/reconcile.git`.
 - Change directory to application folder `reconcile`.
 - Run `docker-compose --file dev.docker-compose.yml up --build -d` to build container and start up the app. This command creates a container running the reconcile app, postgres database container and a pgadmin container. Please make sure ports 8000, 8500 are free on your machine.
 - Access app default url `http://127.0.0.1:8000`
 - Access file upload endpoint by sending a post request to `http://127.0.0.1:8000/v1/reconciliation/upload_csv`. Send a form with two fields named `source_file` and `target_file`
 - Get file reconciliation report by making a get request to the endpoint `http://127.0.0.1:8000/v1/reconciliation/report/<int:report_id>
 - Access database via pgadmin `http://127.0.0.1:8500`. Open `dev.docker-compose.yml` file in the application root directory and change `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD` to your desired values. You could use the default values `touchstone@gmail.com` and `password` as username and password respectively. to access the database via pgadmin.

 - Run `docker-compose --file dev.docker-compose.yml stop` to stop the app. or
 - Run `docker-compose --file dev.docker-compose.yml down` to destroy the app containers.
