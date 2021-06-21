# 计算之前打印开始计算，计算之后打印结束计算
import pytest


@pytest.fixture()
def setdown():
    print('开始计算')
    yield
    print('结束计算')