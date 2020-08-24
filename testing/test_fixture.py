# -*- coding: UTF-8 -*-
import pytest

@pytest.fixture()
def login():
    print("登录!")
    username = 'Jerry'
    passname = '123456'
    # return [1,'qqqq']
    # yield python中的生成器 如果一个方法使用yield，那么这个方法就变成了生成器 能激活pytest的teardown操作，
    yield [username,passname]
    print("登出")

def test_case1(login):
    print(f"需要先登录再执行的测试用例")
    print(login)



def test_case2():
    print("不需要登录就可以执行的测试用例")

@pytest.mark.usefixtures('login')
def test_case3():
    print("需要先登录再执行的测试用例")
    print(login)


@pytest.mark.usefixtures('login')
def test_case4():
    print("需要先登录再执行的测试用例")
    print(login)