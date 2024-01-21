import sys
from cx_Freeze import setup, Executable

# build_exe_options = {
#     "excludes": ["tkinter", "unittest"],
#     "zip_include_packages": ["encodings", "PySide6"],
# }

base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="JoRunner",
    version="1.0",
    description="Aide Marin à rejoindre les JO.",
    # options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)

