# -*- coding: utf-8 -*-
import io
import re
from setuptools import setup


with io.open("pylogs/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)


setup(
    name='pylogs',
    version=version,
    packages=['pylogs'],
    description="Custom log levels for Python's logging module.",
    url='https://github.com/ReiDoBrega/pylogs',
    keywords=['logging'],
    license='MIT'
)
