import os

import jsonpickle

from aws_xray_sdk.core import patch_all

from ocean_jobs.utils.logger import logger
from ocean_jobs.utils.mock import get_mock_data


patch_all()


def lambda_handler(event, context):
    logger.info("## ENVIRONMENT VARIABLES\r" + jsonpickle.encode(dict(**os.environ)))
    logger.info("## EVENT\r" + jsonpickle.encode(event))
    logger.info("## CONTEXT\r" + jsonpickle.encode(context))

    return get_mock_data()
