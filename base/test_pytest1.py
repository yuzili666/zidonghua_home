import allure

@allure.feature('测试报告二')
class Test_py:

    @allure.story('测试小功能5')
    def test_demo1(self):
        a = 1
        b = 1
        assert a == b

    @allure.story('测试小功能6')
    def test_demo2(self):
        a = 1
        b = 1
        assert a == b

    @allure.story('测试小功能7')
    def test_demo3(self):
        a = 1
        b = 1
        assert a == b

    @allure.story('测试小功能8')
    def test_demo4(self):
        a = 1
        b = 1
        assert a == b

