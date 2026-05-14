#!/usr/bin/env python3
import ftplib, io

HOST = 'ftp.appliancerepairclovis.com'
USER = 'prime@appliancerepairclovis.com'
PASS = 'Oyarzabal2026'

ftp = ftplib.FTP()
ftp.connect(HOST, 21, timeout=30)
ftp.login(USER, PASS)
ftp.set_pasv(True)
ftp.cwd('appliancerepairclovis.com/public_html')

buf = io.BytesIO()
ftp.retrbinary('RETR php_errorlog', buf.write)
print(buf.getvalue().decode('utf-8', errors='replace'))
ftp.quit()
