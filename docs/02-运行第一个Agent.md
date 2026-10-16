# 02｜运行第一个 Agent（预计 10～20 分钟）

这一节只验证 **LLM API → AgentScope Agent → 终端输出**，暂时不给 Agent 任何工具。

## 1. 打开示例代码

VS Code 打开 `examples/01_chat.py`。先看四行导入：

- `Agent`：AgentScope 的 Agent。
- `OpenAIChatModel`：OpenAI Chat Completions 及部分兼容 API 的适配器。
- `OpenAICredential`：API 凭据。
- `launch_console`：官方交互式终端入口。

示例使用当前 AgentScope 2.x 的 `Agent` API；不要混用早期教程的 `ReActAgent`。

## 2. 配置 API（只在当前终端设置，不写进仓库）

选择**兼容 OpenAI Chat Completions 和 tool_calls 格式**的模型供应商。你需要知道三个值：

- `WORKPILOT_API_KEY`：真实密钥。
- `WORKPILOT_MODEL`：供应商提供的具体模型 ID。
- `WORKPILOT_BASE_URL`：兼容 API 的基础 URL；直接使用 OpenAI 官方 API 可以不设置。

Windows PowerShell：

~~~powershell
$env:WORKPILOT_API_KEY="你的真实密钥"
$env:WORKPILOT_MODEL="你的模型ID"
$env:WORKPILOT_BASE_URL="服务商给出的兼容API地址"
~~~

macOS / Linux：

~~~bash
export WORKPILOT_API_KEY="你的真实密钥"
export WORKPILOT_MODEL="你的模型ID"
export WORKPILOT_BASE_URL="服务商给出的兼容API地址"
~~~

例如使用阿里百炼兼容接口时，其文档一般提供类似 `https://dashscope.aliyuncs.com/compatible-mode/v1` 的地址；如果使用其他供应商，**以其官方文档为准**，不要照抄示例 URL。

**不要在截图、Issues、聊天或 Git 提交里粘贴 API Key。**

## 3. 运行

先确认终端位于 WorkPilot 根目录，且虚拟环境已激活：

~~~bash
python examples/01_chat.py
~~~

在聊天终端输入：

~~~text
你好，请只用一句话介绍你自己。
~~~

## 4. 预期结果

终端出现来自模型的回答；使用 `exit` 或 `quit` 退出。

这里只验证网络、凭据、模型和 AgentScope 能够工作。**没有工具调用，也不是我们最终的 Harness。**

## 5. 排错

- `KeyError: WORKPILOT_API_KEY`：环境变量没有在当前终端设置。
- `401`：密钥不正确或权限问题。
- `404/model not found`：模型 ID / 基础 URL 不匹配。
- `429`：额度或请求频率限制。
- `ModuleNotFoundError: agentscope`：返回第 01 节确认已安装在虚拟环境。
- 提供商不支持当前 Chat Completions 请求格式：需要更换兼容模型或改用 AgentScope 的对应原生模型适配器。

## 6. 下一步

➡️ [03｜给 Agent 加第一个工具](03-%E7%BB%99Agent%E5%8A%A0%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%B7%A5%E5%85%B7.md)
