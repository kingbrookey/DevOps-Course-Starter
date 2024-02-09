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
