# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vkbottle',
 'vkbottle.api',
 'vkbottle.api.request_rescheduler',
 'vkbottle.api.request_validator',
 'vkbottle.api.response_validator',
 'vkbottle.api.token_generator',
 'vkbottle.dispatch',
 'vkbottle.dispatch.dispenser',
 'vkbottle.dispatch.handlers',
 'vkbottle.dispatch.middlewares',
 'vkbottle.dispatch.return_manager',
 'vkbottle.dispatch.return_manager.bot',
 'vkbottle.dispatch.rules',
 'vkbottle.dispatch.views',
 'vkbottle.dispatch.views.bot',
 'vkbottle.exception_factory',
 'vkbottle.exception_factory.error_handler',
 'vkbottle.exception_factory.swear_handler',
 'vkbottle.framework',
 'vkbottle.framework.bot',
 'vkbottle.framework.bot.labeler',
 'vkbottle.http',
 'vkbottle.http.client',
 'vkbottle.http.middleware',
 'vkbottle.http.session_manager',
 'vkbottle.polling',
 'vkbottle.tools',
 'vkbottle.tools.dev_tools',
 'vkbottle.tools.dev_tools.auth',
 'vkbottle.tools.dev_tools.auth._flows',
 'vkbottle.tools.dev_tools.keyboard',
 'vkbottle.tools.dev_tools.mini_types',
 'vkbottle.tools.dev_tools.mini_types.bot',
 'vkbottle.tools.dev_tools.storage',
 'vkbottle.tools.dev_tools.template',
 'vkbottle.tools.dev_tools.uploader',
 'vkbottle.tools.dev_tools.vkscript_converter',
 'vkbottle.tools.production_tools',
 'vkbottle.tools.production_tools.legacies']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.2,<4.0.0',
 'choicelib>=0.1.1,<0.2.0',
 'vbml>=1.0,<2.0',
 'vkbottle-types==5.131.131.2',
 'watchgod>=0.7,<0.8']

setup_kwargs = {
    'name': 'vkbottle',
    'version': '3.0.3',
    'description': 'Homogenic! Customizable asynchronous VK API framework implementing comfort and speed',
    'long_description': '<p align="center">\n  <a href="https://github.com/timoniq/vkbottle">\n    <img src="https://raw.githubusercontent.com/timoniq/vkbottle/master/docs/logo.jpg" width="200px" style="display: inline-block; border-radius: 5px">\n  </a>\n</p>\n<h1 align="center">\n  VKBottle 3.x\n</h1>\n<p align="center">\n  <img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/timoniq/vkbottle/CI?style=flat-square">\n  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/timoniq/vkbottle?style=flat-square">\n  <img alt="GitHub issues by-label" src="https://img.shields.io/github/issues/timoniq/vkbottle/bug?style=flat-square">\n  <img alt="PyPI" src="https://img.shields.io/pypi/v/vkbottle?color=green&label=PyPI&style=flat-square">\n</p>\n\n> Кастомизируемый, быстрый и удобный фреймворк для работы с VK API\n\n## Документация\n\n[Туториал для новичков](https://github.com/timoniq/vkbottle/blob/master/docs/tutorial/index.md)\\\n[Техническая документация](https://vkbottle.readthedocs.io/ru/latest)\n\n## Установка\n\nУстановить новейшую версию можно командой:\n\n```shell script\npip install -U https://github.com/timoniq/vkbottle/archive/v3.0.zip\n```\n\nУстановить версию 3.0 с PyPI можно командой:\n\n```shell\npip install vkbottle\n```\n\nЕсли вы ищете старые версии (`2.x`) - [вам сюда](https://github.com/timoniq/vkbottle/tree/v2.0)\n\n## Hello World\n\n[Смотреть больше примеров!](https://github.com/timoniq/vkbottle/tree/master/examples)\\\n[Почему VKBottle?](https://github.com/timoniq/vkbottle/blob/master/docs/why_vkbottle.md)\n\n```python\nfrom vkbottle.bot import Bot\n\nbot = Bot("GroupToken")\n\n@bot.on.message()\nasync def handler(_) -> str:\n    return "Hello world!"\n\nbot.run_forever()\n```\n\n## Contributing\n\nПР поддерживаются! Перед созданием пулл реквеста ознакомьтесь с [CONTRIBUTION_GUIDE.md](CONTRIBUTION_GUIDE.md). Нам приятно видеть ваш вклад в развитие библиотеки. Задавайте вопросы в блоке Issues и в [**чате Telegram**](https://t.me/vkbottle_ru) / [**чате VK**](https://vk.me/join/AJQ1d7fBUBM_800lhEe_AwJj)!\n\n## Лицензия\n\nCopyright © 2019-2021 [timoniq](https://github.com/timoniq).\\\nЭтот проект имеет [MIT](./LICENSE) лицензию.\n',
    'author': 'timoniq',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/timoniq/vkbottle',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
