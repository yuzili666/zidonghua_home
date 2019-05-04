import allure

@allure.feature('测试报告一')
class Test_py:

    @allure.story('测试小功能1')
    def test_demo1(self):
        a = 1
        b = 1
        assert a == b

    @allure.story('测试小功能2')
    def test_demo2(self):
        a = 1
        b = 1
        assert a == b

    @allure.story('测试小功能3')
    def test_demo3(self):
        a = 1
        b = 1
        assert a == b

    @allure.story('测试小功能4')
    def test_demo4(self):
        a = 1
        b = 1
        assert a == b

