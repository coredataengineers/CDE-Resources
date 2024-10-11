import logging

import awswrangler as wr
import pandas as pd
from faker import Faker
from utils import aws_sesion

# setting log level for debugging purpose
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(name)s:%(message)s'
    )


def random_profile_generator():
    """
      Static function that generate 10 random profile
      using the faker library. The data is converted
      into a pandas DataFrame.
      Doc: https://faker.readthedocs.io/en/master/
    """
    faker_object = Faker()
    logging.info("Faker object successfully created")

    random_profile_list = [faker_object.profile() for profile in range(1)]

    random_profile_df = pd.DataFrame(random_profile_list)

    return random_profile_df


def extract_random_profile_to_s3():
    """
      Function leverage awswrangler library to write
      a pandas DataFrame to Amazon s3 and register
      the object in a glue database to allow easy query
      in Amazon Athena.
      Doc: https://aws-sdk-pandas.readthedocs.io/en/stable/api.html
    """
    wr.s3.to_parquet(
        df=random_profile_generator(),
        path="s3://anythingwild/example/",
        boto3_session=aws_sesion(),
        mode="overwrite",
        dataset=True,
        database="cde",
        table="test"
        )
    return "Data successfully written to s3 and register in glue"


print(extract_random_profile_to_s3())