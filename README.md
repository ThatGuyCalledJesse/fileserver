A server (made with Flask), that you can run and then upload files to.
You can also download those files again, so that's cool.
# Usage
To use FileServer run `source env/bin/activate`, then `python3 server.py`. Then go to the ip of the device and port 8000, `for example: 192.168.178.1:8000`. Then go to `192.168.178.1:8000/upload` or `192.168.178.1:8000/download`, to download a file go to `192.168.178.1:8000/download/<filename>` and replace <filename> with the name of the (uploaded) file, for example 'photo.jpg'.
