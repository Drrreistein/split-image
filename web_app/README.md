# 长图切分 Web 应用

一个简洁美观的 Web 应用，用于将长图均匀切分成多张图片。

## ✨ 功能特点

- 🖼️ **支持多种格式**: PNG、JPG、JPEG、WEBP、BMP
- 📊 **实时预览**: 上传后即可预览原图和信息
- ⚙️ **灵活配置**: 自定义切分数量（1-100）
- 📦 **批量下载**: 支持打包下载所有切分结果（ZIP）
- 🎨 **美观界面**: 现代化渐变设计，响应式布局
- 📱 **移动友好**: 支持手机和平板设备访问
- 🚀 **简单易用**: 拖拽上传，一键切分

## 🛠️ 技术栈

- **后端**: Flask (Python)
- **图片处理**: Pillow (PIL)
- **前端**: HTML5 + CSS3 + JavaScript
- **设计**: 响应式布局，渐变主题

## 📦 安装步骤

### 方法1：使用启动脚本（推荐）

```bash
# 进入应用目录
cd web_app

# 添加执行权限
chmod +x start.sh

# 运行启动脚本
./start.sh
```

启动脚本会自动：
1. 检查 Python 环境
2. 安装所需依赖
3. 启动 Web 服务

### 方法2：手动安装

```bash
# 安装依赖
pip install -r requirements.txt

# 启动应用
python app.py
```

### 方法3：使用虚拟环境

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt

# 启动应用
python app.py
```

## 🚀 使用方法

1. **启动应用**后，在浏览器中访问：`http://localhost:5000`

2. **上传图片**：
   - 点击上传区域选择文件
   - 或直接拖拽图片到上传区域

3. **设置参数**：
   - 输入切分数量（1-100）
   - 查看图片预览和基本信息

4. **开始切分**：
   - 点击"开始切分"按钮
   - 等待处理完成

5. **下载结果**：
   - 单独下载每张图片
   - 或打包下载所有图片（ZIP）

## 📁 项目结构

```
web_app/
├── app.py                 # Flask 后端应用
├── requirements.txt       # Python 依赖
├── start.sh              # 启动脚本（macOS/Linux）
├── README.md             # 项目文档
├── templates/
│   └── index.html        # 前端页面
├── uploads/              # 上传文件临时目录（自动创建）
└── outputs/              # 切分结果目录（自动创建）
```

## ⚙️ 配置说明

在 `app.py` 中可以修改以下配置：

```python
# 最大上传文件大小（默认50MB）
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

# 服务器端口（默认5000）
app.run(port=5000)

# 允许的文件格式
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'webp', 'bmp'}
```

## 🔒 安全特性

- 文件类型验证
- 文件大小限制
- 安全的文件名处理
- 路径遍历保护

## 📱 设备支持

- ✅ 桌面浏览器（Chrome、Firefox、Safari、Edge）
- ✅ 移动浏览器（iOS Safari、Android Chrome）
- ✅ 平板设备

## 🐛 常见问题

### 1. 端口被占用
```
错误: Address already in use
解决: 修改 app.py 中的端口号，如 app.run(port=5001)
```

### 2. 依赖安装失败
```
错误: ModuleNotFoundError: No module named 'flask'
解决: pip install flask pillow
```

### 3. 文件上传失败
```
检查:
- 文件大小是否超过50MB
- 文件格式是否支持
- 网络连接是否正常
```

## 🔧 开发模式

启动调试模式：

```python
# 在 app.py 中设置
app.run(debug=True, host='0.0.0.0', port=5000)
```

## 📝 更新日志

### v1.0.0 (2024-03-16)
- ✅ 初始版本发布
- ✅ 支持拖拽上传
- ✅ 实时预览
- ✅ 批量下载
- ✅ 响应式设计

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📞 支持

如有问题或建议，请查看项目文档或提交 Issue。
