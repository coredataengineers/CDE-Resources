# Create SSM parameter resource

resource "aws_ssm_parameter" "foo" {
  name  = "database_root_password"
  type  = "String"
  value = "xyz"
}