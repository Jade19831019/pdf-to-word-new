# Cloudflare 部署指南

## 方案一：Cloudflare Pages + Workers

### 1. 部署静态页面到 Cloudflare Pages

```bash
# 安装 wrangler
npm install -g wrangler

# 登录
wrangler login

# 创建项目
wrangler pages project create pdf-to-word-new

# 部署
wrangler pages deploy ./ --project-name=pdf-to-word-new
```

### 2. 后端用 Cloudflare Workers

创建 `worker.js`:

```javascript
export default {
  async fetch(request, env, ctx) {
    return new Response('PDF to Word Converter!');
  },
};
```

部署：

```bash
wrangler deploy
```

## 方案二：Cloudflare Workers + R2 存储

更适合有后端处理的场景。

---

## 快速开始

1. 将项目推送到 GitHub，连接 Cloudflare Pages 自动部署。
