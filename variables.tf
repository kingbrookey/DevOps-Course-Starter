variable "API_KEY" {
  description = "API key for To-do application"
}

variable "API_TOKEN" {
  description = "API token for To-do application"
}
variable "database_password" {
  description = "Database password"
}

variable "mongodb_connectionstring" {
  description = "MongoDB Connection string"
}

variable "BOARD_ID" {
  description = "ID for To do app board"
}

variable "DOING_LIST_ID" {
  description = "ID for Doing list on To do app board"
}

variable "DONE_LIST_ID" {
  description = "ID for Done list on To do app board"
}

variable "TO_DO_LIST_ID" {
  description = "ID for To do list on To do app board"
}

variable "SECRET_KEY" {
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