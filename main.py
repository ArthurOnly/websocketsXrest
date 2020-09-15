import asyncio
import websockets
from time import sleep
import json

async def websocketServer(websocket, path):
   async for message in websocket:
        request = json.loads(message)

        print(request)

        await websocket.send(json.dumps({"Recebido": "True"}))

server = websockets.serve(websocketServer,'localhost',4444)

asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
