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

Additional Notes
The development container uses Flask's development server with hot-reloading for quick code changes during development.
The production container uses Gunicorn to run the application, suitable for production deployments.
Please ensure that you follow best practices for managing secrets and environment variables, especially in production environments.

# Production Container - Manual Deployment Process
### Step 1: Put Container Image on Docker Hub registry
We will be using Docker Hub as the registry to store our production container images.

This will involve:

#### Log into DockerHub locally, with docker login
Build the image, with 
```bash
docker build --target production --tag <dockerhub_username>/<image_name>:<tag> .
```
Push the image with 
```bash
docker push <dockerhub_username>/<image_name>:<tag>
```
Make sure to replace <dockerhub_username>, <image_name>, and <tag> with your specific values.

### Step 2: Create a Web App
- Using the Azure Portal:
Create a Resource -> Web App
Select your Project Exercise resource group.
In the “Publish” field, select “Docker Container”
Under “App Service Plan”, change the “Sku and size” to “B1”.
On the next screen, select Docker Hub in the “Image Source” field, and enter the details of your image.

- Using CLI:
  First, create an App Service Plan:
  
```bash
az appservice plan create --resource-group <resource_group_name> -n <appservice_plan_name> --sku B1 --is-linux
```
Then create the Web App:

```bash
az webapp create --resource-group <resource_group_name> --plan <appservice_plan_name> --name <webapp_name> --deployment-container-image-name docker.io/<dockerhub_username>/<container-image-name>:latest
```
Note: <webapp_name> needs to be globally unique.

### Step 3: Set up environment variables
- Using the Azure Portal
Go to Settings -> Configuration in the Portal.
Add all the environment variables as “New application setting”.

- Using the CLI
Enter them individually via:

```bash
az webapp config appsettings set -g <resource_group_name> -n <webapp_name> --settings FLASK_APP=todo_app/app.
```
Or you can pass in a JSON file containing all variables by using --settings @foo.json.

### Step 4: Confirm the live site works
Browse to http://<webapp_name>.azurewebsites.net/ and confirm no functionality has been lost.

### Step 5: Find your webhook URL and get your logstream URL
This can be located under Deployment Center on the app service’s page in the Azure portal.
Take the webhook provided by the previous step, add in a backslash to escape the $, and run:

```bash
curl -dH -X POST "https://\$<deployment_username>:<deployment_password>@<webapp_name>.scm.azurewebsites.net/docker/hook"
```

This should return a link to a log-stream relating to the re-pulling of the image and restarting the app.
