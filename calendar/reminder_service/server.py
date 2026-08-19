from flask import Flask, request
from flask_cors import CORS
import subprocess
import threading
import os

app = Flask(__name__)
CORS(app)

# 存储当前活跃的任务ID（用于同步关闭）
active_tasks = {}

@app.route('/remind', methods=['POST'])
def remind():
    data = request.json
    title = data.get('title', '⏰ 提醒')
    message = data.get('message', '')
    task_id = data.get('taskId', '')
    
    if task_id:
        active_tasks[task_id] = True
        print(f'✅ 任务 {task_id} 已注册提醒')
    
    threading.Thread(target=show_popup, args=(title, message, task_id)).start()
    return {'status': 'ok'}

@app.route('/dismiss', methods=['POST'])
def dismiss():
    data = request.json
    task_id = data.get('taskId', '')
    
    if task_id and task_id in active_tasks:
        active_tasks.pop(task_id, None)
        print(f'🔕 任务 {task_id} 已停止提醒')
    
    return {'status': 'ok'}

@app.route('/check', methods=['GET'])
def check():
    task_id = request.args.get('taskId', '')
    if task_id and task_id not in active_tasks:
        return {'dismissed': True}
    return {'dismissed': False}

def show_popup(title, message, task_id):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ahk_script = os.path.join(script_dir, 'remind.ahk')
        subprocess.Popen([
            r'D:\AutoHotkey\AutoHotkey.exe',
            ahk_script,
            title,
            message,
            task_id
        ], shell=True)
    except Exception as e:
        print(f'弹窗失败: {e}')

if __name__ == '__main__':
    print('🚀 提醒服务已启动，监听端口 5678')
    print('📌 支持 /remind、/dismiss、/check 接口')
    app.run(host='127.0.0.1', port=5678, debug=False)