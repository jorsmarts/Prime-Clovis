#!/usr/bin/env python3
"""
Upload all docs/ files to public_html, rewriting /Prime-Clovis/ paths to /.
"""
import ftplib, os, sys

HOST = 'ftp.appliancerepairclovis.com'
USER = 'prime@appliancerepairclovis.com'
PASS = 'Oyarzabal2026'
LOCAL_ROOT = '/home/user/webapp/docs_live'
REMOTE_ROOT = 'appliancerepairclovis.com/public_html'

def connect():
    ftp = ftplib.FTP()
    ftp.connect(HOST, 21, timeout=90)
    ftp.login(USER, PASS)
    ftp.set_pasv(True)
    ftp.cwd(REMOTE_ROOT)
    return ftp

def ensure_dir(ftp, remote_dir):
    """Create remote directory if it doesn't exist."""
    try:
        ftp.mkd(remote_dir)
    except ftplib.error_perm:
        pass  # already exists

def upload_file(ftp, local_path, remote_path):
    with open(local_path, 'rb') as f:
        ftp.storbinary(f'STOR {remote_path}', f)

def deploy():
    ftp = connect()
    print(f"Connected. CWD: {ftp.pwd()}")

    uploaded = 0
    errors = 0

    for dirpath, dirnames, filenames in os.walk(LOCAL_ROOT):
        # Compute relative path from docs/
        rel_dir = os.path.relpath(dirpath, LOCAL_ROOT)

        # Create remote subdirectory if needed
        if rel_dir != '.':
            parts = rel_dir.split(os.sep)
            current = ''
            for part in parts:
                current = f"{current}/{part}" if current else part
                ensure_dir(ftp, current)

        for filename in filenames:
            local_file = os.path.join(dirpath, filename)

            if rel_dir == '.':
                remote_file = filename
            else:
                remote_file = f"{rel_dir.replace(os.sep, '/')}/{filename}"

            try:
                upload_file(ftp, local_file, remote_file)
                print(f"  UP {remote_file}")
                uploaded += 1
            except Exception as e:
                print(f"  ERR {remote_file}: {e}")
                errors += 1
                # Reconnect on error
                try:
                    ftp.quit()
                except:
                    pass
                ftp = connect()

    ftp.quit()
    print(f"\n✅ Done. {uploaded} uploaded, {errors} errors.")

deploy()
