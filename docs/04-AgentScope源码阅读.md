# 04｜AgentScope 源码阅读：暂时只看 3 个文件

不要从头到尾读整个仓库。先运行完 02、03，再带着具体问题看源码。

> 以下路径按 AgentScope 2026-10-16 官方 main 分支核对。你本地克隆的 commit 可能不同，以本地实际文件为准。

## 第 1 个文件：Agent Loop

路径：`agentscope-source/src/agentscope/agent/_agent.py`

首先只找：

- `class Agent`
- `__init__` 中的 `model`、`toolkit`、`state`、`middlewares`
- `reply` 或 `reply_stream` 相关方法

**思考：** 模型第一次回复工具调用后，谁负责继续执行工具并把结果送回模型？

参考：[官方源码](https://github.com/agentscope-ai/agentscope/blob/main/src/agentscope/agent/_agent.py)

## 第 2 个文件：Tool 注册

路径：`agentscope-source/src/agentscope/tool/_toolkit.py`

搜索 `class Toolkit`。

**思考：** 工具的名称、参数 Schema、执行函数怎样被框架统一管理？

参考：[Toolkit 源码](https://github.com/agentscope-ai/agentscope/blob/main/src/agentscope/tool/_toolkit.py)

## 第 3 个文件：Python 函数如何变成 Tool

路径：`agentscope-source/src/agentscope/tool/_adapters.py`

搜索 `class FunctionTool`。

**思考：** Python 函数返回的 dict 是怎样转成框架的 ToolChunk / ToolResult 的？

参考：[FunctionTool 源码](https://github.com/agentscope-ai/agentscope/blob/main/src/agentscope/tool/_adapters.py)

## 小作业

在纸上或笔记中画出：

~~~text
User
  ↓
Agent.reply / reply_stream
  ↓
Model
  ↓ (tool call)
Toolkit → FunctionTool → summarize_sales
  ↓ (tool result)
Model
  ↓
Final answer
~~~

你能解释这个流程后，再考虑 Harness 的 Planner / Supervisor；否则容易陷入只会复制粘贴框架代码的状态。
