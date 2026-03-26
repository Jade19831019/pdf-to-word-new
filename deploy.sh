#!/bin/bash
# Cloudflare Pages 部署脚本

echo "🚀 开始部署 PDF to Word 工具..."

# 1. 创建静态文件目录
mkdir -p static

# 2. 复制前端文件
cp templates/index.html static/
echo "✅ 前端文件已复制"

# 3. 检查 wrangler 是否安装
if ! command -v wrangler &> /dev/null; then
    echo "📦 安装 wrangler..."
    npm install -g wrangler
fi

# 4. 提示登录
echo ""
echo "🔑 请登录 Cloudflare:"
echo "运行: wrangler login"
echo ""

# 5. 提示部署命令
echo "🌐 登录后运行以下命令部署:"
echo "wrangler pages deploy static --project-name=pdf-to-word-new"
echo ""
echo "✅ 准备工作完成！"
