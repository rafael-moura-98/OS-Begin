:: Admin permission is expected before running this script
:: This script will install choco and run the python file "win10_startup.py" which is expected to be along this .bat one.


:: A series of files will be also created by the python file. Check file to see more about it.
@echo off

echo %1

if "%1" == "a" echo "All process was selectec!"

::powershell -Command "& {Set-ExecutionPolicy AllSigned; Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))}"

::choco python tree -y

::python .\win10_startup.py
python .\tryyy.py %1

:: Tip - to update your programmers downloaded from choco you just need to run `cup all` :)  """
