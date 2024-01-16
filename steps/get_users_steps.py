import allure
from loguru import logger
from pytest_bdd import when, then
from jsonschema import validate
from validate_schems import get_users_schema
    
@allure.step("Отправляем запрос с значениями page = 1 и per_page = 6")
@when("Отправляем запрос с значениями page = 1 и per_page = 6")
def sending_request_with_values_page_1_and_per_page_6(context):
    logger.info("run step 'sending_request_with_values_page_1_and_per_page_6':")  
    context['response_get_users'] = context['rest_api_methods'].get_users(1, 6)
    logger.debug(f"get_users: {context['response_get_users']}")


@allure.step("Поличили валидный ответ")
@then("Поличили валидный ответ")
def recieved_get_users_response_is_valid(context):
    logger.info('run step \'recieved_get_users_response_is_valid\':') 
    validate(context['response_get_users'], get_users_schema)

@allure.step("Значение page равно 1")
@then("Значение page равно 1")
def page_value_is_1(context):
    logger.info('run step \'page_value_is_1\':') 
    logger.info(f'check that page values is 1:')
    try:
        logger.debug(f"context['response_get_users']['page']: {context['response_get_users']['page']}")
        assert context['response_get_users']['page'] == 1
        logger.info(f'ok')
    except AssertionError:
        logger.error(f'page value not equal 1')
        raise AssertionError(f'page value not equal 1')
       
       
@allure.step("Значение per_page равно 6")
@then("Значение per_page равно 6")
def per_page_value_is_6(context):
    logger.info('run step \'per_page_value_is_6\':') 
    logger.info(f'check that per_page values is 6:')
    try:
        logger.debug(f"context['response_get_users']['per_page']: {context['response_get_users']['per_page']}")
        assert context['response_get_users']['per_page'] == 6
        logger.info(f'ok')
    except AssertionError:
        logger.error(f'per_page value not equal 6')
        raise AssertionError(f'per_page value not equal 6') 


@allure.step("Значение page равно -1")
@then("Значение page равно -1")
def page_value_is_minus_1(context):
    logger.info('run step \'page_value_is_minus_1\':') 
    logger.info(f'check that page values is -1:')
    try:
        logger.debug(f"context['response_get_users']['page']: {context['response_get_users']['page']}")
        assert context['response_get_users']['page'] == -1
        logger.info(f'ok')
    except AssertionError:
        logger.error(f'page value not equal -1')
        raise AssertionError(f'page value not equal -1')


@allure.step("Отправляем запрос с значениями page = -1 и per_page = -6")
@when("Отправляем запрос с значениями page = -1 и per_page = -6")
def sending_request_with_page_minus_1_and_per_page_minus_6(context):
    logger.info("run step 'sending_request_with_page_minus_1_and_per_page_minus_6':")  
    context['response_get_users'] = context['rest_api_methods'].get_users(-1, -6)
    logger.debug(f"get_users: {context['response_get_users']}")

@allure.step("Значение per_page равно -6")
@then("Значение per_page равно -6")
def per_page_value_is_minus_6(context):
    logger.info('run step \'per_page_value_is_minus_6\':') 
    logger.info(f'check that per_page values is -6:')
    try:
        logger.debug(f"context['response_get_users']['per_page']: {context['response_get_users']['per_page']}")
        assert context['response_get_users']['per_page'] == -6
        logger.info(f'ok')
    except AssertionError:
        logger.error(f'per_page value not equal -6')
        raise AssertionError(f'per_page value not equal -6') 


@allure.step("Отправляем запрос с начальными значениями page и per_page")
@when("Отправляем запрос с начальными значениями page и per_page")
def sending_request_with_defoult_values(context):
    logger.info("run step 'sending_request_with_defoult_values':")  
    context['response_get_users'] = context['rest_api_methods'].get_users()
    logger.debug(f"get_users: {context['response_get_users']}")


@allure.step("Запоминаем значение total из ответа")
@when("Запоминаем значение total из ответа")
def memorizing_total_value_from_response(context):
    logger.info("run step 'memorizing_total_value_from_response':")  
    context['response_get_users_total'] = context['response_get_users']['total']
    logger.debug(f"response_get_users_total: {context['response_get_users_total']}")  


@allure.step("Отправляем запрос с значениями page = 1 и per_page = total из предыдущего шага")
@when("Отправляем запрос с значениями page = 1 и per_page = total из предыдущего шага")
def sending_a_request_with_values_page_1_and_per_page_equal_total(context):
    logger.info("run step 'sending_request_with_defoult_values':")  
    context['response_get_users'] = context['rest_api_methods'].get_users(1, int(context['response_get_users_total']))
    logger.debug(f"get_users: {context['response_get_users']}")

@allure.step("Количество объетов совпадает с значением total")
@then("Количество объетов совпадает с значением total")
def number_of_objects_is_same_as_total_value(context):
    logger.info("run step 'number_of_objects_is_same_as_total_value':") 
    try:
        assert len(context['response_get_users']['data']) == context['response_get_users']['total']
        logger.info(f'ok')
    except AssertionError:
        logger.error(f'number of object not equal total value')
        raise AssertionError(f"number of object not equal total value")