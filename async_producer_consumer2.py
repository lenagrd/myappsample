import asyncio
import random


q = asyncio.Queue()


async def consume(queue):
    while True:
        item = await queue.get()
        print(item)




async def producer(num):
    while True:
        await queue.put(num + random.random())
        await asyncio.sleep(random.random())





#################
loop = asyncio.get_event_loop()
queue = asyncio.Queue()


# Consumer task
consumer = asyncio.ensure_future(consume(queue))


tasks = [
    asyncio.ensure_future(producer(1)),
    asyncio.ensure_future(producer(2))]
loop.run_until_complete(asyncio.wait(tasks))


# for i in range(6):
#     loop.create_task(producer(i))


# Wait until the connection is closed
loop.run_forever()
# Wait until the queue is empty
loop.run_until_complete(queue.join())
# Cancel the consumer
consumer.cancel()
# Let the consumer terminate
loop.run_until_complete(consumer)
# Close the loop
loop.close()