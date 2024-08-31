import cx_Freeze, sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"


executables = [cx_Freeze.Executable("Excel_auto.py", base=base, target_name="Node")]

cx_Freeze.setup(
    name="Node",
    options={"build_exe": {"packages": ["tkinter","pandas","openpyxl"], "include_files": [
        "CMDB.xlsx",
    ]}},
    version="1.0",
    description="To find node",
    executables=executables
)