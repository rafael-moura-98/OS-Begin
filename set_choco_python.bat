:: Admin permission is expected before running this script
:: This script will install choco and run the python file "win10_startup.py" which is expected to be along this .bat one.
:: A series of files will be also created by the python file. Check file to see more about it.


@echo off


:: This "check_permission" bit of code was humbly stolen from https://superuser.com/users/267244/alex
goto check_Permissions

:check_Permissions
echo Administrative permissions required. Detecting permissions...

net session >nul 2>&1
if %errorLevel% == 0 (
    echo "Success: Looks like you own your pants! That"s cool bro!"
) else (
    echo "Hey you! Only adults here! Come back and you're admin."
    Exit
)


powershell -Command "& {Set-ExecutionPolicy AllSigned; Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))}"

choco install python -y

python .\win10_startup.py %1

:: Tip - to update your programmers downloaded from choco you just need to run `cup all` :)  """
