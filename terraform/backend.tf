# managing our state file in an s3 bucket
terraform {
  backend "s3" {
    bucket = "cde-terraform-state"
    region = "eu-central-1"
    key    = "dev/dev.tfstate"
  }
}