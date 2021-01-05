import pytest
import yaml
import os
from python_code.calc import Calculator


@pytest.fixture(scope='session')
def connectDB():
    print('连接数据库操作')
    yield
    print('断开数据库连接')


# 获取yaml文件所在的绝对路径
yaml_file_path = os.path.dirname(__file__) + '/datas/calc.yaml'

with open(yaml_file_path, encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    datas_add = datas['add']
    add_datas = datas_add['datas']
    add_myid = datas_add['myid']
    datas_div = datas['div']
    div_datas = datas_div['datas']
    div_myid = datas_div['myid']

    datas_sub = datas['sub']
    sub_datas = datas_sub['datas']
    sub_myid = datas_sub['myid']
    datas_mul = datas['mul']
    mul_datas = datas_mul['datas']
    mul_myid = datas_mul['myid']


@pytest.fixture(scope='class')
def get_calc():
    print('获取计算器实例')
    calc = Calculator()
    return calc


@pytest.fixture(params=add_datas, ids=add_myid)
def get_add_datas(request):
    print('开始计算加法')
    data = request.param
    print(f'request.param 里面的测试数据是：{data}')
    yield data
    print('结束加法计算')


@pytest.fixture(params=div_datas, ids=div_myid)
def get_div_datas(request):
    print('开始计算除法')
    data = request.param
    print(f'request.param 里面的测试数据是：{data}')
    yield data
    print('结束除法计算')


@pytest.fixture(params=sub_datas, ids=sub_myid)
def get_sub_datas(request):
    print("开始计算减法")
    datas = request.param
    print(f"request.param 里面的数据是：{datas}")
    yield datas
    print("结束减法计算")


@pytest.fixture(params=mul_datas, ids=mul_myid)
def get_mul_datas(request):
    print("开始计算乘法")
    datas = request.param
    print(f"request.param 里面的数据是：{datas}")
    yield datas
    print("结束乘法计算")


@pytest.fixture(scope='module')
def test():
    print('开始计算')
    yield
    print('结束计算')
