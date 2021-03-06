"""Transport module for sending strings to the manager."""

import socket

class Client():
    def __init__(self):
        self.manager_ip = '192.168.2.51'
        self.port = 12345

    def send(self, msg: str):
        """Send string to Manager via the server module. Works differently than Server.send()"""
        
        srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        srvr.connect((self.manager_ip, self.port))
        
        srvr.send(msg.encode(encoding='UTF-8'))
        print('Sent message.')

        resp = []
        srvr.settimeout(5.0) # is there a better way to do this???
        while True: # receive data 1024 bytes at a time
            data = srvr.recv(1024).decode(encoding='UTF-8')
            if data == '':
                break
            resp.append(data) # append decoded string
        
        if resp is None: # shut down and retry
            srvr.close()
            return None

        response = ''.join(resp)

        srvr.close()                     # Close the socket when done

        return response