import os
from time import sleep
try:
 import pyperclip
except ModuleNotFoundError:
 x = os.system("python -m pip install pyperclip")
 if x != 0:
  print("Failed to install module.")
  exit(x)
import pyperclip
pyperclip.copy(chr(12))
print("Copied to clipboard")
sleep(5)