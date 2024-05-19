# Using Terraform to Deploy Azure Resources

This project uses Terraform to manage and deploy resources on Microsoft Azure. 

The Terraform configuration provided automates the creation of a service plan, a Linux web app, and a Cosmos DB account. 

Below, you'll find detailed instructions on setting up and using Terraform with this code.

## Prerequisites
Before you start, ensure you have the following installed:

- Terraform (version >= 3.8)
- Azure CLI
- An Azure account with the necessary permissions to create resources

## Project Structure
- main.tf: Main Terraform configuration file defining the Azure resources.
- variables.tf: Defines the variables used in the configuration.
- outputs.tf: (Optional) Outputs to display after Terraform completes.
- terraform.tfvars.example: Example file to store variable values (not provided, to be created by the user).
- Configuration
Provider Configuration: Specifies the AzureRM provider and configures the backend for storing the Terraform state in an Azure Storage Account.

```bash
terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">= 3.8"
    }
  }
  backend "azurerm" {
    resource_group_name  = "YOUR_RESOURCE_GROUP_NAME"
    storage_account_name = "YOUR_STORAGE_ACCOUNT_NAME"
    container_name       = "YOUR_CONTAINER_NAME"
    key                  = "terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
}
```

## Data and Resource Definitions:

- Resource Group Data: Fetches details of an existing resource group.
- Service Plan: Creates an App Service plan for the web app.
- Linux Web App: Deploys a Linux web app using a Docker image.
- Cosmos DB Account: Configures a Cosmos DB account for MongoDB.
- Cosmos DB Database: Creates a MongoDB database within the Cosmos DB account.

## Variables
Create a variables.tf file to define the input variables for the configuration:

```bash
variable "API_KEY" {}
variable "API_TOKEN" {}
variable "BOARD_ID" {}
variable "DOING_LIST_ID" {}
variable "DONE_LIST_ID" {}
variable "SECRET_KEY" {}
variable "TO_DO_LIST_ID" {}
variable "mongodb_connectionstring" {}
variable "resource_group_name" {}
variable "web_app_name" {}
variable "cosmosdb_account_name" {}
```
## Setting Up
- Initialize Terraform:
Run the following command to initialize Terraform. This will download the required providers and set up the backend.

```bash
terraform init
```

## Create a terraform.tfvars File: 
Create a terraform.tfvars file to provide values for the variables defined in variables.tf. You can use the terraform.tfvars.example template provided and rename it to terraform.tfvars.

```bash
# terraform.tfvars.example

# Replace these values with your own
API_KEY = "your_api_key"
API_TOKEN = "your_api_token"
BOARD_ID = "your_board_id"
DOING_LIST_ID = "your_doing_list_id"
DONE_LIST_ID = "your_done_list_id"
SECRET_KEY = "your_secret_key"
TO_DO_LIST_ID = "your_to_do_list_id"
mongodb_connectionstring = "your_mongodb_connection_string"
resource_group_name = "your_resource_group_name"
web_app_name = "your_web_app_name"
cosmosdb_account_name = "your_cosmosdb_account_name"
```

## Rename the Example File:
Rename terraform.tfvars.example to terraform.tfvars.

```bash
mv terraform.tfvars.example terraform.tfvars
```

## Edit terraform.tfvars:
Open the terraform.tfvars file in a text editor and replace the placeholder values with your actual data.

## Deploy Resources:
Run the following commands to deploy the resources to Azure.

```bash
terraform plan
terraform apply
```


The plan command will show you what Terraform will do, and apply will execute the plan and create the resources.

## Resources Created
- Service Plan: An App Service plan named terraformed-asp.
- Linux Web App: A Linux web app running a Docker container.
- Cosmos DB Account: A Cosmos DB account configured for MongoDB.
- Cosmos DB Database: A MongoDB database within the Cosmos DB account.

## Notes
- State Management: Terraform uses Azure Storage to manage the state file. Ensure the specified storage account and container exist.
- Secrets Management: Sensitive information such as API keys and connection strings are managed via Terraform variables. Ensure these are securely handled.

## Cleaning Up
To destroy all resources created by Terraform, run:

```bash
terraform destroy
```


This will remove all resources defined in the configuration.

## Conclusion
This setup leverages Terraform to automate the deployment of web applications and databases on Azure, ensuring consistency and repeatability. Modify the provided Terraform scripts to suit your project's needs and follow the best practices for infrastructure as code.


