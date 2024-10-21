# Reference an an existing iam user

data "aws_iam_user" "existing_user" {
  user_name = "xyz"
}


# Inject xyz user's ARN into an SSM parameter to be saved.
resource "aws_ssm_parameter" "iyiola_user_arn" {
  name  = "xyz"
  type  = "String"
  value = data.aws_iam_user.existing_user.arn
}