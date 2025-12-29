from aiohttp import web

class BaseWebServer:
    def __init__(self, manager, cfg: dict):
        self._manager = manager
        self._router = manager.get("router")

        self._host = cfg.get("host", "127.0.0.1")
        self._port = cfg.get("port", 15001)

        self._app = web.Application()
        self._app.router.add_post("/dispatch", self._handle_request)
        self._app.router.add_get("/dispatch", self._handle_request)

        self._runner = None
        self._site = None

    @classmethod
    def from_config(cls, manager, cfg: dict):
        return cls(manager, cfg)

    async def start(self):
        self._runner = web.AppRunner(self._app)
        await self._runner.setup()
        self._site = web.TCPSite(self._runner, self._host, self._port)
        await self._site.start()

    async def stop(self):
        if self._runner:
            await self._runner.cleanup()

    async def _handle_request(self, request):
        payload = await request.json()
        result = await self._router.dispatch(payload)
        return web.json_response(result)

  
