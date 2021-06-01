from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='arbolbinario',
    version='1.0.0a0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'serve = rest.app:run_rest_server',
            'login = cli.app:login',
        ]
    },
    install_requires=[
        'certifi==2017.11.5',
        'chardet==3.0.4',
        'Click==6.7',
        'clickclick==1.2.2',
        'connexion==1.2',
        'Flask==0.12.2',
        'Flask-Cors==3.0.3',
        'py-healthcheck==1.7.0',
        'idna==2.6',
        'inflection==0.3.1',
        'itsdangerous==0.24',
        'Jinja2==2.10',
        'jsonpickle==0.9.5',
        'jsonschema==2.6.0',
        'MarkupSafe==1.0',
        'PyYAML==3.12',
        'requests==2.18.4',
        'six==1.11.0',
        'urllib3==1.26.5',
        'Werkzeug==0.12.2'
    ])
