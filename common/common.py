import logging
import os
import re
from logging.handlers import TimedRotatingFileHandler

from jsonpath import jsonpath

from common.path import LOG_DIR

file_path = os.path.join(LOG_DIR, 'logs')

def data_processing(data_json, var):
    # 对原始数据做进行特定值的搜索处理，data_json：原始数据。var：需要查找的数据key。返回对应key的value,list类型
    return jsonpath(data_json, '$..{}'.format(var))


def Logs():
    """日志"""
    # 创建logger对象，传入logger名字
    logger = logging.getLogger('logs')
    # 设置日志记录等级
    logger.setLevel("INFO")
    # 输入到流
    sh = logging.StreamHandler()
    # interval:滚动周期，when：表示每天0点更新，backupCount：保存几个日志文件
    file_handler = TimedRotatingFileHandler(filename=file_path, when='MIDNIGHT', interval=1, backupCount=7,
                                            encoding='utf-8')
    # 设置生成日志文件的格式
    file_handler.suffix = "%Y-%m-%d.logs"
    # extMatch是编译好的正则表达式，用于匹配日子文件的后缀名，需要注意的是suffix和extMatch一定要匹配的上
    file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.logs$")
    # 定义日志输出格式
    file_handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s] [%(process)d] [%(levelname)s] - %(module)s.%(funcName)s [%(filename)s-->line:%(lineno)d] - %(levelname)s:%(message)s"
        )
    )
    logger.addHandler(file_handler)
    logger.addHandler(sh)
    return logger



