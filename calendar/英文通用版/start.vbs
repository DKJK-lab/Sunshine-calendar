' ============================================================
'  Sunshine - One-click Launcher (Windows VBS)
'  Purpose: Silently start Python service + open calendar app
' ============================================================
'  ⚠️ Please modify the configuration variables below
'     to match your local environment.
' ============================================================

Set objShell = CreateObject("WScript.Shell")

' ========== Configuration (please edit these) ==========

' 1. Project folder (where server.py and index.html are located)
projectFolder = "D:\reminder_service"   ' change to your actual path

' 2. Python interpreter path (if python is in PATH, just "python.exe")
pythonExe = "python.exe"   ' or "C:\Python312\python.exe"

' 3. Calendar app path (if you have a Pake-built exe, specify its full path)
'    If you don't have an exe, comment out or delete this line
calendarApp = "D:\My calendar\pake-acalendar.exe"   ' change to your actual path

' ========== No changes needed below ==========

' Switch to project directory
objShell.CurrentDirectory = projectFolder

' Start Python service in background (hidden window)
objShell.Run pythonExe & " server.py", 0, False

' If calendar app is configured, launch it
If calendarApp <> "" Then
    objShell.Run calendarApp, 1, False
End If