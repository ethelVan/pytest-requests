import os
# 测试地址

BASE_URL = "http://127.0.0.1:8888/api/private/v1"

# excel格式的测试用例文件配置
Base_Dir = os.path.dirname(os.path.abspath(__file__))
EXCEL_FILE = Base_Dir + "/data/api_cases.xlsx"
SHEET_NAME = "Sheet1"

# mysql配置
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_NAME = "shop"
DB_USER = "root"
DB_PASSWORD = "bababa"

# 测试数据删除
SQL1 = 'delete from sp_category where cat_name = "大码服装"'
SQL2 = 'delete from sp_attribute where attr_name = "VIP尺码"'
SQL3 = 'delete from sp_goods where goods_name = "大码牛仔裤+"'

