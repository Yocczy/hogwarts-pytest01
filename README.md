# 介绍
霍格沃兹测试训练营python第三次课堂和作业记录

pytest

###内容
####第一次  
1.课堂练习：Calculator 计算器测试

2.课后作业：Calculator 计算器测试补全

补全计算器中加法和除法的测试用例  
使用参数化完成测试用例的自动生成  
在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】

注意：
使用等价类，边界值，因果图等设计测试用例  
测试用例中添加断言，验证结果  
灵活使用 setup(), teardown() , setup_class(), teardown_class()

__位置：testing/test_calc.py__

####第二次  
1.课堂练习：  
fixture方法  
conftest.py用法  
pytest配置文件  
pytest插件  
allure生成测试报告  
pytest hook 函数  

2.课后作业：  
    补全计算器（加减乘除）的测试用例  
    使用数据的数据驱动，完成加减乘除用例的自动生成  
    创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】  
    控制测试用例顺序按照【加-减-乘-除】这个顺序执行  
    结合allure 生成测试结果报告

__位置：testing/test_calc_fixture.py__
