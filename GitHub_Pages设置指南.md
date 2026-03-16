# GitHub Pages 设置指南

## ⚠️ 如果Actions成功但网站无法访问

工作流显示成功，但网站还没上线，需要手动启用GitHub Pages。

## 🔧 手动设置步骤

### 步骤1：进入仓库设置

1. 访问你的仓库：https://github.com/Drrreistein/split-image
2. 点击 **Settings**（设置）标签
3. 在左侧菜单找到 **Pages**

### 步骤2：配置GitHub Pages

在 Pages 设置页面：

**Build and deployment** 部分：

1. **Source**: 选择 "GitHub Actions"（推荐）
   - 如果看到 "Deploy from a branch"，切换为 "GitHub Actions"
   - 这会使用我们创建的 `.github/workflows/deploy.yml`

**或者使用传统方式**：

1. **Source**: 选择 "Deploy from a branch"
2. **Branch**: 选择 "main"
3. **Folder**: 选择 "/docs"
4. 点击 **Save**

### 步骤3：等待部署

- 保存后，GitHub会自动开始部署
- 通常需要1-3分钟
- 页面会显示部署状态和访问链接

### 步骤4：访问网站

部署完成后，访问地址：

```
https://drrreistein.github.io/split-image/
```

## 📊 检查部署状态

### 方法1：查看Actions

1. 点击仓库的 **Actions** 标签
2. 查看最新的workflow运行
3. 点击进入查看详细日志

### 方法2：查看Pages设置

1. Settings → Pages
2. 查看顶部的部署状态
3. 会显示类似：
   ```
   Your site is live at https://drrreistein.github.io/split-image/
   ```

## 🐛 常见问题

### 问题1：显示 "Page build failed"

**原因**: 可能是docs目录或index.html有问题

**解决**: 检查文件是否存在
```bash
ls -la docs/
# 应该看到 index.html
```

### 问题2：网站显示404

**原因**: Pages未正确启用或还在部署中

**解决**:
1. 确认Settings → Pages中已正确配置
2. 等待几分钟让部署完成
3. 清除浏览器缓存重试

### 问题3：Actions成功但网站不更新

**原因**: 浏览器缓存或CDN延迟

**解决**:
1. 强制刷新：Ctrl+Shift+R (Windows) 或 Cmd+Shift+R (Mac)
2. 使用隐私模式访问
3. 等待5-10分钟让CDN更新

### 问题4：无法选择 "GitHub Actions"

**原因**: 仓库权限或旧版GitHub界面

**解决**:
- 使用 "Deploy from a branch" 方式
- Branch: main, Folder: /docs

## 📋 完整检查清单

- [ ] docs/index.html 文件存在
- [ ] Settings → Pages 已配置
- [ ] Actions 显示成功
- [ ] 等待1-3分钟
- [ ] 访问 https://drrreistein.github.io/split-image/

## 🎯 快速验证

在终端运行：

```bash
# 检查docs目录
cd /Users/a1-6/WorkBuddy/20260312221420
ls -la docs/

# 应该看到：
# index.html

# 检查git状态
git status

# 如果有未推送的更改
git add .
git commit -m "Update"
git push
```

## 📸 预期的设置界面

在 Settings → Pages 页面，你应该看到：

```
Build and deployment
  Source: GitHub Actions

Your site is published at https://drrreistein.github.io/split-image/
```

## 🔄 重新部署

如果需要手动触发重新部署：

### 方法1：推送新提交
```bash
git commit --allow-empty -m "Trigger redeploy"
git push
```

### 方法2：在Actions页面手动触发
1. Actions → "Deploy to GitHub Pages"
2. 点击 "Run workflow"

### 方法3：在Pages设置重新保存
1. Settings → Pages
2. 更改任何设置后保存
3. 再改回来并保存

## ✅ 成功标志

当一切正常时，你会看到：

1. **Actions页面**: 绿色的 ✓ 标记
2. **Pages设置**: "Your site is live at..."
3. **网站访问**: 显示长图切分工具界面

---

**按照以上步骤设置后，你的网站应该就能正常访问了！**
