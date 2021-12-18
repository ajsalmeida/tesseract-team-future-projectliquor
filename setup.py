
from setuptools import setup

packages = \
['iowalicor', 'iowalicor.data', 'iowalicor.deployment', 'iowalicor.model']

package_data = \
{'': ['*']}

install_requires = \
['Levenshtein>=0.16.0,<0.17.0',
 'dask>=2021.10.0,<2022.0.0',
 'invoke>=1.6.0,<2.0.0',
 'jupyterlab>=3.2.0,<4.0.0',
 'kaggle>=1.5.12,<2.0.0',
 'matplotlib>=3.4.3,<4.0.0',
 'pandas>=1.3.3,<2.0.0',
 'scikit-learn>=1.0.1,<2.0.0']

setup_kwargs = {
    'name': 'iowalicor',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'andrerodrig',
    'author_email': 'andrelmarques11@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

