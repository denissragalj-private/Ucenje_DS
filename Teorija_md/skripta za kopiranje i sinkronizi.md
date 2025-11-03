<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# trebam jednu bat skriptu za kopiranje i sinkroniziranje foldera s jedne lokacije na drugu , radim na windows 11

Evo nekoliko BAT skripti za kopiranje i sinkroniziranje foldera na Windows 11:

## Osnovna skripta za kopiranje

```batch
@echo off
set SOURCE=C:\Izvor
set DESTINATION=D:\Odrediste

echo Kopiram fajlove iz %SOURCE% u %DESTINATION%...
xcopy "%SOURCE%" "%DESTINATION%" /E /Y /I
echo Kopiranje završeno!
pause
```


## Napredna skripta za sinkroniziranje

```batch
@echo off
title Sinkronizacija Foldera
color 0A

REM Definiraj putanje
set SOURCE=C:\Moj_Folder
set DESTINATION=D:\Backup_Folder

REM Kreiraj log fajl
set LOGFILE=%~dp0sync_log_%date:~-4,4%%date:~-10,2%%date:~-7,2%.txt

echo ================================== >> %LOGFILE%
echo Sinkronizacija pocinje: %date% %time% >> %LOGFILE%
echo ================================== >> %LOGFILE%

echo Sinkronizujem foldere...
echo Izvor: %SOURCE%
echo Odrediste: %DESTINATION%

REM Koristi robocopy za sinkronizaciju
robocopy "%SOURCE%" "%DESTINATION%" /MIR /R:3 /W:5 /LOG+:%LOGFILE% /TEE /NP

if %errorlevel% leq 3 (
    echo Sinkronizacija uspešno završena!
    echo Sinkronizacija uspešno završena: %date% %time% >> %LOGFILE%
) else (
    echo Greška tokom sinkronizacije!
    echo Greška tokom sinkronizacije: %date% %time% >> %LOGFILE%
)

pause
```


## Skripta sa proverom postojanja foldera

```batch
@echo off
setlocal enabledelayedexpansion

REM Definiraj putanje
set SOURCE=C:\Dokumenti
set DESTINATION=D:\Backup\Dokumenti

REM Proveri da li izvorni folder postoji
if not exist "%SOURCE%" (
    echo GREŠKA: Izvorni folder ne postoji!
    echo Putanja: %SOURCE%
    pause
    exit /b 1
)

REM Kreiraj odredišni folder ako ne postoji
if not exist "%DESTINATION%" (
    echo Kreiram odredišni folder...
    mkdir "%DESTINATION%"
)

REM Pitaj korisnika za tip operacije
echo Izaberi opciju:
echo 1. Obično kopiranje (zadržava stare fajlove)
echo 2. Sinkronizacija (briše dodatne fajlove u odredištu)
set /p choice="Unesi broj (1 ili 2): "

if "%choice%"=="1" (
    echo Kopiram fajlove...
    robocopy "%SOURCE%" "%DESTINATION%" /E /R:3 /W:5
) else if "%choice%"=="2" (
    echo Sinkronizujem fajlove...
    robocopy "%SOURCE%" "%DESTINATION%" /MIR /R:3 /W:5
) else (
    echo Nevaljan izbor!
    pause
    exit /b 1
)

echo Operacija završena!
pause
```


## Objašnjenje parametara

### XCOPY parametri:

- `/E` - kopira podfoldere uključujući prazne
- `/Y` - ne pita za potvrdu prepisivanja
- `/I` - tretira odredište kao folder


### ROBOCOPY parametri:

- `/MIR` - mirror (sinkronizuje i briše dodatne fajlove)
- `/E` - kopira podfoldere uključujući prazne
- `/R:3` - pokušava 3 puta kod greške
- `/W:5` - čeka 5 sekundi između pokušaja
- `/LOG+` - dodaje u log fajl
- `/TEE` - prikazuje output na ekranu i u log
- `/NP` - ne prikazuje procenat


## Saveti za korišćenje

1. **Promeni putanje**: Upiši svoje putanje umesto primera
2. **Pokreni kao administrator**: Za pristup svim folderima
3. **Testiraj prvo**: Koristi `/L` parametar za test bez kopiranja
4. **Zakaži automatsko pokretanje**: Dodaj u Task Scheduler

Koju varijantu skripte želiš da koristiš?

