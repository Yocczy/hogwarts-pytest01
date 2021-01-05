import pytest
import yaml
from python_code.calc import Calculator


# 从conftest提取
# with open('./datas/calc.yaml', encoding='utf-8') as f:
#     datas = yaml.safe_load(f)
#     datas_add = datas['add']
#     add_datas = datas_add['datas']
#     add_myid = datas_add['myid']
#     datas_div = datas['div']
#     div_datas = datas_div['datas']
#     div_myid = datas_div['myid']
#
# @pytest.fixture(scope='class')
# def get_calc():
#     print('获取计算器实例')
#     calc = Calculator()
#     return calc
#
# @pytest.fixture(params=add_datas, ids=add_myid)
# def get_add_datas(request):
#     print('开始计算')
#     data = request.param
#     print(f'request.param 里面的测试数据是：{data}')
#     yield data
#     print('结束计算')
def test(test):
    pass


class TestCalc():

    @pytest.mark.run(order=0)
    def test_add(self, get_calc, get_add_datas):
        result = get_calc.add(get_add_datas[0], get_add_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_add_datas[2]

    @pytest.mark.run(order=3)
    def test_div(self, get_calc, get_div_datas):
        result = get_calc.div(get_div_datas[0], get_div_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_div_datas[2]

    @pytest.mark.run(order=1)
    def test_sub(self, get_calc, get_sub_datas):
        result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_sub_datas[2]

    @pytest.mark.run(order=2)
    def test_mul(self, get_calc, get_mul_datas):
        result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_mul_datas[2]
