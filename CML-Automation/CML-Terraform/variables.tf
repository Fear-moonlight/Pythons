variable "routers" {
  description = "List of routers with their names and URLs"
  type = list(object({
    name = string
    url  = string
  }))
}