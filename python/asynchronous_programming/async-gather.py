import asyncio
import time

async def fetch(name, seconds):
    print (f"Fetching data for {name}...")
    await asyncio.sleep(seconds)
    print(f"Data fetched for {name}")
    return f"User: {name}"

async def main():

    #sequential execution
    print("Starting sequential execution")
    time_start = time.time()
    result1 = await fetch("Alice", 5)
    result2 = await fetch("Bob", 3)
    result3 = await fetch("Charlie", 2)
    results = [result1, result2, result3]
    time_end = time.time()
    print(f"Total time: {time_end - time_start}")
    print(results)

    print("*******************************")
    #parallel execution using asyncio.gather
    print("Starting parallel execution")
    time_start = time.time()
    results = await asyncio.gather(
        fetch("Alice", 5),
        fetch("Bob", 3),
        fetch("Charlie", 2)
    )
    time_end = time.time()
    print(f"Total time: {time_end - time_start}")
    print(results)

asyncio.run(main())

#OUTPUT
"""
Starting sequential execution
Fetching data for Alice...
Data fetched for Alice
Fetching data for Bob...
Data fetched for Bob
Fetching data for Charlie...
Data fetched for Charlie
Total time: 10.003726959228516
['User: Alice', 'User: Bob', 'User: Charlie']
*******************************
Starting parallel execution
Fetching data for Alice...
Fetching data for Bob...
Fetching data for Charlie...
Data fetched for Charlie
Data fetched for Bob
Data fetched for Alice
Total time: 5.001760959625244
['User: Alice', 'User: Bob', 'User: Charlie']
"""