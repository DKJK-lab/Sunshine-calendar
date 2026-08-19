; ========== 向阳而生 · 置顶提醒弹窗（同步关闭版）==========
title := A_Args[1] ? A_Args[1] : "⏰ 到点提醒"
message := A_Args[2] ? A_Args[2] : ""
taskId := A_Args[3] ? A_Args[3] : ""

; 主窗口：始终置顶 + 无边框
Gui, +AlwaysOnTop +ToolWindow -Caption +Border
Gui, Color, 1A1A1E

; ---- 窗口尺寸 ----
winW := 340
winH := 190

; ----- 标题 -----
Gui, Font, s14 cWhite Bold, 微软雅黑
Gui, Add, Text, x16 y10 w310 h28 Center, %title%

; ----- 分隔线 -----
Gui, Font, s10 cWhite, 微软雅黑
Gui, Add, Text, x24 y44 w292 h1 0x7

; ----- 正文（加粗）-----
Gui, Font, s12 cWhite Bold, 微软雅黑
Gui, Add, Text, x16 y56 w308 h36 Center, %message%

; ----- 按钮：只保留“停止提醒”-----
Gui, Font, s12 cWhite Bold, 微软雅黑
Gui, Add, Button, x110 y112 w120 h32 gStopReminder, 停止提醒

; ----- 透明拖拽背景（整窗口拖动）-----
Gui, Add, Text, x0 y0 w%winW% h%winH% gDragMove BackgroundTrans,

; ----- 显示窗口 -----
Gui, Show, xCenter y150 w%winW% h%winH%, 提醒
WinSet, Transparent, 180, 提醒

; 60秒后自动关闭
SetTimer, AutoClose, 60000
Return

; ========== 事件处理 ==========

StopReminder:
    Gui, Destroy
    RunWait, curl -X POST http://127.0.0.1:5678/dismiss -H "Content-Type: application/json" -d "{\"taskId\":\"%taskId%\"}", , Hide
    ExitApp
Return

AutoClose:
    Gui, Destroy
    ExitApp
Return

DragMove:
    PostMessage, 0xA1, 2, 0, , A
Return

ExitSub:
    Gui, Destroy
    ExitApp
Return