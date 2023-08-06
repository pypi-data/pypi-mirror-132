# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['libtictactoe', 'libtictactoe.cursesUI', 'libtictactoe.logic']

package_data = \
{'': ['*']}

install_requires = \
['certifi==2021.10.8', 'pip==21.2.4', 'setuptools==58.0.4', 'wheel==0.37.0']

setup_kwargs = {
    'name': 'libtictactoe',
    'version': '0.1.7',
    'description': 'Tic Tac Toe game made with Python and Curses',
    'long_description': None,
    'author': 'Marlene Nunes',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.10,<4.0.0',
}


setup(**setup_kwargs)
