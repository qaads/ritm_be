from pytest_bdd import scenario
import pytest
import allure
from steps.get_users_steps import *


@pytest.mark.positive
@pytest.mark.smoke
@allure.title(f'Заполнить оба параметра (Валидные значения)')
@scenario(
    '../scenarios/get_users.feature',
    'Заполнить оба параметра (Валидные значения)'
)
def test_1():
    pass

@pytest.mark.negative
@allure.title(f'Заполнить оба параметра (Невалидные значения: отрицательные)')
@scenario(
    '../scenarios/get_users.feature',
    'Заполнить оба параметра (Невалидные значения: отрицательные)'
)
def test_2():
    pass

@pytest.mark.positive
@allure.title(f'total отражает реальное количество')
@scenario(
    '../scenarios/get_users.feature',
    'total отражает реальное количество'
)
def test_3():
    pass