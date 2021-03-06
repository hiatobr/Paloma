# coding: utf-8

import os

import os.path

from setuptools import setup

## Variáveis locais

from src.setup import classifiers
from src.setup import description
from src.setup import license
from src.setup import name
from src.setup import url
from src.setup import version

## Funções locais

def readme():
	with open('README.rst') as f:
		return f.read()

## Variáveis estáticas

plugins = [
		s for s in os.listdir('plugins') if
			os.path.exists(os.path.join('plugins', s, 'plugin.py'))
	]

protocols = [
		s for s in os.listdir('src/protocols') if
			os.path.exists(os.path.join('src/protocols', s, 'protocol.py'))
	]

dependency_links = []

packages = [
		'paloma',
		'paloma.plugins',
		'paloma.protocols',
	] + \
	['paloma.plugins.'+s for s in plugins] + \
	['paloma.protocols.'+s for s in protocols]

package_dir = {
		'paloma': 'src',
		'paloma.plugins': 'plugins',
		'paloma.protocols': 'src/protocols',
	}

scripts = [
		'bin/test.py',
	]

test_suite = ''

tests_require = ''

## Setups
setup(
	author='Hiato',
	author_email='hiato@riseup.net',
	classifiers=classifiers,
	dependency_links=dependency_links,
	description=description,
	include_package_data=True,
	license=license,
	long_description=readme(),
	maintainer='Hiato',
	maintainer_email='hiato@riseup.net',
	name=name,
	packages=packages,
	package_dir=package_dir,
	scripts=scripts,
	test_suite=test_suite,
	tests_require=tests_require,
	url=url,
	version=version,
	zip_safe=False,
)

