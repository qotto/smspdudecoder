# SMS-PDU Decoder

This library will help you to decode raw SMS data you can get from a GSM modem.

It has some encoding functionality as well.

It is recommended to read [GSM 03.40](https://en.wikipedia.org/wiki/GSM_03.40) to facilitate understanding.

Requires Python 3.6.

## How to install

```
pip install smspdudecoder
```

## How to test

If you want to experiment with it, clone the repository, do some changes, and type `tox` (tox needs to be installed) to launch tests.

## How to use

Please take a look at the source code, which comes with documentation and examples.

For instance, you can use GSM and UCS2 encodings just like that:

```python
>>> from smspdu.codecs import GSM, UCS2
>>> GSM.decode('C8F71D14969741F977FD07')
'How are you?'
>>> UCS2.decode('004C006F00720065006D00200049007000730075006D')
'Lorem Ipsum'
```
