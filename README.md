# Codex&Rhino

Codex 通过本地 MCP 驱动 Rhino 7 的完整配置、使用和项目资料包。

## 这个资料包包含什么

- 本机真实可用的 Rhino 7 + `rhino7_mcp` STDIO 连接方案。
- 从 Rhino 安装、Python/uv 环境、Rhino 侧脚本到 Codex 配置的完整操作步骤。
- Codex 连接后的只读检查、规划、执行、验收、保存和关闭流程。
- 参考图到 Rhino 白模，再到 FHL 木纹材质和 Rhino 映射的完整案例。
- 实际使用的 Rhino MCP 脚本、依赖文件和当前圆形实木茶几模型。
- 故障排查、安全边界、提示词模板和后续继续开发顺序。

## 先看哪几个文件

1. [本地安装与连接配置](文档/01_本地安装与连接配置.md)
2. [Codex + Rhino 日常使用教程](文档/02_Codex_Rhino日常操作教程.md)
3. [参考图建模与材质流程](文档/03_参考图建模与材质流程.md)
4. [故障排查与安全规则](文档/04_故障排查与安全规则.md)
5. [项目交接状态](PROJECT_STATUS.md)

## 本机已验证配置

| 项目 | 当前值 |
|---|---|
| Rhino | Rhino 7 |
| Rhino 可执行文件 | `D:\Program Files\Rhino 7\System\Rhino.exe` |
| Rhino 侧脚本 | `tools\rhino_mcp\rhino_script.py` |
| Python 环境 | `D:\20260525\2026项目汇总\AIGC\CODEX\tools\rhino_mcp_env` |
| Codex MCP 名称 | `rhino7_mcp` |
| 本地桥接端口 | `127.0.0.1:9876` |
| 认证方式 | 本地 STDIO，不使用 OAuth |
| 单位 | 毫米 |

## 当前案例资产

当前案例是圆形实木茶几：1200 mm 桌面直径、520 mm 总高、100 mm 桌面厚度、3 条直径 260 mm 的圆柱桌腿。模型、产品参考图、FHL 木纹材质和交接状态位于：

`项目资产\圆形实木茶几_AI建模项目\`

## 重要说明

视频展示的是 RhinoAiMCP + Claude Desktop 的 HTTP 路线；本机实际采用 Rhino 7 + `reer-ide/rhino_mcp` 本地 STDIO 桥接路线。不要把 `http://localhost:3001/mcp` 的配置直接套到当前 Rhino 7 环境。两条路线的原理相同，但连接端点和配置方式不同。

GitHub 上传时不要上传个人 `config.toml`、API key、`.env` 实际文件、浏览器登录信息或完整虚拟环境目录；本资料包只保留脱敏模板和必要源码。

