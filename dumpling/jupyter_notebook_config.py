import os
import socket


c.NotebookApp.ip = socket.getfqdn()
c.NotebookApp.port = int(os.environ['PORT1'])
c.NotebookApp.open_browser = False
