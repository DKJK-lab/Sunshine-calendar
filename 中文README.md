# ☀️ 向阳而生 · 桌面日历

> 一款集日历、待办任务、子任务、进度环、备忘录、桌面提醒于一体的效率工具。  
> 支持**双向同步提醒**：关闭任意一个弹窗（页面/AHK），另一个自动同步关闭。

---

## ✨ 主要功能

- 📅 **日历看板**：今日 / 待办箱 / 成长记录 / 拾光 四大视图
- ✅ **父子任务**：支持子任务拆分，进度自动计算
- 📝 **备忘录**：支持 Markdown 语法，实时预览
- 🎨 **主题换肤**：深色/浅色模式 + 16 种主题色自由切换
- ⏰ **到点提醒**：循环提醒 + 双向同步关闭（页面弹窗 ↔ 系统置顶弹窗）
- 🖼️ **自定义背景**：支持上传图片作为窗口毛玻璃背景
- 🔍 **内容缩放**：50%~200% 自由缩放

---

## 📁 项目文件说明

| 文件 | 作用 |
| :--- | :--- |
| `index.html` | 日历主界面（HTML + CSS + JavaScript 全合一） |
| `server.py` | Python 提醒服务（基于 Flask） |
| `start.vbs` | Windows 一键启动脚本（静默启动服务 + 打开应用） |
| `remind.ahk` | AutoHotkey 置顶弹窗脚本（可选） |

---

## 🔧 配置指南（使用前必读）

> ⚠️ 本项目包含 3 个需要配置路径的文件，请按以下步骤操作。

### 1. 配置 `start.vbs`（一键启动脚本）

用记事本打开 `start.vbs`，修改以下 3 处：

```vbs
' ★★★ 第1处：改为你的项目文件夹路径 ★★★
projectFolder = "D:\reminder_service"   ' 改为你的实际路径

' ★★★ 第2处：如果你的 python.exe 不在系统 PATH 中，改为完整路径 ★★★
pythonExe = "python.exe"   ' 或 "C:\Python312\python.exe"

' ★★★ 第3处：如果你有日历 exe，改为完整路径；如果没有，删除这行 ★★★
calendarApp = "D:\My calendar\pake-acalendar.exe"   ' 改为你的实际路径
🔧 环境配置与安装
1. Python 环境（必须）
需要 Python 3.8 或更高版本
安装依赖包（在命令行中执行）：
bash
pip install flask flask-cors
2. AutoHotkey（可选）
如果你需要使用系统置顶弹窗功能，需要安装 AutoHotkey v1
安装后，确保 remind.ahk 与 server.py 在同一目录下
3. 端口占用
Python 服务默认运行在 127.0.0.1:5678
如果 5678 端口被占用，请在 server.py 最后一行修改端口号


示例（假设你的项目在 E 盘）：
projectFolder = "E:\my_projects\reminder_service"
pythonExe = "E:\Python314\python.exe"
calendarApp = "E:\calendar\pake-acalendar.exe"
2. 配置 server.py（可选）
如果你的 AutoHotkey 安装路径不同，修改以下变量：
python
# 第 17 行附近
AHK_EXE = "AutoHotkey.exe"   # 或 "C:\Program Files\AutoHotkey\AutoHotkey.exe"
3. 配置 remind.ahk（可选）
如果 curl 不在系统 PATH 中，将 curl 改为完整路径：
autohotkey
RunWait, "C:\Windows\System32\curl.exe" -X POST ...


⚠️ 常见问题
问题	解决方法
双击 start.vbs 没反应	检查 projectFolder 路径是否正确
报错“系统找不到指定的文件”	检查 pythonExe 和 calendarApp 路径是否正确
Python 服务启动失败	检查端口 5678 是否被占用，在 server.py 中修改端口号
提醒弹窗不显示	确认 AutoHotkey 已安装，且 AHK_EXE 路径正确


📝 注意事项
数据存储在浏览器 localStorage 中，清除浏览器缓存会导致数据丢失，请定期导出备份。

Python 服务默认监听 127.0.0.1:5678，请确保端口未被占用。

感谢 [Pake](https://github.com/tw93/Pake) 项目提供的开源打包工具，让我能够将本项目的网页代码轻松打包为跨平台桌面应用。Pake 是一个优秀且易用的开源项目，推荐给所有希望将网页快速打包为桌面应用的朋友。

本项目仅将 Pake 作为打包工具使用，未修改其源代码，且遵守 Pake 的开源协议。
版权所有 © 2026 DKJK

本软件采用以下许可证：

**个人使用与学习许可**
- ✅ 允许：个人学习、研究、非商业用途的使用
- ✅ 允许：查看、Fork、修改源代码（仅供个人学习）
- ✅ 允许：将修改后的代码用于个人使用

**商业使用限制**
- ❌ 禁止：将本软件或其衍生版本用于任何商业用途
- ❌ 禁止：售卖、租赁、转售本软件
- ❌ 禁止：将本软件集成到商业产品或服务中
- ❌ 禁止：利用本软件提供付费服务或技术支持

如需商业使用授权，请联系作者获得书面许可。

**免责声明**
本软件按“原样”提供，不提供任何明示或暗示的担保。在任何情况下，作者均不对因使用本软件而产生的任何直接、间接、偶然、特殊或后果性损害承担责任。

联系方式：731766303@qq.com
