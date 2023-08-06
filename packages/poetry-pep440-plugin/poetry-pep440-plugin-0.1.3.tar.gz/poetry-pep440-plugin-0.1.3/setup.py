# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_pep440_plugin']

package_data = \
{'': ['*']}

install_requires = \
['poetry>=1.2.0a2,<2.0.0']

entry_points = \
{'poetry.application.plugin': ['poetry-pep440-plugin = '
                               'poetry_pep440_plugin.plugin:Pep440Plugin']}

setup_kwargs = {
    'name': 'poetry-pep440-plugin',
    'version': '0.1.3',
    'description': 'Loosens validation for PEP440 version constraints',
    'long_description': '# poetry-pep440-plugin\n\nThis is a simple Poetry plugin to monkeypatch a fix for https://github.com/python-poetry/poetry/issues/4176.\n',
    'author': 'Martin Liu',
    'author_email': 'martin.xs.liu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/martinxsliu/poetry_pep440_plugin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
