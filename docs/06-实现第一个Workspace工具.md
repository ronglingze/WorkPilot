# Step 4｜自己写第一个 Workspace 工具

**目标只有一个：** 使用 Python 列出 `data/workspace/` 中的文件名。

此步骤还不调用 DeepSeek。先把工具写好并测试，下一步再注册到 AgentScope。

## 1. 同步最新代码

Linux 服务器终端，先退出 Agent 聊天窗口：

~~~bash
cd /home/ysk/WorkPilot
git pull --ff-only
~~~

如果提示本地有未提交的修改，先停下，不要执行 `git reset --hard`。

## 2. 查看示例数据

~~~bash
ls data/workspace
~~~

应看到：

~~~text
meeting_notes.md
q1_sales.csv
q2_sales.csv
~~~

这些是合成测试数据，不是真实企业文件。

## 3. 自己创建 Python 文件

在 VS Code 中新建：

`examples/workspace_tools.py`

输入下面的代码（建议自己敲一遍，理解每一行）：

~~~python
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[1] / "data" / "workspace"


def list_workspace_files() -> list[str]:
    """List available files in the WorkPilot demo workspace."""
    return sorted(p.name for p in WORKSPACE.iterdir() if p.is_file())


if __name__ == "__main__":
    print(list_workspace_files())
~~~

这里用固定目录，**不要让模型任意指定操作系统路径**。后面加入动态文件操作时，需要专门设计路径校验与权限。

## 4. 独立测试

~~~bash
python examples/workspace_tools.py
~~~

预期看到：

~~~text
['meeting_notes.md', 'q1_sales.csv', 'q2_sales.csv']
~~~

出现这三个文件名就算成功。

## 5. 一句理解

`list_workspace_files` 是普通 Python 函数，还不是 Agent 工具。

下一步，我们会使用 AgentScope 的 `FunctionTool` / `Toolkit` 注册它，再让 DeepSeek 决定何时调用。

## 6. 完成后

把第 4 步的终端输出发给我。我们再做**工具注册**，一次只推进一步。
