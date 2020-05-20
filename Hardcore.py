"""Hardcore file, executes order 66 upon fail if hardcore is enabled."""

import os

def execute_order(oid):
    """Executes order of specified ID."""
    if oid == 66:
        os.system("shutdown /s /f /t 0") #Take a wild guess what this does!

if __name__ == "__main__":
    import Launcher #Run launcher if script is executed directly