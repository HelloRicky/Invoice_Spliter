from cx_Freeze import setup, Executable

setup(
    name = "Gui test",
    version = "0.1",
    description = "My GUI Program",
    executables = [Executable('gui.py')],
    )
