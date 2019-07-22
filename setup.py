#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

if __name__ == '__main__':
    setup(
        name='smspdudecoder',
        version='1.2.2',
        url='https://github.com/qotto/smspdu',
        license='MIT',
        author='Alexandre Syenchuk',
        author_email='sacha@qotto.net',
        description='Python SMS PDU Decoder',
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=['smspdu'],
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'bitstring >= 3.1',
            'pytz',
        ],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Intended Audience :: Telecommunications Industry',
            'License :: OSI Approved :: MIT License',
            'Topic :: Communications :: Telephony',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        ],
    )
