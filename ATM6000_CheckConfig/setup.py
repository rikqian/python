import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": [
    "dbinfo", "os", "pymysql"], "excludes": ["tkinter"], "include_files": ["dbconfig.ini", "README", "vc_redist.x64.exe"], "include_msvcr": True}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name='ATM6000_V21_Checker',
      version="0.1",
      description="ATM6000 v2.1 check configuration",
      options={"build_exe": build_exe_options},
      executables=[Executable("chkconfig.py", base=None, targetName='ATM6000_V21_Checker.exe')])
