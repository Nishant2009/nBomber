from setuptools import setup

setup(name="bomber",
version="1.0",
description="SMS BOMBER with 50000 sms limit",
author="Nishant",
url='https://github.com/Nishant2009/Bomber/',
scripts=['bomber'],
install_requires=['certifi>=2020.6.20','chardet>=3.0.4','colorama>=0.4.3','idna>=2.10','requests>=2.24.0','phonenumbers>=8.12.48']
)