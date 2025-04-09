import os

# 获取当前文件的目录
DIR = os.getcwd()

# 获取项目目录的路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 获取测试用例的目录路径
CASE_DIR = os.path.join(BASE_DIR, 'testcases')

# 获取测试报告的目录路径
REPOST_DIR = os.path.join(BASE_DIR, 'reports')

# 获取日志文件的目录路径
LOG_DIR = os.path.join(BASE_DIR, 'logs')


# 获取用例数据文件的目录路径
DATA_DIR = os.path.join(BASE_DIR, 'data')
