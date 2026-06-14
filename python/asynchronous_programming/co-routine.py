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


# coroutine example : coroutine -> promise to return a value in the future. fn can continue its execution and do other work while waiting for the other fn to return the value.
# doesnt start until await is called.

async def fetch():
    print ("Fetching data...")
    await asyncio.sleep(5)
    print("Data fetched")
    return "User: ABC"

async def main():
    print("Starting co-routine")
    result = await fetch()
    print("Co-routine completed") # This will execute after fetch is done and result is available.
    print(result)

# to execute a co-routine, we need an async event-loop. asyncio.run creates this event loop.
asyncio.run(main())

#OUTPUT
"""
5
Starting co-routine
Fetching data...
Data fetched
Co-routine completed
User: ABC
"""