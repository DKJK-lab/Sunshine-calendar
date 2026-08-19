# -*- coding: utf-8 -*-
"""
Sunshine Reminder Service (Flask)
Purpose: Receive reminder requests, launch AutoHotkey popup, provide sync dismiss API
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import threading
import os
import sys

app = Flask(__name__)
CORS(app)

# ============================================
# Configuration (please adjust to your system)
# ============================================

# Path to AutoHotkey executable (if in PATH, just "AutoHotkey.exe")
AHK_EXE = "AutoHotkey.exe"   # or "C:\Program Files\AutoHotkey\AutoHotkey.exe"

# Reminder script filename (must be in the same directory as server.py)
AHK_SCRIPT = "remind.ahk"

# ============================================

# Store active task IDs for sync dismissal
active_tasks = {}

@app.route('/remind', methods=['POST'])
def remind():
    """Receive reminder request and launch AHK popup"""
    data = request.json
    title = data.get('title', 'Reminder')
    message = data.get('message', '')
    task_id = data.get('taskId', '')

    if task_id:
        active_tasks[task_id] = True
        print(f'[Remind] Task {task_id} registered')

    threading.Thread(target=show_popup, args=(title, message, task_id)).start()
    return jsonify({'status': 'ok'})

@app.route('/dismiss', methods=['POST'])
def dismiss():
    """Dismiss reminder (called from frontend or AHK)"""
    data = request.json
    task_id = data.get('taskId', '')

    if task_id and task_id in active_tasks:
        active_tasks.pop(task_id, None)
        print(f'[Dismiss] Task {task_id} stopped')

    return jsonify({'status': 'ok'})

@app.route('/check', methods=['GET'])
def check():
    """Polling endpoint to check if task is still active"""
    task_id = request.args.get('taskId', '')
    if task_id and task_id not in active_tasks:
        return jsonify({'dismissed': True})
    return jsonify({'dismissed': False})

def show_popup(title, message, task_id):
    """Launch AutoHotkey popup window"""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ahk_script_path = os.path.join(script_dir, AHK_SCRIPT)

        subprocess.Popen([
            AHK_EXE,
            ahk_script_path,
            title,
            message,
            task_id
        ], shell=False)
        print(f'[Popup] AHK popup launched: {title}')
    except Exception as e:
        print(f'[Error] Failed to launch popup: {e}')

if __name__ == '__main__':
    print('☀️  Sunshine Reminder Service started')
    print('📡 Listening on port: 5678')
    print('🔄 Supported APIs: /remind, /dismiss, /check')
    print('⚠️  Please ensure AutoHotkey is installed and AHK_EXE is correct')
    app.run(host='127.0.0.1', port=5678, debug=False)