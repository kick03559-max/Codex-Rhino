# GitHub 上传与后续维护

## 1. 上传范围

推荐上传：

- `README.md`；
- `文档/`；
- `配置模板/`；
- `rhino_mcp/` 中的源码、依赖说明和许可证；
- `项目资产/` 中的当前模型、参考图和材质图。

不要上传：

- `C:\Users\<用户名>\.codex\config.toml` 原文件；
- FHL 或其他服务的 API key；
- `.env` 实际配置；
- `tools\rhino_mcp_env` 完整虚拟环境；
- 浏览器 Cookie、登录缓存或个人凭证。

## 2. 推荐命名

资料包显示名称为 `Codex&Rhino`。GitHub 仓库实际名称建议使用 `Codex-Rhino`，因为仓库 URL 使用连字符更稳妥；README 标题和本地资料包仍保留 `Codex&Rhino`。

## 3. 使用 GitHub CLI 上传

本流程需要 GitHub CLI `gh` 和一个已登录的 GitHub 账号。检查：

```powershell
gh --version
gh auth status
```

未登录时：

```powershell
gh auth login
```

按提示选择 GitHub.com、HTTPS 和浏览器登录。登录完成后重新执行 `gh auth status`。

## 4. 初始化本地仓库

在资料包根目录执行：

```powershell
cd "D:\20260525\2026项目汇总\AIGC\CODEX\Codex&Rhino"
git init
git branch -M main
git add README.md 文档 配置模板 rhino_mcp 项目资产 PROJECT_STATUS.md
git status --short
git commit -m "docs: add Codex and Rhino workflow package"
```

提交前必须检查 `git status --short`，确认没有出现密钥、`.env` 实际文件或完整虚拟环境。

## 5. 创建和上传仓库

如果账号中还没有仓库：

```powershell
gh repo create Codex-Rhino --private --source=. --remote=origin --push
```

如果用户希望公开发布，把 `--private` 改为 `--public`；涉及模型、参考图和材质资产时，默认建议私有仓库。

如果仓库已经存在：

```powershell
git remote add origin https://github.com/<用户名>/Codex-Rhino.git
git push -u origin main
```

## 6. 后续更新

每次新增模型或文档后：

```powershell
git status --short
git add <明确的文件或目录>
git commit -m "docs: update Codex Rhino workflow"
git push
```

不要使用没有检查范围的 `git add -A`，除非确认整个工作区的所有变更都属于该仓库。

