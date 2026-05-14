#!/usr/bin/env python3
"""
Step 1: Delete wp-content subdirs (keep uploads), using relative paths.
"""
import ftplib, sys

HOST = 'ftp.appliancerepairclovis.com'
USER = 'prime@appliancerepairclovis.com'
PASS = 'Oyarzabal2026'

def connect():
    ftp = ftplib.FTP()
    ftp.connect(HOST, 21, timeout=90)
    ftp.login(USER, PASS)
    ftp.set_pasv(True)
    ftp.cwd('appliancerepairclovis.com')
    ftp.cwd('public_html')
    print("Connected. CWD:", ftp.pwd())
    return ftp

def parse(lines):
    files, dirs = [], []
    for line in lines:
        parts = line.split()
        if len(parts) < 9: continue
        name = ' '.join(parts[8:])
        if name in ('.', '..'): continue
        if line.startswith('d'): dirs.append(name)
        else: files.append(name)
    return files, dirs

def rm_recursive(ftp, path):
    """Delete everything inside path, then remove path itself."""
    saved = ftp.pwd()
    try:
        ftp.cwd(path)
    except Exception as e:
        print(f"  Cannot cd into {path}: {e}")
        return
    here = ftp.pwd()
    lines = []
    ftp.retrlines('LIST', lines.append)
    files, dirs = parse(lines)
    for f in files:
        try:
            ftp.delete(f)
            print(f"  del {here}/{f}")
        except Exception as e:
            print(f"  ERR del {f}: {e}")
    for d in dirs:
        rm_recursive(ftp, d)
    ftp.cwd(saved)
    try:
        ftp.rmd(path)
        print(f"  rmd {here}")
    except Exception as e:
        print(f"  ERR rmd {path}: {e}")

ftp = connect()

# List wp-content
lines = []
ftp.cwd('wp-content')
ftp.retrlines('LIST', lines.append)
print("\n=== wp-content contents ===")
for l in lines: print(l)
files, dirs = parse(lines)

# Delete all wp-content files
for f in files:
    try:
        ftp.delete(f)
        print(f"del wp-content/{f}")
    except Exception as e:
        print(f"ERR {f}: {e}")

# Delete all wp-content dirs EXCEPT uploads
ftp.cwd('..') # back to public_html
for d in dirs:
    if d == 'uploads':
        print(f"SKIP wp-content/uploads — keeping images")
        continue
    print(f"\nDeleting wp-content/{d} ...")
    ftp.cwd('wp-content')
    rm_recursive(ftp, d)
    ftp.cwd('..') # back to public_html

print("\n✅ wp-content cleanup done.")

# Final check
lines2 = []
ftp.cwd('wp-content')
ftp.retrlines('LIST', lines2.append)
print("\n=== wp-content after cleanup ===")
for l in lines2: print(l)

ftp.quit()
