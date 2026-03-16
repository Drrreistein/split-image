#!/bin/bash

echo "正在启动长图切分 Web 应用..."
echo ""

# 检查 Python 版本
if command -v python3 &> /dev/null; then
    PYTHON=python3
elif command -v python &> /dev/null; then
    PYTHON=python
else
    echo "错误: 未找到 Python，请先安装 Python 3.6+"
    exit 1
fi

# 检查是否安装了依赖
if ! $PYTHON -c "import flask" &> /dev/null; then
    echo "正在安装依赖..."
    $PYTHON -m pip install -r requirements.txt
fi

echo ""
echo "======================================"
echo "  长图切分工具 Web 应用"
echo "======================================"
echo ""
echo "访问地址: http://localhost:5000"
echo "按 Ctrl+C 停止服务"
echo ""

# 启动应用
$PYTHON app.py
