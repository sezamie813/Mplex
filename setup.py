from setuptools import setup, find_packages

setup(
    name='terminalforge',
    version='0.1.0',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'terminalforge=cli.terminalforge:app',
        ],
    },
    include_package_data=True,
    description='AI-Powered Development Environment',
    author='TerminalForge Team',
    license='MIT',
)
