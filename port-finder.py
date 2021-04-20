#!/usr/bin/python3
GNU nano 4.9.3                       
import socket




print (""" 
                    _           __ _           _           
                  | |         / _(_)         | |          
  _ __   ___  _ __| |_ ______| |_ _ _ __   __| | ___ _ __ 
 | '_ \ / _ \| '__| __|______|  _| | '_ \ / _` |/ _ \ '__|
 | |_) | (_) | |  | |_       | | | | | | | (_| |  __/ |   
 | .__/ \___/|_|   \__|      |_| |_|_| |_|\__,_|\___|_|   
 | |                                                      
 |_|                             #-n_A                       """)




ip = raw_input("enter the IP Adress: ")
port = input("Enter the Port Number: ")
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if sock.connect_ex((ip,port)):
       print "Port ",port, "is closed"
else:
         print"Port",port,"is OPEN"
