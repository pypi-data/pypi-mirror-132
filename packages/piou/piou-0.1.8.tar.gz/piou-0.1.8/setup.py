# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['piou', 'piou.formatter']

package_data = \
{'': ['*']}

install_requires = \
['rich>=10.11.0,<11.0.0']

setup_kwargs = {
    'name': 'piou',
    'version': '0.1.8',
    'description': 'A CLI tool',
    'long_description': '# Piou  \n\n[![Python versions](https://img.shields.io/pypi/pyversions/piou)](https://pypi.python.org/pypi/piou)\n[![Latest PyPI version](https://img.shields.io/pypi/v/piou?logo=pypi)](https://pypi.python.org/pypi/piou)\n[![CircleCI](https://circleci.com/gh/Andarius/piou/tree/master.svg?style=shield)](https://app.circleci.com/pipelines/github/Andarius/piou?branch=master)\n[![Latest conda-forge version](https://img.shields.io/conda/vn/conda-forge/piou?logo=conda-forge)](https://anaconda.org/conda-forge/piou)  \n\nA CLI tool to build beautiful command-line interfaces with type validation.\n\nIt is as simple as\n\n```python\nfrom piou import Cli, Option\n\ncli = Cli(description=\'A CLI tool\')\n\n\n@cli.command(cmd=\'foo\',\n             help=\'Run foo command\')\ndef foo_main(\n    foo1: int = Option(..., help=\'Foo arguments\'),\n    foo2: str = Option(..., \'-f\', \'--foo2\', help=\'Foo2 arguments\'),\n    foo3: str = Option(None, \'-g\', \'--foo3\', help=\'Foo3 arguments\'),\n):\n    pass\n\nif __name__ == \'__main__\':\n    cli.run()\n```\nThe output will look like this: \n\n![example](https://github.com/Andarius/piou/raw/master/docs/simple-output.png)\n\n\n# Install\n\nYou can install `piou` with either:\n - `pip install piou`\n - `conda install piou -c conda-forge`\n\n# Features  \n\n## Commands  \n\n```python\nfrom piou import Cli, Option\n\ncli = Cli(description=\'A CLI tool\')\n\n\n@cli.command(cmd=\'foo\',\n             help=\'Run foo command\')\ndef foo_main(\n    foo1: int = Option(..., help=\'Foo arguments\'),\n    foo2: str = Option(..., \'-f\', \'--foo2\', help=\'Foo2 arguments\'),\n    foo3: str = Option(None, \'-g\', \'--foo3\', help=\'Foo3 arguments\'),\n):\n    pass\n\n@cli.command(cmd=\'bar\',\n             help=\'Run foo command\')\ndef bar_main(\n    foo1: int = Option(..., help=\'Foo arguments\'),\n    foo2: str = Option(..., \'-f\', \'--foo2\', help=\'Foo2 arguments\'),\n    foo3: str = Option(None, \'-g\', \'--foo3\', help=\'Foo3 arguments\'),\n):\n    pass\n\nif __name__ == \'__main__\':\n    cli.run()\n```  \n\n\nIn this case, `foo1` is a positional argument while `foo2` and `foo3` are keyword arguments.\n\nYou can optionally specify global options that will be passed to all commands: \n\n```python\ncli = Cli(description=\'A CLI tool\')\n\ncli.add_option(None, \'-q\', \'--quiet\', help=\'Do not output any message\')\n```\n\nThe **help** can also be extracted from the function docstring, both functions here have\nthe same one.\n\n```python\n@cli.command(cmd=\'bar\', help=\'Run foo command\')\ndef bar_main():\n    pass\n\n@cli.command(cmd=\'bar2\')\ndef bar_2_main():\n    """\n    Run foo command\n    """\n    pass\n```\n\n\n\n\n## Sub-commands\n\nYou can group commands into sub-commands:\n\n```python\nfrom piou import Cli, Option\n\ncli = Cli(description=\'A CLI tool\')\n\nsub_cmd = cli.add_sub_parser(cmd=\'sub\', description=\'A sub command\')\n\nsub_cmd.add_option(False, \'-\', \'--dry-run\', help=\'Run in dry run mode\')\n\n\n@sub_cmd.command(cmd=\'foo\', help=\'Run baz command\')\ndef baz_bar_main(**kwargs):\n    pass\n\n\n@sub_cmd.command(cmd=\'bar\', help=\'Run toto command\')\ndef toto_main(\n        foo1: int = Option(..., help=\'Foo arguments\'),\n        foo2: str = Option(..., \'-f\', \'--foo2\', help=\'Foo2 arguments\'),\n):\n    pass\n\n\nif __name__ == \'__main__\':\n    cli.run()\n\n```\n\n![example](https://github.com/Andarius/piou/raw/master/docs/sub-cmd-output.png)\n\n\n## Complete example\n\nHere is a more complete example that you can try  by running `python -m piou.test` \n\n```python\nfrom piou import Cli, Option\n\ncli = Cli(description=\'A CLI tool\')\n\ncli.add_option(None, \'-q\', \'--quiet\', help=\'Do not output any message\')\ncli.add_option(None, \'--verbose\', help=\'Increase verbosity\')\n\n\n@cli.command(cmd=\'foo\',\n             help=\'Run foo command\')\ndef foo_main(\n        quiet: bool,\n        verbose: bool,\n        foo1: int = Option(..., help=\'Foo arguments\'),\n        foo2: str = Option(..., \'-f\', \'--foo2\', help=\'Foo2 arguments\'),\n        foo3: str = Option(None, \'-g\', \'--foo3\', help=\'Foo3 arguments\'),\n):\n    pass\n\n\n@cli.command(cmd=\'bar\', help=\'Run bar command\')\ndef bar_main(**kwargs):\n    pass\n\n\nsub_cmd = cli.add_sub_parser(cmd=\'sub\', description=\'A sub command\')\nsub_cmd.add_option(None, \'--test\', help=\'Test mode\')\n\n\n@sub_cmd.command(cmd=\'bar\', help=\'Run baz command\')\ndef baz_bar_main(\n        **kwargs\n):\n    pass\n\n\n@sub_cmd.command(cmd=\'toto\', help=\'Run toto command\')\ndef toto_main(\n        test: bool,\n        quiet: bool,\n        verbose: bool,\n        foo1: int = Option(..., help=\'Foo arguments\'),\n        foo2: str = Option(..., \'-f\', \'--foo2\', help=\'Foo2 arguments\'),\n):\n    pass\n\n\nif __name__ == \'__main__\':\n    cli.run()\n```\n',
    'author': 'Julien Brayere',
    'author_email': 'julien.brayere@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/andarius/pioupiou',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
