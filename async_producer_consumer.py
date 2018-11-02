import asyncio
import random

q = asyncio.Queue()


async def producer(num):
    while True:
        print('produced ')
        await q.put(num + random.random())
        await asyncio.sleep(random.random())

async def consumer(num):
    while True:
        value = await q.get()
        print('Consumed', num, value)

loop = asyncio.get_event_loop()

for i in range(6):
    loop.create_task(producer(i))

loop.create_task(consumer(1))

loop.run_forever()