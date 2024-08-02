#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a simple Python script to send ZPL to a Zebra printer.
# It uses the socket library to create a TCP connection to the printer.
# Then it sends the ZPL command to the printer.

import socket       

# Variables
PRINT_SOCKET = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         
HOST = "10.0.1.220" 
PORT = 9100 
label_list = [
]
ZPL_TEMPLATE_PREFIX = "^XA~TA000~JSN^LT0^MNW^MDT^PON^PMN^LH0,0^JMA^PR6,6~SD15^JUS^LRN^CI27^PA0,1,1,0^XZ^XA^MMT^PW831^LL1218^LS0^FT191,898^BXN,45,200,0,0,1,_,1"

ZPL_TEMPLATE_SUFFIX = "^PQ1,0,1,Y^XZ"

def init_settings():
    global PRINT_SOCKET
    PRINT_SOCKET = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    
    global HOST
    HOST = "10.0.1.220" 
    global PORT
    PORT = 9100 
    PRINT_SOCKET.connect((HOST, PORT))

def generate_label_list(quantity, data, suffix, starting_number, trailing_zeros):
    print("Generating label list")
    global label_list
    count = 0

    while count < quantity:
        if suffix == "None":
            label_list.append(data)
        elif suffix == "Alpha":
            label_list.append(data + chr(65 + count))
        else:
            label_list.append(data + str(count + starting_number).zfill(trailing_zeros))
        count += 1


def print_labels():
    for label in label_list:
        print("For label: " + label)
        try:
            # 2-character
            if len(label) == 2:
                zpl_command = (
                    ZPL_TEMPLATE_PREFIX
                    + "^FH\^FD%s^FS^FT264,1113^A0N,203,271^FH\^CI28^FD%s^FS^CI27"
                    + ZPL_TEMPLATE_SUFFIX
                ) % (label, label)
            # 3-character
            elif len(label) == 3:
                zpl_command = (
                    ZPL_TEMPLATE_PREFIX
                    + "^FH\^FD%s^FS^FT198,1113^A0N,203,271^FH\^CI28^FD%s^FS^CI27"
                    + ZPL_TEMPLATE_SUFFIX
                ) % (label, label)
            #4-character
            elif len(label) == 4:
                zpl_command = (
                    ZPL_TEMPLATE_PREFIX
                    + "^FH\^FD%s^FS^FT132,1113^A0N,203,271^FH\^CI28^FD%s^FS^CI27"
                    + ZPL_TEMPLATE_SUFFIX
                ) % (label, label)
            elif len(label) == 5:
                zpl_command = (
                    ZPL_TEMPLATE_PREFIX
                    + "^FH\^FD%s^FS^FT67,1113^A0N,203,271^FH\^CI28^FD%s^FS^CI27"
                    + ZPL_TEMPLATE_SUFFIX
                ) % (label, label)
            else:
                print(f"Label length not supported: {len(label)}", label)
                continue

            PRINT_SOCKET.send(zpl_command.encode()) #encode string to bytes
        except Exception as e:
            print("Error with the connection:", str(e))



def start(quantity, size, data, suffix, starting_number, trailing_zeros):
    init_settings()
    generate_label_list(quantity, data, suffix, starting_number, trailing_zeros)
    print_labels()
    PRINT_SOCKET.close()