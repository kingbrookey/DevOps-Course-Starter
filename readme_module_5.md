# Flask To-Do App Dockerized

This is a Dockerized Flask application for a To-Do list.

## Getting Started

These instructions will help you set up and run the application using Docker in both development and production environments.

### Prerequisites

- Docker: Ensure you have Docker installed on your system. You can download and install it from [Docker's official website](https://www.docker.com/get-started).

### Development Container

To run the application in a development environment:

1. Build the development Docker image:
```bash
  docker build --target development --tag todo-app:dev .
```

Create an .env file in the project root and set the environment variables required for your application. For example:
TRELLO_API_KEY=your_trello_api_key
TRELLO_API_TOKEN=your_trello_api_token
BOARD_ID=your_board_id
TODO_LIST_ID=your_todo_list_id
DONE_LIST_ID=your_done_list_id


2. Start the development container with hot-reloading and bind mounting the project directory:  Replace $(pwd) with the path to your project directory:
```bash
docker run --env-file ./.env -p 5000:80 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev
```

3. Access the application at http://localhost:5000. Flask will provide detailed logging and automatically reload the app when you edit Python files.

To run the application in a production environment:

1. Build the production Docker image:
```bash
docker build --target production --tag todo-app:prod .
```
2. Set the required environment variables for your application, either by creating an .env file or by specifying them in your production environment.

3. Start the production container:
```bash
docker run --env-file ./.env -p 80:5000 todo-app:prod
```
4. Access the production application at http://localhost.

### Additional Notes
The development container uses Flask's development server with hot-reloading for quick code changes during development.
The production container uses Gunicorn to run the application, suitable for production deployments.
Please ensure that you follow best practices for managing secrets and environment variables, especially in production environments.

[click here to read the azure deployment readme](./readme_azure_deployment_steps.md)


[and here to read about the encryption used in the To do application](./readme_encryption_status.md)

#### Happy coding!
