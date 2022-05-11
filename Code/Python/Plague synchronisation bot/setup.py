# -*- encoding: utf-8 -*-
import os
"""
<u>Setup of the Bot</u>
"""
exit_code = None


def run(command: str, return_code=False):
    global exit_code
    """Simply runs the command and return the error code"""

    exit_code = os.system(command)
    success = False
    if exit_code == 0:
        success = True

    if return_code:
        return success
    else:
        return success, exit_code


print("Checking")
