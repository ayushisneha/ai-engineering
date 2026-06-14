import time
import asyncio

# non-cooperative example
# a only need value from b, but it has to wait for b to finish before it can continue its execution.
def a():
    value = b()
    print(value)

def b():
    time.sleep(10)
    return 5

a()

# cooperative example
# a can yield control to b while it is waiting for the value, allowing b to execute

async def x():
    value = await y()
    print(value)

async def y():
    await asyncio.sleep(10)
    return 5

async def main():
    await x()

# to execute a co-routine, we need an event-loop. 
asyncio.run(main())
