@echo off
chcp 65001 >nul
echo 🔍 正在更新导航页面...
python generate_navigation.py
echo.
echo ✅ 更新完成！按任意键退出...
pause >nul
