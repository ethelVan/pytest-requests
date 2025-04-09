import pytest

from common.example_api import example_api
from common.common import Logs

logs = Logs()

logs
@pytest.fixture(scope="session")
def api_url():
    return "https://example.com/graphql"


@pytest.fixture(scope="session")
def login_token():
    all_login_token = example_api(name="getToken")['data']['getToken']['token']
    logs.info("全局的token：{}".format(login_token))
    return all_login_token
