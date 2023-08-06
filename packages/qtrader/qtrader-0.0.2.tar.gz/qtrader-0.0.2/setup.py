# -*- coding: utf-8 -*-
# @Time    : 29/4/2020 11:04 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: setup.py
# @Software: PyCharm

"""
Either specify package data in setup.py or MANIFEST.in:
https://www.codenong.com/cs106808509/
"""

from setuptools import setup, find_packages

setup(
    name='qtrader',   # 包名称，之后如果上传到了pypi，则需要通过该名称下载
    version='0.0.2',  # version只能是数字，还有其他字符则会报错
    keywords=('setup', 'qtrader'),
    description='setup qtrader',
    long_description='',
    license='MIT',    # 遵循的协议
    install_requires=['sqlalchemy', 'pandas', 'numpy', 'pytz', 'clickhouse-driver', 'matplotlib', 'plotly'], # 这里面填写项目用到的第三方依赖
    author='josephchen',
    author_email='josephchenhk@gmail.com',
    include_package_data=True,
    packages=find_packages(), # 项目内所有自己编写的库
    # package_data={"": [
        # "*.ico",
        # "*.ini",
        # "*.dll",
        # "*.so",
        # "*.pyd",
    # ]},
    platforms='any',
    url='', # 项目链接,
    entry_points={
        'console_scripts':[
            'example=examples.demo_strategy:run'
        ]
    },
)