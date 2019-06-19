from pirc522 import RFID
import datetime, sys

import sys

rdr = RFID()
util = rdr.util()
datetime.datetime.now()
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)


def welcome():
    # Welcome message.
    print("[i] RFID Key Brute-forcer.")
    print("[i] Written by Nobatgeldi, built on https://github.com/Nobatgeldi.")
    print("[i] Press Ctrl-C to stop the program.")
    print(datetime.datetime.now())
    file.write("Time:"+str(datetime.datetime.now())+"\n")


def tempcombo(t1, t2, t3, t4, t5, t6):
    temp_combo = []
    temp_combo.extend([t1, t2, t3, t4, t5, t6])
    return temp_combo


def Reader(attempt):
    try:

        rdr.wait_for_tag()
        (error, tag_type) = rdr.request()
        if not error:
            print("Tag detected")
            (error, uid) = rdr.anticoll()
            if not error:
                print("UID: " + str(uid))
                # Select Tag is required before Auth
                if not rdr.select_tag(uid):
                    key = [hex(attempt[0]), hex(attempt[1]), hex(attempt[2]), hex(attempt[3]), hex(attempt[4]), hex(attempt[5])]
                    print key
                    # Auth for block 2 (block 2 of sector 0) using default shipping key A
                    if not rdr.card_auth(rdr.auth_a, 2, attempt, uid):
                        # This will print something like (False, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                        print("Reading block 2: " + str(rdr.read(2)))
                        # Log found key
                        file.write("Int:"+str(attempt)+"\n")
                        file.write("Hex:"+str(key)+"\n")
                        file.close()
                        # Always stop crypto1 when done working
                        rdr.stop_crypto()
                        sys.exit("[!] SUCCESS [!] - The correct key is " + str(key))

    # Stop on Ctrl+C and clean up
    except KeyboardInterrupt:
        rdr.cleanup()


def Start(target):
    welcome()
    print("[i] Pure brute force option selected... Generating all 274,941,996,890,625 combinations... Please be patient.")

    if target == "ascending":
        i1 = 1
        i2 = 1
        i3 = 1
        i4 = 1
        i5 = 1
        i6 = 1

        while (i1 <= 255):
            temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
            while (i2 <= 255):
                temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
                while (i3 <= 255):
                    temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
                    while (i4 <= 255):
                        temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
                        while (i5 <= 255):
                            temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
                            while (i6 <= 255):
                                temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
                                Reader(temp_combo)
                                i6 += 1
                            Reader(temp_combo)
                            i6 = 1
                            i5 += 1
                        Reader(temp_combo)
                        i5 = 1
                        i4 += 1
                    Reader(temp_combo)
                    i4 = 1
                    i3 += 1
                Reader(temp_combo)
                i3 = 1
                i2 += 1
            Reader(temp_combo)
            i2 = 1
            i1 += 1

        i1 = 1

    elif target == "descending":
        i1 = 255
        i2 = 255
        i3 = 255
        i4 = 255
        i5 = 255
        i6 = 255
        print("Generating all.")
        while (i1 >= 1):
            temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
            Reader(temp_combo)
            print temp_combo

            while (i2 >= 1):
                temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
                Reader(temp_combo)
                print temp_combo

                while (i3 >= 1):
                    temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
                    Reader(temp_combo)
                    print temp_combo

                    while (i4 >= 1):
                        temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
                        Reader(temp_combo)
                        print temp_combo

                        while (i5 >= 1):
                            temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
                            Reader(temp_combo)
                            print temp_combo

                            while (i6 >= 1):
                                temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
                                Reader(temp_combo)
                                print temp_combo
                                i6 -= 1

                            i6 = 255
                            i5 -= 1

                        i5 = 255
                        i4 -= 1

                    i4 = 255
                    i3 -= 1

                i3 = 255
                i2 -= 1

            i2 = 255
            i1 -= 1

        i1 = 255

    else:
        sys.exit("[-] No value for the --order parameter was provided, please choose from either ascending or descending.")


if __name__ == '__main__':
    file = open("log.txt","a")
    Start("descending")
    #Start("ascending")