# coding: utf-8
# Copyright (c) Qotto, 2018

"""
Implementation of different codecs used in SMS PDUs, according to the GSM 03.38 specification.
"""

from binascii import hexlify
from binascii import unhexlify
from bitstring import BitStream

__all__ = ['GSM', 'UCS2']


class GSM:
    """
    GSM 7-bit SMS codec
    """
    ALPHABET = (
        '@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ\x1BÆæßÉ !"#¤%&\'()*+,-./0123456789:;<=>?'
        '¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà'
    )

    ALPHABET_EXT = {
        10: '\f',
        20: '^',
        40: '{',
        41: '}',
        47: '\\',
        60: '[',
        61: '~',
        62: ']',
        64: '|',
        101: '€',
    }
    ALPHABET_EXT_INV = dict([(v[1], v[0]) for v in ALPHABET_EXT.items()])

    CHAR_EXT = 0x1B

    @classmethod
    def decode(cls, data: str, with_padding: bool = False) -> str:
        r"""
        Returns decoded message from PDU string.

        Some examples:

        >>> GSM.decode('C8F71D14969741F977FD07')
        'How are you?'

        >>> GSM.decode('32D0A60C8287E5A0F63B3D07')
        '2 € par mois'

        Decodes without padding
        >>> GSM.decode('AA58ACA6AA8D1A')
        '*115*5#\r'

        Decodes with padding, remove the last <CR>
        >>> GSM.decode('AA58ACA6AA8D1A', True)
        '*115*5#'
        """
        reversed_bits = BitStream(hex=cls.reversed_octets(data)).bin
        septets = [int(reversed_bits[k:k+7], 2) for k in range(len(reversed_bits)-7, -1, -7)]
        res = ''
        is_extended = False
        for char_index in septets:
            if char_index == cls.CHAR_EXT:
                is_extended = True
                continue
            if is_extended:
                is_extended = False
                res += cls.ALPHABET_EXT.get(char_index, ' ')
            else:
                res += cls.ALPHABET[char_index]

        if with_padding and len(res) % 8 == 0 and res.endswith('\r'):
            return res[:-1]
        else:
            return res

    @classmethod
    def encode(cls, data: str, with_padding: bool = False) -> str:
        """
        Returns an encoded PDU string.

        Example:

        >>> GSM.encode("hellohello")
        'E8329BFD4697D9EC37'

        You can also use characters from the extended table:

        >>> GSM.encode("2 € par mois")
        '32D0A60C8287E5A0F63B3D07'

        Encodes without padding
        >>> GSM.encode('*115*5#')
        'AA58ACA6AA8D00'

        Encodes with padding, add an <CR> at the end
        >>> GSM.encode('*115*5#', True)
        'AA58ACA6AA8D1A'
        """
        chars = list()
        for char in data:
            try:
                # tries the standard alphabet
                char_index = cls.ALPHABET.index(char)
            except ValueError:
                chars.append(cls.CHAR_EXT)
                # tries the extended alphabet
                try:
                    char_index = cls.ALPHABET_EXT_INV[char]
                except KeyError:
                    char_index = cls.CHAR_EXT
            if char_index == cls.CHAR_EXT:
                raise ValueError(f"Char \"{char}\" can not be encoded with the GSM 7-bit codec")
            chars.append(char_index)

        if with_padding and (len(chars) + 1) % 8 == 0:
            chars.append(cls.ALPHABET.index('\r'))

        res = '0' * (len(chars) % 8) + ''.join([f'{char:07b}' for char in chars][::-1])
        return cls.reversed_octets(BitStream(bin=res).hex.upper())

    @classmethod
    def reversed_octets(cls, data: str) -> str:
        """
        Reverses octets in a PDU string.

        >>> GSM.reversed_octets("00F1F2F3")
        'F3F2F100'
        """
        return ''.join([data[k:k+2] for k in range(0, len(data), 2)][::-1])


class UCS2:
    """
    UCS-2 SMS codec.

    This codec actually uses the UTF-16 extension, and doesn't warn if
    some characters are out of the pure UCS-2 charset range.
    """
    @classmethod
    def encode(cls, data: str) -> str:
        """
        Returns an encoded PDU string.

        Example:

        >>> UCS2.encode("Je pompe donc je suis.")
        '004A006500200070006F006D0070006500200064006F006E00630020006A006500200073007500690073002E'
        """
        return hexlify(data.encode('utf-16be')).decode('ascii').upper()

    @classmethod
    def decode(cls, data: str) -> str:
        """
        Returns decoded message from PDU string.

        Example:

        >>> UCS2.decode('004C006F00720065006D00200049007000730075006D')
        'Lorem Ipsum'
        """
        return unhexlify(data).decode('utf-16be')
