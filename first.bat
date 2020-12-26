@ECHO OFF

Copy "caffeine.exe" "%AppData%" 

Copy "caffeineMeter.exe" "%AppData%"

Copy "starter.vbs" "%AppData%"

echo [InternetShortcut] >> "%Appdata%\Microsoft\Windows\Start Menu\Programs\Startup\autostart.url"
echo URL="%Appdata%\starter.vbs" >> "%Appdata%\Microsoft\Windows\Start Menu\Programs\Startup\autostart.url"
echo IconFile=C:\WINDOWS\system32\SHELL32.dll >> "%Appdata%\Microsoft\Windows\Start Menu\Programs\Startup\autostart.url"
echo IconIndex=20 >> "%Appdata%\Microsoft\Windows\Start Menu\Programs\Startup\autostart.url"

exit
