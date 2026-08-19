text

---

## 📄 `README.en.md`

```markdown
# ☀️ Sunshine Calendar · Desktop Daily Planner

> An all-in-one productivity tool featuring calendar, to-do list, subtasks, progress ring, memo, and desktop reminders.  
> Supports **bidirectional reminder sync**: closing any popup (page/AHK) will automatically close the other.

---

## ✨ Features

- 📅 **Calendar Dashboard**: Today / Inbox / Growth / Shiguang views
- ✅ **Parent-Child Tasks**: Subtask support with automatic progress calculation
- 📝 **Memo**: Markdown support with live preview
- 🎨 **Theme Switcher**: Dark/Light mode + 16 theme colors
- ⏰ **Reminders**: Recurring alerts with bidirectional sync (page ↔ system popup)
- 🖼️ **Custom Background**: Upload images as glass-morphism background
- 🔍 **Zoom**: 50%~200% scaling

---

## 📁 Project Files

| File | Description |
| :--- | :--- |
| `index.html` | Main calendar interface (HTML + CSS + JS all-in-one) |
| `server.py` | Python reminder service (Flask backend) |
| `start.vbs` | Windows one-click launcher (starts service + app silently) |
| `remind.ahk` | AutoHotkey always-on-top popup script (optional) |

---

## 🔧 Configuration Guide (must read before use)

> ⚠️ This project requires you to configure 3 files with your local paths.

### 1. Configure `start.vbs` (one-click launcher)

Open `start.vbs` with Notepad and modify these 3 variables:

```vbs
' ★★★ #1: Change to your project folder path ★★★
projectFolder = "D:\reminder_service"   ' change to your actual path

' ★★★ #2: If python.exe is not in system PATH, use full path ★★★
pythonExe = "python.exe"   ' or "C:\Python312\python.exe"

' ★★★ #3: If you have a calendar exe, set its full path; if not, delete this line ★★★
calendarApp = "D:\My calendar\pake-acalendar.exe"   ' change to your actual path
Example (if your project is on E drive):
Environment Setup & Installation
1. Python Environment (Required)
Python 3.8 or higher is required

Install dependencies (run in command line):

bash
pip install flask flask-cors
2. AutoHotkey (Optional)
If you need the system-level always-on-top popup feature, you need to install AutoHotkey v1

After installation, make sure remind.ahk is in the same directory as server.py

3. Port Configuration
The Python service runs on 127.0.0.1:5678 by default

If port 5678 is occupied, you can change it in the last line of server.py

4. One-Click Launch Script (Windows)
Edit start.vbs and change the following paths to match your system:

vbs
projectFolder = "D:\reminder_service"   ' Change to your project path
pythonExe = "python.exe"                ' Or full path like "C:\Python312\python.exe"
calendarApp = "D:\My calendar\pake-acalendar.exe"  ' Change to your app path
5. Running the Application
Method	Action	Use Case
Method 1 (Recommended)	Double-click start.vbs (after configuration)	One-click start: service + app
Method 2	Run python server.py, then open index.html	Full features with reminders
Method 3	Open index.html directly in browser	Web-only version, no reminders
📦 Quick Start (TL;DR)
bash
# 1. Install dependencies
pip install flask flask-cors

# 2. Start the reminder service
python server.py

# 3. Open index.html in your browser
# (or double-click start.vbs for one-click launch)
💡 Pro Tip: Create requirements.txt
For better compatibility, create a requirements.txt file in your project root:

text
flask
flask-cors
Then users can install all dependencies with a single command:

bash
pip install -r requirements.txt


vbs
projectFolder = "E:\my_projects\reminder_service"
pythonExe = "E:\Python314\python.exe"
calendarApp = "E:\calendar\pake-acalendar.exe"
2. Configure server.py (optional)
If your AutoHotkey installation path differs, modify this variable:

python
# Around line 17
AHK_EXE = "AutoHotkey.exe"   # or "C:\Program Files\AutoHotkey\AutoHotkey.exe"
3. Configure remind.ahk (optional)
If curl is not in system PATH, use full path:

autohotkey
RunWait, "C:\Windows\System32\curl.exe" -X POST ...
🚀 How to Run
Method	Action	Use Case
Method 1 (recommended)	Double-click start.vbs (after configuration)	One-click start: service + app
Method 2	Run python server.py, then double-click index.html	Full features with reminders
Method 3	Double-click index.html directly	Web-only version, no reminders
📦 Install Dependencies
bash
pip install flask flask-cors
⚠️ Troubleshooting
Issue	Solution
Double-clicking start.vbs does nothing	Check if projectFolder path is correct
Error "System cannot find the file specified"	Verify pythonExe and calendarApp paths
Python service fails to start	Port 5678 may be occupied; change port in server.py
Reminder popup doesn't appear	Ensure AutoHotkey is installed and AHK_EXE path is correct
📝 Notes
Data is stored in browser localStorage. Clearing browser cache will erase all data — export backups regularly.

Python service listens on 127.0.0.1:5678 by default. Ensure the port is available.

Special thanks to the [Pake](https://github.com/tw93/Pake) project for providing the open-source packaging tool that allows me to easily package this project's web code into a cross-platform desktop application. Pake is an excellent and user-friendly open-source project, recommended to anyone who wants to quickly package web pages into desktop apps.

This project uses Pake solely as a packaging tool, does not modify its source code, and complies with Pake's open-source license.
Copyright © 2026 DKJK

This software is licensed under the following terms:

**Personal Use & Learning License**
- ✅ Permitted: Personal learning, research, and non-commercial use
- ✅ Permitted: Viewing, forking, and modifying source code (for personal learning only)
- ✅ Permitted: Using modified code for personal purposes

**Commercial Use Restrictions**
- ❌ Prohibited: Any commercial use of this software or its derivatives
- ❌ Prohibited: Selling, renting, or reselling this software
- ❌ Prohibited: Integrating this software into commercial products or services
- ❌ Prohibited: Providing paid services or technical support based on this software

For commercial use authorization, please contact the author for written permission.

**Disclaimer**
This software is provided "as is", without any express or implied warranties. In no event shall the author be liable for any direct, indirect, incidental, special, or consequential damages arising out of the use of this software.

Contact: 731766303@qq.com
