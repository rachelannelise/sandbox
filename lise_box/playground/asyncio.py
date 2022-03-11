# %%
import asyncio

loop = asyncio.get_event_loop()
loop.call_soon(lambda: print("Hello World"))
loop.call_later(30, lambda: print("Hello World"))
loop.run_forever()

async def func():
    await ...