terraform {
  required_providers {
    iosxe = {
      source  = "CiscoDevNet/iosxe"
      version = "~> 0.5.1" 
    }
  }
}
provider "iosxe" {
  username = "admin"
  password = "admin"
  url  = "https://10.1.1.73" 
}