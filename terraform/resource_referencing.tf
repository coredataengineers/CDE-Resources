# New user to be created
resource "aws_iam_user" "new_joiner" {
  name = "martin"
}


# Creating group to add new user in it.
resource "aws_iam_group" "data_engineers" {
  name = "data_engineering_team"
}


# Resource to add new user in the new group
resource "aws_iam_group_membership" "team" {
  name = "user_added_to_group"

  users = [
    aws_iam_user.new_joiner.name # referenced the user resource created on line 2
  ]

  group = aws_iam_group.data_engineers.name # referenced the group resource created on line 8
}


# =============================================================================

# Create random password to be saved 
resource "random_password" "database_password" {
  length  = 16
  special = true
}


# create ssm paramter to save the database password
resource "aws_ssm_parameter" "db_password_ssm_params" {
  name  = "finance_database_password"
  type  = "String"
  value = random_password.database_password.result
}
