# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['code_census', 'code_census.alembic', 'code_census.alembic.versions']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy-Utils>=0.37.8,<0.38.0',
 'SQLAlchemy==1.4.0',
 'alembic>=1.6.5,<2.0.0',
 'beautifulsoup4>=4.9.3,<5.0.0',
 'click>=7.1.2',
 'lxml>=4.6.3,<5.0.0',
 'mypy>=0.910',
 'psycopg2>=2.9.1,<3.0.0',
 'rich>=10.7.0,<11.0.0']

entry_points = \
{'console_scripts': ['census = code_census.cli:cli',
                     'code_census = code_census.cli:cli']}

setup_kwargs = {
    'name': 'code-census',
    'version': '0.0.16',
    'description': 'A command line tool to collect, organize, report code metrics.',
    'long_description': '# census\n\nA CLI tool to track code metrics\n\n# Installation\n\n`pip install code_census`\n\n# Documentation\n\nThe project documentation is available at [https://kracekumar.github.io/code_census/](https://kracekumar.github.io/code_census/).\n',
    'author': 'Kracekumar',
    'author_email': 'me@kracekumar.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://kracekumar.github.io/code_census/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
