Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "%Appdata%/caffeine.exe" & Chr(34), 0
WinScriptHost.Run Chr(34) & "%Appdata%/caffeineMeter.exe" & Chr(34), 0
Set WinScriptHost = Nothing
