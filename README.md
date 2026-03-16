# 长图切分工具 (Image Splitter)

一个功能完整的长图切分工具，提供命令行、Web应用和Skill三种使用方式。

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ 功能特点

- 🖼️ 支持多种图片格式（PNG、JPG、JPEG、WEBP、BMP）
- ⚡ 快速均匀切分算法
- 🎨 美观的Web界面
- 📦 批量下载（ZIP）
- 🤖 WorkBuddy Skill集成
- 💻 命令行工具

## 🚀 快速开始

### Web应用版本（推荐）

```bash
# 克隆仓库
git clone https://github.com/Drrreistein/split-image.git
cd split-image

# 安装依赖
cd web_app
pip install -r requirements.txt

# 启动应用
python app.py

# 访问 http://localhost:9000
```

### 命令行版本

```bash
# 安装依赖
pip install Pillow

# 使用
python split_image.py <图片路径> <切分数量>

# 示例
python split_image.py screenshot.png 5
```

## 📖 文档

- [Web应用使用指南](Web应用使用指南.md)
- [命令行使用说明](使用说明.md)
- [Skill安装指南](安装指南.md)
- [项目总览](项目总览.md)

## 🌐 在线演示

访问 Web 应用：http://localhost:9000

### Web应用功能

- 📤 拖拽上传
- 👁️ 实时预览
- ⚙️ 自定义切分数量
- 📦 ZIP批量下载
- 📱 响应式设计

## 📦 项目结构

```
split-image/
├── split_image.py          # 命令行工具
├── web_app/                # Web应用
│   ├── app.py             # Flask后端
│   ├── templates/         # 前端模板
│   └── requirements.txt   # 依赖列表
├── split-image-skill/      # WorkBuddy Skill
└── docs/                   # 文档
```

## 🛠️ 技术栈

- **后端**: Flask 3.0
- **图片处理**: Pillow (PIL)
- **前端**: HTML5 + CSS3 + JavaScript
- **设计**: 渐变色、响应式布局

## 📊 性能

- 支持文件大小：最大 50MB
- 切分范围：1-100张
- 处理速度：~1秒/10MB
- 支持格式：PNG、JPG、JPEG、WEBP、BMP

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 🙏 致谢

感谢使用长图切分工具！
