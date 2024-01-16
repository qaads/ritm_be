import os
import requests
from loguru import logger
from dotenv import load_dotenv

load_dotenv()

class REST_API_Methods():
    
    def post(self, method: str, params: dict = None):
        logger.info(f"run request.post func:")
        logger.debug(f"json = {params}")
        requests.post(f"{os.getenv('URL')}/{method}", json=params)
    
    def get(self, method: str, params_: dict):
        logger.debug(f"run request.get func:")
        logger.debug(f"try to send get '{method}' method:")
        response = requests.get(f"{os.getenv('URL')}/{method}", params=params_)
        logger.debug(f"response has been recieved: {response}")
        logger.info(f"check that status code = 200:")
        try:
            logger.debug(f"status_code: {response.status_code}")
            assert response.status_code == 200
            return response.json()
        except AssertionError as e:
            logger.error(f"response.status_code: {response.status_code}")
            raise e(f"response.status_code: {response.status_code}")
    
    # По результатам ручного тестирования складывается впечатление что 1 и 6 - значения по умолчанию
    def get_users(self, page: int = 1, per_page: int = 6):
        logger.debug(f"run func: get_users:")
        params = {
            "page": page,
            "per_page": per_page
        }
        return self.get("users", params)

    
    