# thoughtframe/router.py

import inspect
from tf_core.modules.BaseFrameModule import BaseFrameModule


class BaseFrameRouter:
    def __init__(self, module_manager):
        self._modules = module_manager

    # -------------------------------------------------
    # Core resolution + validation
    # -------------------------------------------------
    def _resolve(self, inMsg):
        command = inMsg.get("command")
        if not command or "." not in command:
            raise ValueError(f"Invalid command format: {command}")

        module_name, method_name = command.split(".", 1)

        module = self._modules.get(module_name)
        if module is None:
            raise LookupError(f"Module not found: {module_name}")

        if not isinstance(module, BaseFrameModule):
            raise TypeError(
                f"Registered module '{module_name}' "
                f"is not a BaseFrameModule"
            )

        handler = getattr(module, method_name, None)
        if handler is None or not callable(handler):
            raise LookupError(
                f"Command not found: {module_name}.{method_name}"
            )

        # Enforce EXACTLY ONE parameter
        sig = inspect.signature(handler)
        params = list(sig.parameters.values())

        if len(params) != 1:
            raise TypeError(
                f"{module_name}.{method_name} must accept exactly "
                f"one argument (request)"
            )

        p = params[0]
        if p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD):
            raise TypeError(
                f"{module_name}.{method_name} "
                f"may not use *args or **kwargs"
            )

        return handler

    # -------------------------------------------------
    # Asynchronous dispatch ONLY
    # -------------------------------------------------
    async def dispatch(self, inMsg):
        handler = self._resolve(inMsg)

        result = handler(inMsg)

        if inspect.isawaitable(result):
            return await result

        return result
