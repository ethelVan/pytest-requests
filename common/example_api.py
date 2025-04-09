import os
import util
from common.common import Logs
from common.path import DATA_DIR
from common.read_data import ReadJson

logs = Logs()

read_json = ReadJson(os.path.join(DATA_DIR, "querydatas.json"))
read_case = ReadJson(os.path.join(DATA_DIR, "casedatas.json"))


def example_api(name, api_url, num=0, headers=None, param_string=None, error=False, token=False, data=None, **kwargs):
    # 判断是否启动错误用例，默认关闭
    if error:
        name_error = name.lower()
    else:
        name_error = name
    # 读取对应的用例参数
    case_data = read_case.read_json(name_error)[num]
    # 上下文接口关联参数，并生成新的测试数据
    if param_string is None:
        case_data = case_data
    else:
        case_data.update(param_string)
    # 判断是否开启调试模式，默认关闭
    if token:
        token = example_api(name="getToken")['data']['getToken']['token']
    else:  # 不开启调试模式，直接从外部获取token
        token = headers
    headers = {"authorization": token}
    # 最终下发的参数
    json = {"operationName": name, "variables": case_data, "query": read_json.read_json(name)}
    logs.info(
        'json入参数据：{}，data入参数据：{}，关联参数数据：{}，其他参数数据：{}'.format(case_data, data, param_string, kwargs))
    return util.post(url=api_url, json=json, headers=headers, data=data, **kwargs).json()
