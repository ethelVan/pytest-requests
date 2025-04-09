# api_auto_test
## 整体思路：
*将接口测试请求体及入参、预期结果、断言都放入excel里管理（后期可以直接从swagger里读取接口写进文件，修改更方便*
#### 1. 思路拆分
- 解析excel
- 发起请求
- 处理断言
- json提取

#### 2. 目录结构 
├── README.md   
├── data 
│   ├── api_cases.xlsx
├── logs                       
│   ├── test.log               
├── utils
│   ├── allure_utils 
│   ├── analyse_case
│   ├── asserts
│   ├── excel_utils
│   ├── extractor
│   └── send_req
├── conftest.py 
├── pytest.ini                 
├── requirements.txt           
├── testcases                  
│   └── test_runner.py 
└── run.py

3. todo
- 解析swagger
- 测试环境分离
- 支持grpc请求
- 异常处理
- 。。。
    
