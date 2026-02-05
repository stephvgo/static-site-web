terraform {
  backend "s3" {
    bucket = "steph-vgo-website"
    key    = "terraform/state.tfstate"
    region = "us-east-1"
  }
}
