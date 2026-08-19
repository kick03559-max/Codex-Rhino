# Codex&Rhino 项目交接状态

> 更新时间：2026-08-19
> 
> 本地资料包：`D:\20260525\2026项目汇总\AIGC\CODEX\Codex&Rhino`

## 当前目标

整理本机 Codex + Rhino 7 + MCP 的完整连接配置、日常使用流程、参考图建模和 FHL 材质应用流程，并把当前圆形实木茶几项目、源码和教程集中到一个可继续维护的资料包中，随后上传到用户的 GitHub 账号。

## 已完成内容

- 已创建本地资料包目录 `Codex&Rhino`。
- 已整理本机真实配置：Rhino 7、`rhino7_mcp`、本地 STDIO、`127.0.0.1:9876`、Python 环境和 Rhino 侧脚本。
- 已复制 Rhino MCP 源码副本、依赖说明、许可证和启动脚本。
- 已整理视频路线与本机实际部署差异，明确视频的 RhinoAiMCP HTTP 路线不是本机最终路线。
- 已编写安装配置、日常操作、参考图建模与材质、故障排查、安全规则和 GitHub 维护文档。
- 已复制当前圆形实木茶几模型、白底产品图、FHL 原始木纹和桌腿竖向木纹。
- 未复制个人 Codex `config.toml`、FHL key、`.env` 实际配置或 Python 虚拟环境。

## 当前项目资产

```text
项目资产\圆形实木茶几_AI建模项目\
├─ 圆形实木茶几_木纹材质模型.3dm
├─ PROJECT_STATUS.md
├─ 参考图\圆形实木茶几_白底产品图.png
└─ 资产\
   ├─ 木纹材质_FHL原始.png
   └─ 木纹材质_桌腿竖向.png
```

## 关键技术决策

- Rhino 7 采用本地 STDIO MCP 桥接，不使用 OAuth；不要把 `http://localhost:3001/mcp` 的 RhinoAiMCP 配置直接套用到本机。
- Codex 配置使用 `command = '...reer-rhino-mcp.exe'`，写操作审批模式为 `writes`。
- Rhino 7 代码按 IronPython 2.7 编写，辅助函数和导入都放入同一个 `main()` 函数。
- 模型操作遵循“读取 → 规划 → 确认 → 执行 → 再读取验收 → 保存”的顺序。
- GitHub 资料包使用 `Codex&Rhino` 作为显示名称；建议 GitHub 仓库 slug 使用 `Codex-Rhino`。

## 测试结果

- 原画框模型：11 个 Brep，已保留。
- 茶几模型：4 个 Brep，已应用材质和纹理方向 UserText。
- Rhino 场景单位：毫米。
- 视口：已验证桌面木纹和桌腿竖向木纹显示。
- `.3dm`、参考图和材质图：均已复制到资料包并核对存在。
- 文档：README、5 个专题文档、配置模板均已生成。

## GitHub 上传状态

- 已在 `Codex&Rhino` 目录初始化 Git 仓库，分支为 `main`。
- 已完成敏感信息扫描，未发现 API key、私钥或实际 `.env` 配置；个人配置和虚拟环境已由 `.gitignore` 排除。
- GitHub 私有仓库：<https://github.com/kick03559-max/Codex-Rhino>
- 已通过 Git Credential Manager 完成浏览器授权并推送到 `origin/main`。
- 首次提交：`4caa7053ae735ed33ce0857e40b1d358a99e2c73`（`docs: add Codex and Rhino workflow package`）。
- 当前工作区已与 `origin/main` 同步；本机未安装 `gh` CLI，但不影响本次 Git 推送。

## 已知问题

- Rhino MCP 虚拟环境没有打包，换电脑需按安装文档重新创建。
- 配置模板含当前电脑的示例绝对路径，复制到其他电脑后必须修改。
- GitHub 仓库如果公开，模型和参考图会公开；建议默认创建私有仓库。
- 当前茶几模型尺寸为参考图估算值，不是实测生产尺寸。
- Rhino 7 标准材质以 `Shine=18/255` 近似中等粗糙度，不等同于完整 PBR roughness 通道。

## 下一步顺序

1. 在 GitHub 仓库首页确认 README、教程、源码和项目资产均可正常浏览或下载。
2. 后续所有相关文档、模型版本和材质资产继续放入 `Codex&Rhino` 目录。
3. 每次修改前后执行敏感信息检查，再提交并推送到 `main`；不要提交真实密钥、个人 `config.toml` 或虚拟环境。
4. 如需多人协作，再另行建立功能分支和 Pull Request 流程。
