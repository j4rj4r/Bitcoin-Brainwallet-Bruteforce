import argparse
import sys

from file_management import FileManagement
from scan import Scan

if __name__ == '__main__':

    inputfile = 'default_wordlist.txt'
    outputfile = 'output.txt'

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Words dictionary file (e.g. dictionary.txt)',
                        type=str, required=False)
    parser.add_argument('-o', '--output', help='output file (e.g. output.txt)',
                        type=str, required=False)
    parser.add_argument('-c', '--compressed', help="Use compressed addresses", action='store_true', required=False)
    parser.add_argument('--version', action='version', version='Version : 1.01')

    args = parser.parse_args()

    if args.input:
        inputfile = args.input
    if args.output:
        outputfile = args.output

    # We initialize file management
    file = FileManagement(outputfile, inputfile)
    # A list with the contents of the dictionary is retrieved.
    wordlist = file.read_dictionary()
    # The scan object is initialized with the list of dictionary contents.
    scan = Scan(file, wordlist)
    # Start the scan and get the result.
    try:

        if args.compressed:
            print('Compressed Addresses : ON')
            result = scan.launch(compressed=True)
        else:
            result = scan.launch()
        # We write the result in a output file
        if not result:
            print('We didn\'t find anything !')

    except KeyboardInterrupt:
        print('Exit...')
        sys.exit(0)
