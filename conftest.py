import pytest
from loguru import logger
import os
from dotenv import load_dotenv
from methods import REST_API_Methods

load_dotenv()

logger.add('logs/at_rest_api_kebox_{time:MM-DD_HH:mm:ss}.log', format='{time:MM-DD HH:mm:ss} | {level} | {message}', level='TRACE')

@pytest.fixture(autouse=True, scope='session')
def context():
    context = {}
    context['rest_api_methods'] = REST_API_Methods()
    return context


@pytest.fixture(autouse = True)
def log_test_progress(request):
    logger.info(f"run {request.node.name}:")
    yield
    logger.info(f"{request.node.name} is over")



