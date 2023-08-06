# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aggexif']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['aggexif = aggexif.main:main',
                     'sqlite = aggexif.sqlite_cache:main']}

setup_kwargs = {
    'name': 'aggexif',
    'version': '0.4.1',
    'description': "Aggregate Image's EXIF Tool",
    'long_description': '## Required\n- python 3.8 later & pip\n- exiftool\n\n## Install\n```\n# pip install aggexif\n```\n\n## Usage\nBasic usage.\n\n```\n$ aggexif ~/dir/*.NEF\n---- CAMERA LIST ----\nNIKON Z 7: 276▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\nNIKON Z 6: 69▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n---- LENS LIST ----\nAF-S VR Zoom-Nikkor 70-300mm f/4.5-5.6G IF-ED: 213▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n                       NIKKOR Z 14-30mm f/4 S: 69▇▇▇▇▇▇▇▇\n                        NIKKOR Z 50mm f/1.8 S: 48▇▇▇▇▇\n       AF-S Zoom-Nikkor 80-200mm f/2.8D IF-ED: 13\n---- FOCAL LENGTH ----\n  10-15: 19▇▇▇▇▇▇▇▇▇▇▇\n  15-20: 7▇▇▇\n  20-24: 9▇▇▇▇▇\n  28-35: 34▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n  45-50: 48▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n  60-70: 54▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n  70-85: 30▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n 85-105: 13▇▇▇▇▇▇▇\n105-135: 11▇▇▇▇▇\n135-200: 18▇▇▇▇▇▇▇▇▇▇\n200-300: 100▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n---- YEAR ----\n2021: 345▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n```\n\nUse stdin pipe, -a(use cache), -w(print width), -l(filter lens), --monthly(view monthly graph) and --year(filter year).\n\n```\nfind ~/picture/ -name "*.NEF" | poetry run aggexif -a -w=100 -l="14-30" --monthly --year=2021\n---- CAMERA LIST ----\nNIKON Z 6: 4441▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\nNIKON Z 7: 1183▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n---- LENS LIST ----\nNIKKOR Z 14-30mm f/4 S: 5624▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n---- FOCAL LENGTH ----\n10-15: 1301▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n15-20: 946▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n20-24: 860▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n24-28: 428▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n28-35: 2088▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n40-45: 1\n---- MONTH ----\n2021/01: 185▇▇▇▇▇▇▇▇▇▇▇\n2021/02: 1192▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n2021/03: 491▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n2021/04: 712▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n2021/05: 756▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n2021/06: 523▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n2021/07: 507▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n2021/08: 146▇▇▇▇▇▇▇▇\n2021/09: 83▇▇▇▇\n2021/10: 586▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n2021/11: 227▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n2021/12: 216▇▇▇▇▇▇▇▇▇▇▇▇▇\n```\n\n## Help\n```\nusage: Aggregate EXIF [-h] [-w WIDTH] [-l LENS [LENS ...]] [-c CAMERA [CAMERA ...]]\n                      [--year YEAR [YEAR ...]] [--month MONTH [MONTH ...]]\n                      [--day DAY [DAY ...]] [--yearly] [--monthly] [--daily] [-a]\n                      [--ignore-cache]\n                      [paths ...]\n\npositional arguments:\n  paths                 images paths\n\noptions:\n  -h, --help            show this help message and exit\n  -w WIDTH, --width WIDTH\n                        print width\n  -l LENS [LENS ...], --lens LENS [LENS ...]\n                        select lens\n  -c CAMERA [CAMERA ...], --camera CAMERA [CAMERA ...]\n                        select camera\n  --year YEAR [YEAR ...]\n                        select year\n  --month MONTH [MONTH ...]\n                        select month\n  --day DAY [DAY ...]   select day of month\n  --yearly              view yearly graph\n  --monthly             view monthly graph\n  --daily               view daily graph\n  -a, --cache           save exif in cache\n  --ignore-cache        ignore cache\n```\n\n## Cache\nAggexif supports local caching. If you want to save the cache, add a --cache option. If you want to disable the cache temporarily, use a --ignore-cache option. Since the cache is stored in `~/.config/aggexif/exif.db` as a SQLite, so you can delete it to remove all the cache.\n\n## Tested Camera\n- Nikon Z6/Z7(+FTZ)\n- SONY A7C/A7III\n- OLYMPUS E-PL10\n- Panasonic GX7MK3(GX9)\n- Canon EOS-RP\n\n## Development\nUse poetry.\n\n```\n# run\n$ poetry run aggexif -h\n\n# test(doctest)\n$ poetry run pytest --doctest-modules\n\n# build\n$ poetry build\n\n# local install(after build)\n$ pip install dist/aggexif-x.x.x.tar.gz\n\n# publish\n$ poetry publish -u ponkotuy -p `password`\n```\n',
    'author': 'ponkotuy',
    'author_email': 'web@ponkotuy.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ponkotuy/python-exif',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
