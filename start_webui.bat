@echo off
chcp 65001 >nul
title Daily Stock Analysis - WebUI
cd /d "%~dp0"
echo 正在启动 Web 服务，请稍候...
echo 服务启动后可访问: http://127.0.0.1:8000
echo.
.\venv\Scripts\python.exe webui.py
pause
