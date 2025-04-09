import allure


def allure_init(case):
    allure.dynamic.feature(case["feature"])
    allure.dynamic.feature(case["story"])
    allure.dynamic.title(f"ID:{case["id"]} -- {case["title"]}")




