terraform {
  backend "s3" {
    bucket  = "cde-capstone-project-backend-bucket"
    key     = "state/terraform.tfstate"
    region  = "eu-west-2"
    encrypt = true
  }
}