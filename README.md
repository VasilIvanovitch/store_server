# store_server
# Django Website Project

This is an educational project for a web application developed using the Django framework on the backend, based on the tutorial course available at [https://stepik.org/course/125859/info](https://stepik.org/course/125859/info).

The project includes user authentication and registration functionality, as well as a demo payment integration using the Stripe service. Redis and Celery are utilized for certain features within the project.

PostgreSQL is used as the database for this website.

The project is prepared for deployment on the backend server.

The `Server` branch contains the code that is currently deployed on the remote server for the website. It includes the necessary `docker-compose.yml` and `Dockerfile` files for deployment within a Docker container. The database used by the application runs independently on another server.

## Getting Started

To get started with the project, follow these steps:

1. Create a working directory for the project.
2. Clone the repository into the working directory, specifically from the Server branch to access the deployed code.
3. Copy the docker-compose.yml file and the nginx folder to the working directory.
4. Review the docker-compose.yml file and make any necessary adjustments to match your environment and configuration.
5. Set up the necessary environment variables for the project, including those related to the database and Stripe integration.
6. Build and run the Docker container to deploy the website.
7. Access the website on the provided URL.

## Dependencies

The project has the following dependencies:

- Django
- Redis
- Celery
- PostgreSQL
- Stripe

Make sure to install these dependencies before running the project.

## Contributions

Contributions to the project are welcome. If you find any issues or have suggestions for improvements, please feel free to submit a pull request.

## License

The project is released under the MIT License. See the [LICENSE](LICENSE) file for more details.
