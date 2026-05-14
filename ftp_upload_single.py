#!/usr/bin/env python3
"""Upload a single file to public_html via FTP."""
import ftplib, sys

HOST = 'ftp.appliancerepairclovis.com'
USER = 'prime@appliancerepairclovis.com'
PASS = 'Oyarzabal2026'

local_file  = sys.argv[1]   # e.g. /home/user/webapp/cleanup.php
remote_name = sys.argv[2]   # e.g. cleanup.php

ftp = ftplib.FTP()
ftp.connect(HOST, 21, timeout=60)
ftp.login(USER, PASS)
ftp.set_pasv(True)
ftp.cwd('appliancerepairclovis.com')
ftp.cwd('public_html')
print("CWD:", ftp.pwd())

with open(local_file, 'rb') as f:
    ftp.storbinary(f'STOR {remote_name}', f)
print(f"Uploaded: {remote_name}")
ftp.quit()
