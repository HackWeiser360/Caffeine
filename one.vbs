Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "first.bat" & Chr(34), 0
Set WinScriptHost = Nothing
