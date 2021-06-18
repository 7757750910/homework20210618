'''1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
'''
import pytest
import yaml

#被测方法
def add(self,a,b):
    return a+b
def div(self,c,d):
    return c/d
#测试方法
class TestAdd:
    def setup_class(self):
        print('开始加法测试')
    def teardown_class(self):
        print('加法测试结束')
    def setup(self):
        print('开始执行用例')
    def teardown(self):
        print('结束用例执行')

    @pytest.mark.parametrize(['a', 'b', 'expect'], yaml.safe_load((open("./add.yaml"))))
    @pytest.mark.add
    def test_add1(self,a,b,expect):
        assert expect == a+b

class TestDiv:
    def setup_class(self):
        print('开始除法测试')
    def teardown_class(self):
        print('除法测试结束')
    def setup(self):
        print('开始执行用例')
    def teardown(self):
        print('结束用例执行')

    @pytest.mark.parametrize(['c', 'd', 'expect'], yaml.safe_load((open("./div.yml."))))
    @pytest.mark.div
    def test_div1(self, c, d, expect):
        assert expect == c/d


'''
加法中存在字母、特殊字符、数字类的混合相加，可是断言这块怎么添加判断呢，
eg:1+a = ? 这个断言该怎么写，assert error?,还是断言就不支持，
这块没研究出来该咋写，用例中只会写一些常规的。
除法中除数是0的时候，也是不会写断言这部分
还有结果是无限循环小数的时候，断言该怎么写
'''




