# GitHub Pages 部署

## 🌐 访问地址

部署完成后，你的应用将可以通过以下地址访问：

```
https://drrreistein.github.io/split-image/
```

## 📦 纯前端版本特点

这个版本完全在浏览器中运行，无需服务器：

✅ **100% 客户端处理** - 图片不会上传到服务器
✅ **快速处理** - 本地Canvas API切分
✅ **隐私安全** - 数据不离开浏览器
✅ **免费托管** - GitHub Pages完全免费
✅ **HTTPS支持** - 自动SSL证书

## 🚀 自动部署

### 方式1：通过GitHub Actions自动部署

已配置自动部署，每次推送到main分支会自动更新GitHub Pages。

查看 `.github/workflows/deploy.yml` 配置。

### 方式2：手动启用GitHub Pages

1. 进入仓库 Settings
2. 点击左侧 "Pages"
3. Source 选择 "Deploy from a branch"
4. Branch 选择 "main"
5. Folder 选择 "/docs"
6. 点击 "Save"

等待几分钟，访问 https://drrreistein.github.io/split-image/

## 📁 文件结构

```
split-image/
├── docs/                    # GitHub Pages目录
│   └── index.html          # 纯前端应用
├── web_app/                 # Flask后端版本
├── .github/
│   └── workflows/
│       └── deploy.yml      # 自动部署配置
└── README.md
```

## 🔄 版本对比

| 特性 | GitHub Pages版 | Flask版 |
|------|---------------|---------|
| 需要服务器 | ❌ | ✅ |
| 隐私保护 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 处理速度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 大文件支持 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 免费使用 | ✅ | 取决于平台 |

## 🎯 使用建议

- **日常使用**: GitHub Pages版（免费、隐私、快速）
- **大文件处理**: Flask版（支持更大文件）
- **企业应用**: 自部署Flask版

## 🛠️ 技术栈

- **Canvas API** - 图片切分处理
- **JSZip** - ZIP打包下载
- **FileReader API** - 文件读取
- **Blob API** - 文件下载

## 📊 性能

- 小文件（<5MB）：即时处理
- 中等文件（5-20MB）：1-2秒
- 大文件（20-50MB）：3-5秒
- 最大支持：取决于浏览器内存

## 🔒 隐私保证

1. **零数据上传** - 所有处理在浏览器完成
2. **无服务器日志** - 没有服务器记录
3. **离线可用** - 加载后可离线使用
4. **开源透明** - 代码完全可见

---

**享受完全免费的在线长图切分服务！** 🎉
