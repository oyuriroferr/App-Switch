from os import system as cmd
from os import path, environ
from shutil import unpack_archive
file_name = "main.zip"
desktop = path.join(environ["USERPROFILE"], "Desktop")
cmd(f'cd {desktop} && powershell Invoke-WebRequest "https://github.com/oyuriroferr/App-Switch/archive/refs/heads/Installation.zip" -OutFile "{file_name}"')
unpack_archive(rf'{desktop}\{file_name}', desktop + r"\main", 'zip')
cmd(f'start {desktop + r"\main\App-Switch-Installation\Main\Switch-App.exe"}')
cmd(f'del /f /q {desktop + r"\\" + file_name } && rmdir /S /Q {desktop + r"\main\App-Switch-Installation\Installer"}')
