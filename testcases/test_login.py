#!/usr/bin/evn Python
# -*-coding:utf-8 -*-

import pytest
import allure
from common.example_api import example_api
from common.common import Logs

logs = Logs()


class TestLogin_01:
    @allure.feature('登录成功用例01')
    @pytest.mark.parametrize("case_data", [0, 1])
    def test_01(self,api_url,case_data):
        # 下发参数
        succeed_api = example_api(name="getToken", api_url=api_url, num=case_data)
        logs.info('返回数据：{}'.format(succeed_api))
        try:
            assert succeed_api['data']['getToken']['token'] is not None
        except AssertionError as e:
            logs.info("断言失败信息：{}".format(e))

    @allure.feature('登录失败用例01')
    @pytest.mark.parametrize("case_data", [0])
    def test_02(self, api_url,case_data):
        # 下发参数
        error_api = example_api(name="getToken", api_url=api_url, num=case_data, error=True)
        logs.info('返回数据：{}'.format(error_api))
        try:
            assert error_api['errors'][0]["message"] is not None
            logs.info('error_api：{}'.format((error_api['errors'][0]["message"])))
        except AssertionError as e:
            logs.info("断言失败信息：{}".format(e))
