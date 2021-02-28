class FileManagement:
    def __init__(self, outputfile, inputfile=None):
        self.inputfile = inputfile
        self.outputfile = outputfile

    def read_dictionary(self):
        f = open(self.inputfile, "r")
        lines = f.read().splitlines()
        f.close()
        return lines

    def write_discovery(self, address, password, wif, balance):
        f = open(self.outputfile, "a")
        f.write(address + "|" + password + "|" + wif + "|" + balance + "\n")
        f.close()
