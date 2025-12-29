# thoughtframe/main.py

import asyncio
import sys 

from tf_core.bootstrap import configure, thoughtframe
from tf_core.web.webserver import BaseWebServer 

configure()

async def heartbeat():
    while True:
        print("heartbeat")
        await asyncio.sleep(5)


        
async def main():
    #asyncio.create_task(ml_task())
    # await asyncio.Event().wait()
    # if len(sys.argv) > 1:
    #     url = sys.argv[1]
    # else:
    #     # Corrected f-string syntax: use {} instead of ${}
    #     url = f"ws://localhost:8080/entermedia/services/websocket/org/thoughtframe/websocket/BenchConnection?sessionid={tabID}"
    #
    # # --- Delegation to the Managed Service ---
    #
    # # 1. Access the dedicated FrameConnection service
    tabID = "PythonConnection"
    url = NETWORK_CONFIG["websocket"]
    url = url.replace("{tabID}", tabID)
    
    connection_service = thoughtframe.connection
    #
   
   
    
    # 2. Start the connection. This method owns the async with block, 
    #    keepalive, and message consumption loop.
    await connection_service.start(url)

# 3. Run the application
asyncio.run(main())