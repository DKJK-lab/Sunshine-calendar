; ============================================================
;  Sunshine - Always-on-top Reminder Popup (AutoHotkey v1)
;  Purpose: Show reminder window with "Stop Reminder" button
;           that syncs with the backend dismissal API.
; ============================================================

; ========== Read command-line arguments ==========
title := A_Args[1] ? A_Args[1] : "Reminder"
message := A_Args[2] ? A_Args[2] : ""
taskId := A_Args[3] ? A_Args[3] : ""

; ========== Window settings ==========
Gui, +AlwaysOnTop +ToolWindow -Caption +Border
Gui, Color, 1A1A1E

winW := 340
winH := 190

; --- Title ---
Gui, Font, s14 cWhite Bold, Segoe UI
Gui, Add, Text, x16 y10 w310 h28 Center, %title%

; --- Separator ---
Gui, Font, s10 cWhite, Segoe UI
Gui, Add, Text, x24 y44 w292 h1 0x7

; --- Message ---
Gui, Font, s12 cWhite Bold, Segoe UI
Gui, Add, Text, x16 y56 w308 h36 Center, %message%

; --- Stop Reminder button ---
Gui, Font, s12 cWhite Bold, Segoe UI
Gui, Add, Button, x110 y112 w120 h32 gStopReminder, Stop Reminder

; --- Drag background ---
Gui, Add, Text, x0 y0 w%winW% h%winH% gDragMove BackgroundTrans,

; ========== Show window ==========
Gui, Show, xCenter y150 w%winW% h%winH%, Reminder
WinSet, Transparent, 180, Reminder

; Auto-close after 60 seconds
SetTimer, AutoClose, 60000
Return

; ========== Event handlers ==========

StopReminder:
    Gui, Destroy
    RunWait, curl -X POST http://127.0.0.1:5678/dismiss -H "Content-Type: application/json" -d "{""taskId"":""%taskId%""}", Hide
    ExitApp
Return

AutoClose:
    Gui, Destroy
    RunWait, curl -X POST http://127.0.0.1:5678/dismiss -H "Content-Type: application/json" -d "{""taskId"":""%taskId%""}", Hide
    ExitApp
Return

DragMove:
    PostMessage, 0xA1, 2, 0, , A
Return

ExitSub:
    Gui, Destroy
    ExitApp
Return