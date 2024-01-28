#!/usr/bin/python
import os
import sys
import optparse
import compulink
import time


COMPULINK_PIN = 24
COMPULINK_ADDR = 1

def main(argv):
    # setup compulink
    mycompulink = compulink.CompuLink(COMPULINK_PIN, COMPULINK_ADDR)
    mycompulink.debug = 1
    for address in range(1,16):
        mycompulink.address = address
        for command in range(1,16):
            mycompulink.sendCommand(command)
            time.sleep(3)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
