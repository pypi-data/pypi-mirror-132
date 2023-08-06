# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycvcqv']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.21.1,<2.0.0', 'pandas>=1.3.3,<2.0.0']

setup_kwargs = {
    'name': 'pycvcqv',
    'version': '0.1.10',
    'description': 'Coefficient of Variation (CV) and Coefficient of Quartile Variation (CQV) with Confidence Intervals (CI) ',
    'long_description': '# pycvcqv\n\n<div align="center">\n\n[![PyPI](https://img.shields.io/pypi/v/pycvcqv)](https://pypi.org/project/pycvcqv/)\n[![Python Version](https://img.shields.io/pypi/pyversions/pycvcqv.svg)](https://pypi.org/project/pycvcqv/)\n[![Build status](https://github.com/MaaniBeigy/pycvcqv/workflows/build/badge.svg)](https://github.com/MaaniBeigy/pycvcqv/actions?query=workflow%3Abuild)\n[![coverage report](https://raw.githubusercontent.com/MaaniBeigy/pycvcqv/main/assets/images/coverage.svg)](https://raw.githubusercontent.com/MaaniBeigy/pycvcqv/main/.logs/coverage.txt)\n[![static analysis](https://raw.githubusercontent.com/MaaniBeigy/pycvcqv/main/assets/images/mypy.svg)](https://raw.githubusercontent.com/MaaniBeigy/pycvcqv/main/.logs/mypy.txt)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/MaaniBeigy/pycvcqv/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n[![maintainability](https://raw.githubusercontent.com/MaaniBeigy/pycvcqv/main/assets/images/maintainability.svg)](https://raw.githubusercontent.com/MaaniBeigy/pycvcqv/main/.logs/maintainability.txt)\n[![complexity](https://raw.githubusercontent.com/MaaniBeigy/pycvcqv/main/assets/images/complexity.svg)](https://raw.githubusercontent.com/MaaniBeigy/pycvcqv/main/.logs/complexity.txt)\n[![Safety Vulnerabilities](https://raw.githubusercontent.com/MaaniBeigy/pycvcqv/main/assets/images/vulnerabilities.svg)](https://raw.githubusercontent.com/MaaniBeigy/pycvcqv/main/.logs/safety.txt)\n[![docstring coverage](https://raw.githubusercontent.com/MaaniBeigy/pycvcqv/main/assets/images/interrogate_badge.svg)](https://raw.githubusercontent.com/MaaniBeigy/pycvcqv/main/.logs/docstring.txt)\n[![lint report](https://raw.githubusercontent.com/MaaniBeigy/pycvcqv/main/assets/images/pylint.svg)](https://raw.githubusercontent.com/MaaniBeigy/pycvcqv/main/.logs/pylint-log.txt)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/MaaniBeigy/pycvcqv/blob/master/.pre-commit-config.yaml)\n[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/MaaniBeigy/pycvcqv/releases)\n[![License](https://img.shields.io/github/license/MaaniBeigy/pycvcqv)](https://github.com/MaaniBeigy/pycvcqv/blob/master/LICENSE)\n[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FMaaniBeigy%2Fpycvcqv.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FMaaniBeigy%2Fpycvcqv?ref=badge_shield)\n\nCoefficient of Variation (CV) and Coefficient of Quartile Variation (CQV) with Confidence Intervals (CI)\n\nPython port of [cvcqv](https://github.com/MaaniBeigy/cvcqv)\n\n</div>\n\n## Introduction\n\n`pycvcqv` provides some easy-to-use functions to calculate the\nCoefficient of  Variation (`cv`) and Coefficient of Quartile Variation (`cqv`)\nwith confidence intervals provided with all available methods.\n\n## Install\n\n```bash\npip install pycvcqv\n```\n\n## Usage\n\n```python\nimport pandas as pd\nfrom pycvcqv import coefficient_of_variation, cqv\n\ncoefficient_of_variation(\n    data=[0.2, 0.5, 1.1, 1.4, 1.8, 2.3, 2.5, 2.7, 3.5, 4.4, 4.6, 5.4, 5.4],\n    multiplier=100,\n)\n# 64.6467\ncqv(\n    data=[0.2, 0.5, 1.1, 1.4, 1.8, 2.3, 2.5, 2.7, 3.5, 4.4, 4.6, 5.4, 5.4],\n    multiplier=100,\n)\n# 51.7241\ndata = pd.DataFrame(\n    {\n        "col-1": pd.Series([0.2, 0.5, 1.1, 1.4, 1.8, 2.3, 2.5, 2.7, 3.5]),\n        "col-2": pd.Series([5.4, 5.4, 5.7, 5.8, 5.9, 6.0, 6.6, 7.1, 7.9]),\n    }\n)\ncoefficient_of_variation(data=data, num_threads=3)\n#   columns      cv\n# 0   col-1  0.6076\n# 1   col-2  0.1359\ncqv(data=data, num_threads=-1)\n#   columns      cqv\n# 0   col-1  0.3889\n# 1   col-2  0.0732\n```\n\n## For contributors:\n\n### Testing:\n\n```bash\nmake install\nmake pre-commit-install\nmake test && make coverage && make check-codestyle && make mypy && make check-safety && make extrabadges\n```\n\n### Upload code to GitHub:\n\n```bash\npre-commit run --all-files\ngit add .\ngit commit -m ":tada: Initial commit"\ngit push -u origin main\n```\n\n\n## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)\n[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FMaaniBeigy%2Fpycvcqv.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FMaaniBeigy%2Fpycvcqv?ref=badge_shield)\n\nThis project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)\n\n\n## License\n[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FMaaniBeigy%2Fpycvcqv.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FMaaniBeigy%2Fpycvcqv?ref=badge_large)\n',
    'author': 'MaaniBeigy',
    'author_email': 'manibeygi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MaaniBeigy/pycvcqv',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0',
}


setup(**setup_kwargs)
