Set objShell = CreateObject("WScript.Shell")
objShell.CurrentDirectory = "D:\reminder_service"
objShell.Run "python.exe server.py", 0, False
objShell.Run "pake-acalendar.exe", 1, False