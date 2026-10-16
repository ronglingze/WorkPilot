# WorkPilot

面向长程知识工作的 Agent Harness 学习项目。

**现在只做第一阶段：理解 AgentScope 并跑通一个安全、只读的工具调用。**
先不要开发 Planner、Supervisor、Memory 或训练。

## 从这里开始

👉 [docs/00-先看这里.md](docs/00-%E5%85%88%E7%9C%8B%E8%BF%99%E9%87%8C.md)

学习顺序：

1. [00 先看这里](docs/00-%E5%85%88%E7%9C%8B%E8%BF%99%E9%87%8C.md)
2. [01 检查目录与安装环境](docs/01-%E6%A3%80%E6%9F%A5%E7%9B%AE%E5%BD%95%E4%B8%8E%E5%AE%89%E8%A3%85%E7%8E%AF%E5%A2%83.md)
3. [02 运行第一个 Agent](docs/02-%E8%BF%90%E8%A1%8C%E7%AC%AC%E4%B8%80%E4%B8%AAAgent.md)
4. [03 给 Agent 加第一个工具](docs/03-%E7%BB%99Agent%E5%8A%A0%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%B7%A5%E5%85%B7.md)
5. [04 AgentScope 源码阅读](docs/04-AgentScope%E6%BA%90%E7%A0%81%E9%98%85%E8%AF%BB.md)
6. [05 下一阶段的边界](docs/05-%E4%B8%8B%E4%B8%80%E9%98%B6%E6%AE%B5.md)

## 目录

- `agentscope-source/`：你本地克隆的官方源码，已被 Git 忽略。
- `docs/`：细粒度学习步骤。
- `examples/`：最小可运行示例。
- `data/`：练习数据。

官方源码：https://github.com/agentscope-ai/agentscope

**安全提醒：** API Key 只在你的终端环境变量里设置，不要提交到 GitHub。工具示例仅读取项目内固定的 CSV，不允许模型执行任意 Shell 命令。
