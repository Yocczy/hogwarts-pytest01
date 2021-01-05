import pytest
import yaml
from python_code.calc import Calculator

with open('./datas/calc.yaml', encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    datas_add = datas['add']
    add_datas = datas_add['datas']
    add_myid = datas_add['myid']
    datas_div = datas['div']
    div_datas = datas_div['datas']
    div_myid = datas_div['myid']

class TestCalc:

    def setup_class(self):
        print('开始计算')
        # 实例化计算器类
        self.calc = Calculator()

    def teardown_class(self):
        print('计算结束')

    # 传入参数，python_code.calc替代
    # @pytest.mark.parametrize(
    #     "a, b, expect",
    #     [
    #         (1, 1, 2),
    #         (0.1, 0.1, 0.2),
    #         (-1, -1, -2),
    #         (0.1, 0.2, 0.3)
    #     ], ids=['int', 'float', 'negative', 'round']
    # )

    @pytest.mark.parametrize(
        "a, b, expect",
        add_datas, ids=add_myid
    )
    def test_add(self, a, b, expect):
        # 实例化计算器类
        # calc = Calculator()
        # 调用add方法
        result = self.calc.add(a, b)
        # 判断result是浮点数，作出保留2位小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果之后，需要写断言
        assert result == expect

    @pytest.mark.parametrize(
        "a, b, expect",
        div_datas, ids=div_myid
    )
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    # def test_add2(self):
    #     result = self.calc.add(0.1, 0.2)
    #     assert round(result, 2) == 0.3

    # def test_add1(self):
    #     calc = Calculator()
    #     result = self.calc.add(1, 1)
    #     assert result == 2