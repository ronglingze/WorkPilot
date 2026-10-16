"""WorkPilot Step 1: use an API model with AgentScope, without tools."""

import asyncio
import os

from agentscope.agent import Agent
from agentscope.console import launch_console
from agentscope.credential import OpenAICredential
from agentscope.model import OpenAIChatModel


async def main() -> None:
    api_key = os.environ.get("WORKPILOT_API_KEY")
    model_id = os.environ.get("WORKPILOT_MODEL")
    base_url = os.environ.get("WORKPILOT_BASE_URL") or None

    if not api_key or not model_id:
        raise RuntimeError(
            "请先设置 WORKPILOT_API_KEY 和 WORKPILOT_MODEL 环境变量。"
        )

    model = OpenAIChatModel(
        credential=OpenAICredential(api_key=api_key, base_url=base_url),
        model=model_id,
        stream=True,
    )
    agent = Agent(
        name="WorkPilot",
        system_prompt="你是 WorkPilot。请用简洁中文回答问题。",
        model=model,
    )
    await launch_console(agent)


if __name__ == "__main__":
    asyncio.run(main())
