# -*- coding: utf-8 -*-
"""
向阳而生 - 提醒服务 (Flask)
功能：接收前端提醒请求，调用 AutoHotkey 弹窗，提供同步关闭接口
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
# 配置区域（用户可根据实际情况修改）
# ============================================

# AutoHotkey 可执行文件路径（如果已经添加到 PATH，可以只写 "AutoHotkey.exe"）
AHK_EXE = "AutoHotkey.exe"   # 或 "C:\Program Files\AutoHotkey\AutoHotkey.exe"

# 提醒弹窗脚本文件名（与 server.py 在同一目录）
AHK_SCRIPT = "remind.ahk"

# ============================================

# 存储当前活跃的任务ID（用于同步关闭）
active_tasks = {}

@app.route('/remind', methods=['POST'])
def remind():
    """接收提醒请求，启动 AHK 弹窗"""
    data = request.json
    title = data.get('title', '到点提醒')
    message = data.get('message', '')
    task_id = data.get('taskId', '')

    if task_id:
        active_tasks[task_id] = True
        print(f'[提醒] 任务 {task_id} 已注册提醒')

    # 启动独立线程执行弹窗，避免阻塞
    threading.Thread(target=show_popup, args=(title, message, task_id)).start()
    return jsonify({'status': 'ok'})

@app.route('/dismiss', methods=['POST'])
def dismiss():
    """关闭提醒（前端或 AHK 调用）"""
    data = request.json
    task_id = data.get('taskId', '')

    if task_id and task_id in active_tasks:
        active_tasks.pop(task_id, None)
        print(f'[停止] 任务 {task_id} 已停止提醒')

    return jsonify({'status': 'ok'})

@app.route('/check', methods=['GET'])
def check():
    """轮询检查任务是否仍活跃"""
    task_id = request.args.get('taskId', '')
    if task_id and task_id not in active_tasks:
        return jsonify({'dismissed': True})
    return jsonify({'dismissed': False})

def show_popup(title, message, task_id):
    """调用 AutoHotkey 弹窗"""
    try:
        # 获取当前脚本所在目录
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ahk_script_path = os.path.join(script_dir, AHK_SCRIPT)

        # 启动 AHK 进程
        subprocess.Popen([
            AHK_EXE,
            ahk_script_path,
            title,
            message,
            task_id
        ], shell=False)
        print(f'[弹窗] 已启动 AHK 弹窗：{title}')
    except Exception as e:
        print(f'[错误] 弹窗启动失败：{e}')

if __name__ == '__main__':
    print('☀️  向阳而生提醒服务已启动')
    print('📡 监听端口: 5678')
    print('🔄 支持接口: /remind, /dismiss, /check')
    print('⚠️  请确保 AutoHotkey 已安装且 AHK_EXE 路径正确')
    app.run(host='127.0.0.1', port=5678, debug=False)