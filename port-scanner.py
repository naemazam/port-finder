# Network port scanner
# Focus first will be on making the functionality of the software.
# Second focus will be on lowering the runtime of the software.


import socket
import logging
import time


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
    print("\nHello user and welcome to Network Port Scanner!")
    print("Please insert a IP address that you want to scan for open and     closed ports.")
    print("The range of ports scanned is 1-65535.")
    u_ip = input("\nTarget IP: ")

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