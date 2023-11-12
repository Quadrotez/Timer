from cx_Freeze import setup, Executable

setup(
    name="YourScript",
    version="1.0",
    description="Your Description",
    executables=[Executable("main.py")]
)
