# SMS-PDU Decoder

This library will help you to decode raw SMS data you can get from a GSM modem (generally by using AT commands).

It has some encoding functionality as well.

It is recommended to read the [GSM 03.40](https://en.wikipedia.org/wiki/GSM_03.40) specification to better understand the components this library works wtih.

## How to install

This library has been successfully tested and works with Python versions ranging from 3.7 up to 3.10.

```
pip install smspdudecoder
```

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

## How to test and contribute

First, clone this repository:

```sh
git clone git@github.com:Qotto/smspdudecoder.git
# or use HTTPS if you are unauthenticated:
# git clone https://github.com/Qotto/smspdudecoder.git
cd smspdudecoder
```

### Using Docker

The easiest way to test this library against all supported Python versions is to use Docker.

```sh
make docker-test
```

Behinds the scenes, this will build a Docker image with all supported Python versions and run the tests with [tox](https://tox.wiki/).

### Using your existing Python installation

If you want to simply run the test suite, make sure that you have dependencies installed with:

```sh
pip install -r requirements.txt
```

And use the following command:

```sh
make test
```
