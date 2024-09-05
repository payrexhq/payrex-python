from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='payrex-python',
    version='1.0.0',
    author='PayRex',
    author_email='support@payrexhq.com',
    description='PayRex Python Library',
    long_description=(Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    keywords='payrex',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    license='MIT',
    url='https://github.com/payrexhq/payrex-python'
)
