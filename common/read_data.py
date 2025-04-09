import json
import os


class ReadJson:

    def __init__(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as fp:
            self.json_data = json.load(fp)

    def read_json(self, data_name):
        """读取json文件"""
        return self.json_data[data_name]
