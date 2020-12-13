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
        self.calc = Calculator()

    def teardown_class(self):
        print('计算结束')

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
        # calc = Calculator()
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
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
    #
    # def test_add2(self):
    #     calc = Calculator()
    #     result = self.calc.add(1, 1)
    #     assert result == 2
