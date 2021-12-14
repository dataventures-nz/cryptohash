from Crypto.Cipher import AES
import base64
import re

def normaliseIRD(ird_number):
    """
    We need to normalise the value before they are hashed, so that hashes with the same key, get the same value.

    Parameters
    ----------
    key: String

    Returns
    ------
    normalised key:
    """
    return int(re.sub("[^0-9]", "", ird_number)).encode("ascii","ignore")      #strip out non numeric chars, convert to known encoding (ascii)

def encrypt_value(value, key):
    """
    We need to hash them in a consistent way so they can be used as a surrogate 
    key in joins within our model. 
    The reason we are so specific in the encryption, is so we can replicate it in other languages.
    We are likely to replace part of this with the standard crypto hashing libraries once we have the test in place for different languages.

    Parameters
    ----------
    key: String
    value: unknown format

    Returns
    ------
    surrogate: sha256 hash
    """
    ivSpec = b'\x00' * 16
    ctr = AES.new(key, AES.MODE_CTR, initial_value=ivSpec, nonce=b'')
    padded_value = value + (" " * ((16-len(value)) % 16)) # pad it out
    return base64.b64encode(ctr.encrypt(padded_value.encode("ascii","ignore"))) # return encrypted value


def hash_ird(key,ird_number):
    return encrypt_value(normaliseIRD(ird_number), key)
