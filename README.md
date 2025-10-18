# Mirrorium Navigation

一个简洁美观的项目导航页面，支持通过 Pull Request 添加新项目入口。

## 🚀 在线预览

访问 [Mirrorium Navigation](https://mirrorium.top) 查看效果。

## 📝 如何添加新项目

### 方法一：通过 Pull Request（推荐）

1. **Fork 本仓库**
2. **创建项目入口文件**
   - 在项目根目录创建一个 `.txt` 文件
   - 文件名将作为项目名称
   - 文件内容格式：
     ```
     项目链接
     项目简介
     ```
   
3. **添加项目图片**（可选）
   - 将图片文件放在项目根目录
   - 支持格式：`.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`
   - 图片文件名应与txt文件名相同

4. **提交 Pull Request**
   - 提交您的更改
   - 等待审核和合并

### 方法二：直接编辑

1. 在项目根目录创建txt文件
2. 运行生成脚本：
   ```bash
   python generate_navigation.py
   ```

## 📋 项目入口文件格式

### 文件命名
- 文件名：`项目名称.txt`
- 示例：`我的博客.txt`

### 文件内容
```
https://example.com
这是我的个人博客，分享技术文章和生活感悟
```

### 示例文件
```
橙猫猫博客预览页.txt
内容：
https://blog.mirrorium.top
这是一个关于编程技术和生活感悟的个人博客，记录我的学习成长历程
```

## 🖼️ 项目图片

### 图片要求
- **尺寸**：建议 400x300 像素或 16:9 比例
- **格式**：支持 JPG、PNG、GIF、WebP
- **大小**：建议不超过 2MB
- **命名**：与txt文件名相同（不含扩展名）

### 示例
```
橙猫猫博客预览页.txt
橙猫猫博客预览页.jpg
```

## 🎨 项目样式

### 默认样式
- 蓝色渐变背景
- 白色文字
- 圆角卡片设计

### 博客样式
- 橙色渐变背景
- 项目名称包含"博客"关键词时自动应用
- 特殊视觉效果

## 🛠️ 本地开发

### 环境要求
- Python 3.6+
- 无需额外依赖

### 运行步骤
1. 克隆仓库
2. 添加项目入口文件
3. 运行生成脚本：
   ```bash
   python generate_navigation.py
   ```
4. 打开 `index.html` 查看效果

## 📁 项目结构

```
Mirrorium_Navigation/
├── index.html              # 主页面
├── generate_navigation.py  # 生成脚本
├── README.md              # 说明文档
├── 项目名称.txt           # 项目入口文件
├── 项目名称.jpg           # 项目图片（可选）
└── ...                    # 其他项目文件
```

## 🤝 贡献指南

1. Fork 本仓库
2. 创建您的特性分支：`git checkout -b feature/新项目名称`
3. 添加项目入口文件和图片
4. 运行生成脚本确保格式正确
5. 提交更改：`git commit -m "添加新项目：项目名称"`
6. 推送分支：`git push origin feature/新项目名称`
7. 创建 Pull Request

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 项目主页：[Mirrorium](https://mirrorium.top)
- 邮箱：mirrorium@outlook.com
- 提交 Issue：[GitHub Issues](https://github.com/Mirrorium227/Mirrorium_Navigation)

---

⭐ 如果这个项目对您有帮助，请给个 Star 支持一下！
