' ============================================================
'  向阳而生 - 一键启动脚本（Windows VBS）
'  功能：静默启动 Python 提醒服务 + 打开日历应用
' ============================================================
'  ⚠️ 使用前请根据你的电脑环境修改下面的配置变量
' ============================================================

Set objShell = CreateObject("WScript.Shell")

' ========== 配置区域（请修改为你的实际路径） ==========

' 1. 项目文件夹路径（包含 server.py 和 index.html 的目录）
projectFolder = "D:\reminder_service"   ' 改为你的实际路径

' 2. Python 解释器路径（如果 python 已在 PATH 中，可以只写 "python.exe"）
pythonExe = "python.exe"   ' 或 "C:\Python312\python.exe"

' 3. 日历应用路径（如果你已经用 Pake 打包了 exe，填它的完整路径）
'    如果没有 exe，可以注释掉或删除下面这行
calendarApp = "D:\My calendar\pake-acalendar.exe"   ' 改为你的实际路径

' ========== 以下代码无需修改 ==========

' 切换到项目目录
objShell.CurrentDirectory = projectFolder

' 后台启动 Python 服务（隐藏窗口）
objShell.Run pythonExe & " server.py", 0, False

' 如果配置了日历应用，则打开它
If calendarApp <> "" Then
    objShell.Run calendarApp, 1, False
End If

' 结束