import pytest


# @pytest.fixture(autouse=True, scope='function, class, module, session')
@pytest.fixture(scope='function')
def login():
    print('登陆操作')
    username = 'aaa'
    password = '123456'
    token = 'token123456'
    yield [username, password, token]
    print('登出操作')


def test_case1(login):
    print(f'login information:{login}')
    print('测试用例1')


def test_case2(connectDB):
    print('测试用例2')


@pytest.mark.usefixtures('login')
def test_case3():
    print('测试用例3')
