This project is based on Python3.12 and Django Web Framework.

## Requirements
- Docker
- Docker Compose
- Python 3.12.1

## Installation via Docker
 - Update local env file with environment variables from env_sample file.
 - Setup docker and docker compose on your local machine.
 - Start up docker service.
 - Pull recent changes from remote repository `git clone git@github.com:kmazi/reconcile.git`.
 - Change directory to application folder `reconcile`.
 - Run `docker-compose --file dev.docker-compose.yml up --build -d` to build container and start up the app. This command creates a container running the reconcile app, postgres database container and a pgadmin container.
 - Access app via url `http://127.0.0.1:8000`
 - Access database via pgadmin `http://127.0.0.1:8500`. Open `dev.docker-compose.yml` file in the application root directory and change `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD` to your desired values. You could use the default values `touchstone@gmail.com` and `password` as username and password respectively.

 - Run `docker-compose --file dev.docker-compose.yml stop` to stop the app.
