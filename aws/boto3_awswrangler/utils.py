from boto3 import Session


def aws_sesion():
    """
     This function store the
     the aws profile in session, Documenation in the below link
     https://boto3.amazonaws.com/v1/documentation/api/latest/guide/session.html
     Note: Your credentials should not be expose in a plain text..
    """
    session = Session(
        aws_access_key_id="YourAccessKey",
        aws_secret_access_key="YourSecretKey",
        region_name="eu-central-1"
        )

    return session
