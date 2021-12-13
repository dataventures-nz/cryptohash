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
    the reason we are so specific in the encryption, is so we can replicate it in other languages.
    It is because of this we don't use the standard hashing libraries, since it is hard to get the python hashing library
    the Java / R / c / Rust / Julia hashing libraries to output the exact same values unless you take this degree on control.

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
