module "aci" {
  source = "netascode/nac-aci/aci"
  version = "0.9.3"

  yaml_files = ["aci.nac.yaml"]

  manage_tenants = true
}
