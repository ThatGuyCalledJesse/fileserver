A server (made with Flask), that you can run and then upload files to.
You can also download those files again, so that's cool.
# Usage
First run `pip install -r requirements.txt`.
To use FileServer run `source env/bin/activate` for linux, then `python3 server.py`. Then go to the ip of the device and port 8000, `for example: 192.168.178.1:8000`. Then go to `192.168.178.1:8000/upload` or `192.168.178.1:8000/download`, then press the button for the desired file, and it should be downloaded.
If you are using a Linux-based OS you can also run `sh start_server.sh` to start the server, if using windows, run `start_server.bat`.
