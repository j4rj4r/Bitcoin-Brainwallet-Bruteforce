# Bitcoin-Brainwallet-Bruteforce
A project for bruteforce bitcoin brainwallet.
In input it takes a dictionary and for each line it generates a private key and checks if there is a balance.

## Requirements :
- Python 3.x
- Dictionary file

## Install :
```
python3 -m pip install -r requirements.txt 
```
## Usage :

The default dictionary is used if it is not defined.
```
python3 main.py 
```
Or you can define another dictionary to use.
```
python3 main.py -i anotherdict.txt
```
If you want to use compressed addresses
```
python3 main.py -c
```