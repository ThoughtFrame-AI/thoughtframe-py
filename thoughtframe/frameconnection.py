# thoughtframe/frameconnection.py
import asyncio
import json
import websockets

class FrameConnection:
    """Manages the lifecycle and state of the WebSocket connection."""
    
    def __init__(self, manager):
        self._manager = manager
        self._ws = None  # Holds the active connection object
        self.router = self._manager.get("router") # Access router once on init
        
    async def start(self, url: str):
        """Connects and starts the message consumption loop."""
        print(f"Connecting to: {url}")
        
        # The core connection management happens here
        async with websockets.connect(url) as ws:
            self._ws = ws
            
            asyncio.create_task(self.keepalive())
            
            # Initial handshake
            await ws.send(json.dumps({
                "command": "python_hello",
                "catalogid": "system",
                "message": "Hello from Python"
            }))
            
            # Start message consumption loop
            await self.consume_messages()

    async def keepalive(self):
        """Sends periodic keepalive frames."""
        while self._ws:
            try:
                await self._ws.send("keepalive")
            except:
                return # Exit gracefully on failure
            await asyncio.sleep(10)
    
    async def consume_messages(self):
        """Handles message reception and dispatch."""
        async for msg in self._ws:
            parsed = json.load(msg)
            # Delegate to the router service
            await self.router.dispatch(parsed, None, self._ws)