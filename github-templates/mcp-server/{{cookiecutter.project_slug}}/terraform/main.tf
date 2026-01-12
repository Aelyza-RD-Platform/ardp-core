terraform {
  required_version = ">= 1.5.0"
  
  backend "s3" {
    bucket = "aelyza-tech-terraform-state"
    key    = "{{ cookiecutter.project_slug }}/terraform.tfstate"
    region = "{{ cookiecutter.aws_region }}"
  }
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "{{ cookiecutter.aws_region }}"
  
  default_tags {
    tags = {
      Company   = "{{ cookiecutter.company }}"
      ManagedBy = "ARDP"
      Project   = "{{ cookiecutter.project_slug }}"
    }
  }
}

# Module ECR depuis ARDP Core
module "ecr_repository" {
  source = "git::https://github.com/Aelyza-RD-Platform/ardp-core.git//terraform-modules/aws-ecr?ref=v1.0.0"
  
  repository_name = "{{ cookiecutter.project_slug }}"
  
  tags = {
    Project   = "{{ cookiecutter.project_slug }}"
    Component = "MCP-Server"
  }
}

{% if cookiecutter.use_postgres == "y" %}
# Module RDS depuis ARDP Core (si nécessaire)
module "rds_instance" {
  source = "git::https://github.com/Aelyza-RD-Platform/ardp-core.git//terraform-modules/aws-rds?ref=v1.0.0"
  
  instance_name = "{{ cookiecutter.project_slug }}-db"
  engine_version = "15.4"
  
  tags = {
    Project   = "{{ cookiecutter.project_slug }}"
    Component = "Database"
  }
}
{% endif %}

# Outputs
output "ecr_repository_url" {
  value = module.ecr_repository.repository_url
}

{% if cookiecutter.use_postgres == "y" %}
output "database_url" {
  value     = module.rds_instance.database_url
  sensitive = true
}
{% endif %}
