# Port-finder is a Open-source Python project By naem 
#v2.0 colourful designs
import socket
import logging
import time

print (""" 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                   _           __ _           _            +
+                 | |         / _(_)         | |            +
+ _ __   ___  _ __| |_ ______| |_ _ _ __   __| | ___ _ __   +
+| '_ \ / _ \| '__| __|______|  _| | '_ \ / _` |/ _ \ '__|  +
+| |_) | (_) | |  | |_       | | | | | | | (_| |  __/ |     +
+| .__/ \___/|_|   \__|      |_| |_|_| |_|\__,_|\___|_|     +
+| |                                                        +
+|_|                                            #N-A_v2.0   +
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
A Faster Port Checker From 1-65535 port with Log-file
""")
     
class SConnect:

    def __init__(self, ip, port=None):
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
        self.s_connection = socket.socket(socket.AF_INET,       socket.SOCK_STREAM)
        self.s_connection.settimeout(0.3)

    def portscan(self):

        return self.s_connection.connect_ex(self.address)


def main():

    logging.basicConfig(filename="errlog.log", format="%(asctime)s : %(message)s")
    logging.info("Start")
    print("\nPlease insert a IP address(ip4/6) that you want to scan for open and closed ports.")
    u_ip = input("\nTarget IP:>>> ")

    open_pcounter = 0
    closed_pcounter = 0

    if u_ip is not None:
        for p in range(1, 65536):
            start_ptime = time.time()
            c = SConnect(u_ip, p)
            if c.portscan() == 0:
                print("Port {} is open".format(p))
                open_pcounter += 1
            else:
                print("Port {} is closed".format(p))
                closed_pcounter += 1
            print("--- %s seconds ---" % (time.time() - start_ptime))
    else:
        print("You failed, terminating.\n")

    print("Total open ports:%s".format(open_pcounter))
    print("Total closed ports:%s".format(closed_pcounter))
    logging.info("Finished")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
