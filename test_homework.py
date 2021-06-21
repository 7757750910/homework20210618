'''
1.改造 计算器 测试用例，使用 fixture 函数获取计算器的实例
2.计算之前打印开始计算，计算之后打印结束计算
3.添加用例日志，并将日志保存到日志文件目录下
4.生成测试报告，展示测试用例的标题，用例步骤，与测试日志，截图附到课程贴下
'''
import logging
import allure
import pytest
import yaml


# 被测方法
def add(a, b):
    return a + b


def div(c, d):
    return c / d


# 测试加法
@allure.story('测试加法')
@allure.title('正常数据测试加法')
@pytest.mark.parametrize(['a', 'b', 'expect'], yaml.safe_load(open("./add.yaml")))
def test_add1(a, b, expect, setdown):
    logging.info(f'源数据 {a}')
    logging.info(f'源数据 {b}')
    assert expect == a + b


# 小数相加时的特殊情况
@allure.story('测试加法异常')
@allure.title('特殊数据测试加法')
@pytest.mark.parametrize('a,b,expect', [(0.1, 0.2, 0.3)])
def test_add2(a, b, expect, setdown):
    logging.info(f'源数据 {a}')
    logging.info(f'源数据 {b}')
    assert expect == round((a + b), 2)


# 测试除法
@allure.story('测试除法')
@allure.title('正常测试除法异常')
@pytest.mark.parametrize(['c', 'd', 'expect'], yaml.safe_load((open("./div.yml."))))
@pytest.mark.div
def test_div1(c, d, expect, setdown):
    logging.info(f'源数据 {c}')
    logging.info(f'源数据 {d}')
    assert expect == c / d


# 除数为0时
@allure.story('测试除法异常')
@allure.title('特殊数据测试除法异常')
@pytest.mark.parametrize('c,d', [(1, 0)])
def test_div2(c, d, setdown):
    logging.info(f'源数据 {c}')
    logging.info(f'源数据 {d}')
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


def test_attach_photo():
    allure.attach.file("D:\霍格沃兹/kobe.jpg",
                       name='这是一个图片', attachment_type=allure.attachment_type.JPG)
