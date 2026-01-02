terraform {
  backend "s3" {
    bucket = "hellocdkstack-bucket83908e77-gtnwol5hfpqo"
    region = "ap-northeast-1"
    key = "test/terraform.tfstate"
  }
}