variable "API_KEY" {
  description = "API key for To-do application"
  sensitive = true  
}

variable "API_TOKEN" {
  description = "API token for To-do application"
  sensitive = true  
}
variable "database_password" {
  description = "Database password"
  sensitive = true  
}

variable "mongodb_connectionstring" {
  description = "MongoDB Connection string"
  sensitive = true  
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
  sensitive = true  
}
variable "LOGGLY_TOKEN" {
  description = "Token for loggly application"
  sensitive = true  
}