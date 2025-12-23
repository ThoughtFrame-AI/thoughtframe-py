import json
from typing import Protocol, Any

# ------------------------------------------
# 1. Define a Protocol FIRST (the interface)
# ------------------------------------------

class FrameRouter(Protocol):
    async def dispatch(self, inMsg: Any, inState: Any, inWs: Any):
        ...


# ------------------------------------------
# 2. Define your concrete router
# ------------------------------------------

class BaseFrameRouter:
    def __init__(self, inModuleManager):
        self.field_module_manager = inModuleManager

    async def dispatch(self, inMsg, inState, inWs):
        cmd = inMsg.get("command")
        if not cmd:
            return

        handlerName = f"handler_{cmd}"

        try:
            handler = self.field_module_manager.get(handlerName)
        except KeyError:
            return

        try:
            response = await handler(inMsg, inState)
        except Exception as e:
            err = {
                "command": "error",
                "error": str(e),
                "original_command": cmd
            }
            await inWs.send(json.dumps(err))
            return

        if response:
            await inWs.send(json.dumps(response))
