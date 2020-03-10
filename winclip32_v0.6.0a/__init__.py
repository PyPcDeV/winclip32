import sys, os
winclip32_PATH = os.path.abspath(os.path.dirname(__file__))
try:
    os.environ['PATH'] = ';'.join((winclip32_PATH, os.environ['PATH']))
    sys.path.append(winclip32_PATH)
except Exception:
    print("Couldn't add winclip32 to sys.path...\nwinclip32 path : " +winclip32_PATH)

from winclip32.main import *

del winclip32_PATH, clipboard_formats_str, clipboard_formats_int

