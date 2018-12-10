import time, sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data

test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,"*_test.py")

if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    filename = './report/result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Guest Manage System Interface Test Report',
                             description='Implementation Example with: ')
    runner.run(discover)
    fp.close()
