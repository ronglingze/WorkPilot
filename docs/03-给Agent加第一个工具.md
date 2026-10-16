# 03｜给 Agent 加第一个工具（预计 20～30 分钟）

这一节要亲眼观察最重要的调用链：

**用户提问 → 模型决定调用工具 → Python 函数执行 → 工具结果返回模型 → 模型回答。**

## 1. 先不要连 API：验证纯 Python 逻辑

打开 `data/sales.csv`，里面是 3 条销售数据。

打开 `examples/sales_tool.py`。它只读取这一份固定 CSV，不允许 LLM 指定任意文件路径。

直接运行工具函数：

~~~bash
python -c "from examples.sales_tool import summarize_sales; print(summarize_sales())"
~~~

期望输出包含：

~~~text
'total': 3600
~~~

如果这一步失败，先修 Python 文件问题；**与模型和 API 无关**。

## 2. 打开 Agent 侧代码

打开 `examples/02_tools.py`，找到：

- `FunctionTool(func=summarize_sales, ...)`：把 Python 函数包装成可调用工具。
- `Toolkit(tools=[...])`：注册工具。
- `Agent(..., toolkit=toolkit)`：把工具交给 Agent。
- `launch_console(agent)`：观察工具调用与返回。

注意：这里显式地允许了**一个固定路径、只读的工具**；不是允许 Agent 执行任意代码、命令或写文件。

## 3. 运行 Agent

保持同一个终端的 API 环境变量：

~~~bash
python examples/02_tools.py
~~~

输入：

~~~text
请使用 summarize_sales 工具读取销售数据，告诉我总销售额和各地区金额，不要自己编造。
~~~

## 4. 观察

应当看到工具调用或相关调用事件，然后得到总销售额 **3600**。

如果模型直接猜测数值而没有调用工具，这一步不算通过。检查模型是否支持 Tool Calling，并明确要求调用工具；不同模型的遵循程度可能不同。

## 5. 做一个非常小的实验

修改 `data/sales.csv`：把 north 的 `1200` 改为 `1300`。

重新执行第 1 步，应该得到总额 **3700**。

再执行第 3 步，让模型重新调用工具。

这个实验的目的：证明数值来自外部工具，而不是写死在 System Prompt 里。

实验后可以用 `git diff` 查看你改过的文件；如果想恢复示例数据，请直接把 north 改回 `1200`，不要随手执行 `git reset --hard`。

## 6. 完成标准

- [ ] 不依赖 API，Python 工具独立返回 3600。
- [ ] LLM 成功调用工具，而不是猜测。
- [ ] CSV 数字改变后，模型答案随工具结果变化。
- [ ] 能用自己的话说出 LLM / Toolkit / Python Tool 的分工。

➡️ [04｜阅读 AgentScope 源码](04-AgentScope%E6%BA%90%E7%A0%81%E9%98%85%E8%AF%BB.md)
