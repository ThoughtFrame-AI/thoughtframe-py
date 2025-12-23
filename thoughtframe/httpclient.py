# thoughtframe/httpclient.py

import aiohttp

class HttpClient:
    async def post(self, inUrl, inPayload):
        async with aiohttp.ClientSession() as session:
            async with session.post(inUrl, json=inPayload) as resp:
                return await resp.json()

    async def get(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()
