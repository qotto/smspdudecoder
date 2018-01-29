#!/usr/bin/env python

from setuptools import setup

if __name__ == '__main__':
    setup(
        name='SMS PDU Decoder',
        version='0',
        url='https://github.com/qotto/smspdu',
        license='MIT',
        author='Alexandre Syenchuk',
        author_email='sacha@qotto.net',
        description='Qotto/smspdu',
        packages=['smspdu'],
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'bitstring >= 3.1',
        ],
        classifiers=[
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3.6',
        ],
    )
