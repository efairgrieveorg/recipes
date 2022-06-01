terraform {
    required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "~> 3.0"
        }
    }
    backend "s3" {
        region = "eu-west-1"
    }
}

variable "project" {
    description = "GitHub repository name, passed by the workflow"
    type = string
}

variable "env" {
  description = "The environment"
  type = string
}

resource "aws_s3_bucket" "recipes" {
  bucket = "${var.env}-euans-recipes"
}

resource "aws_s3_bucket" "test" {
  bucket = "${var.env}-testing-recipes"
}


data "archive_file" "recipes" {
  type = "zip"
  source_dir = "${path.module}/markdown_table_gen"
  output_path = "${path.module}/${var.project}-latest.zip"
}

resource "aws_s3_bucket_object" "recipes" {
  bucket = aws_s3_bucket.recipes.id
  key = "${var.project}-latest.zip"
  source = data.archive_file.recipes.output_path
  etag = filemd5(data.archive_file.recipes.output_path)
  lifecycle {
    ignore_changes = [
        etag
    ]
  }
}