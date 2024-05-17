variable "API_KEY" {
  description = "API key for To-do application"
}

variable "TF_VAR_API_TOKEN" {
  description = "API token for To-do application"
}
variable "TF_VAR_database_password" {
  description = "Database password"
}

variable "TF_VAR_mongodb_connectionstring" {
  description = "MongoDB Connection string"
}

variable "TF_VAR_BOARD_ID" {
  description = "ID for To do app board"
}

variable "TF_VAR_DOING_LIST_ID" {
  description = "ID for Doing list on To do app board"
}

variable "TF_VAR_DONE_LIST_ID" {
  description = "ID for Done list on To do app board"
}

variable "TF_VAR_TO_DO_LIST_ID" {
  description = "ID for To do list on To do app board"
}

variable "TF_VAR_SECRET_KEY" {
  description = "Secret key for accessing To do app board"
}

variable "TF_VAR_client_secret" {
  description = "Client Secret key for Service principal"
}

variable "TF_VAR_client_id" {
  description = "Client ID key for Service principal"
}

variable "TF_VAR_tenant_id" {
  description = "Tenant ID key for Service principal"
}

variable "TF_VAR_subscription_id" {
  description = "Subscription ID key for Service principal"
}