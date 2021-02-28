import hashlib
import binascii
import base58


class PrivateKey:
    def __init__(self, _privatekey=None):
        self._privatekey = _privatekey
        self._passphrase = None
        self.wif = None

    def from_passphrase(self, passphrase):
        hex_private_key = hashlib.sha256(passphrase.encode('utf-8')).hexdigest()
        self._privatekey = hex_private_key
        self._passphrase = passphrase
        self.wif = None
        return self._privatekey

    def privatekey_to_wif(self, _privatekey=None, compressed=False):
        if _privatekey is None:
            privatekey = self._privatekey
        else:
            privatekey = _privatekey
        if compressed:
            extented_key = "80" + privatekey + "01"
        else:
            extented_key = "80" + privatekey
        first_sha256 = hashlib.sha256(binascii.unhexlify(extented_key)).hexdigest()
        second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
        final_key = extented_key + second_sha256[:8]
        wif = base58.b58encode(binascii.unhexlify(final_key))
        wif = wif.decode("utf-8")
        self.wif = wif
        return wif
