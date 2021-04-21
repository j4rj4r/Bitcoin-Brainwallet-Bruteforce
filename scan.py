from privatekey import PrivateKey
from bit import Key


class Scan:

    def __init__(self, file, wordlist):
        self.file = file
        self.wordlist = wordlist
        self.pkey = PrivateKey()
        self.discoveries = []
        self.balancetotal = 0
        self.noemptyaddr = 0

    def launch(self, compressed=False):
        for password in self.wordlist:
            self.pkey.from_passphrase(password)
            if compressed:
                wif = self.pkey.privatekey_to_wif(compressed=True)
            else:
                wif = self.pkey.privatekey_to_wif()
            key = Key(wif)
            balance = key.get_balance('btc')
            # If the balance is not empty
            if balance != "0":
                if key.address not in self.discoveries:
                    print(f'{key.address} : {balance}')
                    self.discoveries.append(key.address)
                    self.file.write_discovery(key.address, password, self.pkey.wif, balance)
                    self.balancetotal += float(balance)
                    self.noemptyaddr += 1
            else:
                print(f'Empty balance for : {password}')

        print(f'You have found a total of  {self.balancetotal} btc')
        print(f'Addresses with btc : {self.noemptyaddr}')
        return self.discoveries
