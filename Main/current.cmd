@echo off
setlocal enabledelayedexpansion

:: Definir a lista de comandos
set "commands[0]=python  %%~dp0Effects\Invert.py & python  %%~dp0Effects\Rectangles.py"
set "commands[1]=python  %%~dp0Effects\Invert.py"
set "commands[2]=python  %%~dp0Effects\CursorFollow.py & python  %%~dp0Effects\Invert.py & python  %%~dp0Effects\RandomErrors.py"
set "commands[3]=python  %%~dp0Effects\RandomErrors.py & python  %%~dp0Effects\Invert.py"
set "commands[4]=python  %%~dp0Effects\Tunnel.py"
set "commands[5]=python  %%~dp0Effects\Invert.py & python  %%~dp0Effects\Invert.py"
set "commands[6]=python  %%~dp0Effects\Void.py"
set "commands[7]=python  %%~dp0Effects\Void.py & python  %%~dp0Effects\Invert.py"

:: Gerar número aleatório entre 0 e 7
set /a random1=%random% %% 8
set /a random2=%random% %% 8

:: Escolher dois comandos aleatórios
set "command1=!commands[%random1%]!"
set "command2=!commands[%random2%]!"

:: Concatenar os comandos escolhidos
echo !command1! & !command2!
