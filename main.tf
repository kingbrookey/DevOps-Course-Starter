terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">= 3.8"
    }
  }
  backend "azurerm" {
    resource_group_name  = "Cohort28_KinEbr_ProjectExercise"
    storage_account_name = "kingsleymod12store"
    container_name       = "kingsleymod12storecontainer"
    key                  = "terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
  client_id       = var.TF_VAR_client_id
  client_secret   = var.TF_VAR_client_secret
  tenant_id       = var.TF_VAR_tenant_id
  subscription_id = var.TF_VAR_subscription_id
}

data "azurerm_resource_group" "main" {
  name     = "Cohort28_KinEbr_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
  name                = "terraformed-asp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_web_app" "main" {
  name                = "kingsleymod12app"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id

  site_config {
    always_on = false
    ftps_state = "FtpsOnly"
    http2_enabled = true

    application_stack {
      docker_image     = "kingbrookey/my-todo-app-mod8"
      docker_image_tag = "latest"
      
    }
  }

  app_settings = {
    "API_KEY" = TF_VAR_API_KEY
    "API_TOKEN" = var.TF_VAR_API_TOKEN
    "BOARD_ID" = var.TF_VAR_BOARD_ID
    "DOCKER_REGISTRY_SERVER_URL" = "https://docker.io"
    "DOING_LIST_ID" = var.TF_VAR_DOING_LIST_ID
    "DONE_LIST_ID" = var.TF_VAR_DONE_LIST_ID
    "FLASK_APP" = "todo_app/app"
    "FLASK_ENV" = "production"
    "SECRET_KEY" = var.TF_VAR_SECRET_KEY
    "TO_DO_LIST_ID" = var.TF_VAR_TO_DO_LIST_ID
    "WEBSITES_ENABLE_APP_SERVICE_STORAGE" = "false"
    "WEBSITES_PORT" = "5000"
  }

    connection_string {
    name  = "Database"
    type  = "SQLServer"
    value = var.TF_VAR_mongodb_connectionstring
  }

  client_affinity_enabled = true
  https_only = true 
}

resource "azurerm_cosmosdb_account" "db" {
  name                = "terraformed-cosmos-db-mod12"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "MongoDB"

  enable_automatic_failover = false

  capabilities {
    name = "EnableServerless"
  }

  capabilities {
    name = "EnableAggregationPipeline"
  }

  capabilities {
    name = "mongoEnableDocLevelTTL"
  }

  capabilities {
    name = "MongoDBv3.4"
  }

  capabilities {
    name = "EnableMongo"
  }

  consistency_policy {
    consistency_level       = "BoundedStaleness"
    max_interval_in_seconds = 300
    max_staleness_prefix    = 100000
  }
  lifecycle { prevent_destroy = true }

  geo_location {
    location          = "westus"
    failover_priority = 0
  }
}

resource "azurerm_cosmosdb_mongo_database" "database" {
  name                = "terraformed-cosmos-mongo-db-mod12"
  resource_group_name = data.azurerm_resource_group.main.name
  account_name        = "terraformed-cosmos-db-mod12"
}