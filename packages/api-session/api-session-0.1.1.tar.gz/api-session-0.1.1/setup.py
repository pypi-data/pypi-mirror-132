# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['api_session']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'api-session',
    'version': '0.1.1',
    'description': 'requests.Session to work with (JSON) APIs',
    'long_description': None,
    'author': 'Baptiste Fontaine',
    'author_email': 'baptiste@bixoto.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
