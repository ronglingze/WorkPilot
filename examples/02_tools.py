"""WorkPilot Step 2: observe an AgentScope tool call (read-only)."""

import asyncio
import os

from agentscope.agent import Agent
from agentscope.console import launch_console
from agentscope.credential import OpenAICredential
from agentscope.model import OpenAIChatModel
from agentscope.permission import PermissionBehavior, PermissionDecision
from agentscope.tool import FunctionTool, Toolkit

from sales_tool import summarize_sales


async def main() -> None:
    api_key = os.environ.get("WORKPILOT_API_KEY")
    model_id = os.environ.get("WORKPILOT_MODEL")
    base_url = os.environ.get("WORKPILOT_BASE_URL") or None

    if not api_key or not model_id:
        raise RuntimeError(
            "请先设置 WORKPILOT_API_KEY 和 WORKPILOT_MODEL 环境变量。"
        )

    safe_read_only_tool = FunctionTool(
        func=summarize_sales,
        is_read_only=True,
        permission=PermissionDecision(
            behavior=PermissionBehavior.ALLOW,
            message="只读取 WorkPilot 项目内固定的销售示例 CSV。",
        ),
    )

    model = OpenAIChatModel(
        credential=OpenAICredential(api_key=api_key, base_url=base_url),
        model=model_id,
        stream=True,
    )
    agent = Agent(
        name="WorkPilot",
        system_prompt=(
            "你是 WorkPilot。当用户询问销售数据时，"
            "必须调用 summarize_sales 工具获取真实数值，"
            "不能猜测数据。请用中文回答。"
        ),
        model=model,
        toolkit=Toolkit(tools=[safe_read_only_tool]),
    )
    await launch_console(agent)


if __name__ == "__main__":
    asyncio.run(main())
