# MFRC522PythonAuthKeyBruteforcer
Just a simple RFID authentication key brute-force program written in python, as all the ones I found were written in C. This is much more user friendly

Usage:

Add any keys you wish to test to the keys.txt file. They must be in the following format:
a0,a1,a2,a3,a4,a5

So remove any hex nonsense like \x or 0x from the front.

Make sure to have an Mifare RC522 RFID Reader setup and running in order to use this software.
This software is built on top of https://github.com/mxgxw/MFRC522-python.

To connect the reader to a  Raspberry Pi, refer to the following wiring diagram:
https://cdn.pimylifeup.com/wp-content/uploads/2017/10/RFID-Diagram.png

In the Raspberry Pi config, make sure to enable the SPI Interface

Lastly, clone SPI-Py from the following repository:
https://github.com/lthiery/SPI-Py
- Install with the following command:
- root@linux:/Downloads/SPI-Py# python setup.py install
