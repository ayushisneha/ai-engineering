import asyncio
import time

async def fetch(name, seconds):
    print(f"Fetching data for {name}...")
    await asyncio.sleep(seconds)
    print(f"Data fetched for {name}")
    return f"User: {name}"

async def main():
    start_time = time.time()

    # Task started and registered to event loop, but main continues to execute without waiting for the task to complete.
    task1 = asyncio.create_task(fetch("DB query", 5))
    task2 = asyncio.create_task(fetch("API call", 3))

    await asyncio.sleep(3) # Simulate doing other work while tasks are running
    print("Tasks created, main continues")

    result1 = await task1 # main will wait here until task1 is complete and result is available.
    result2 = await task2 

    end_time = time.time()
    print(f"Total time: {end_time - start_time}")
    print(f"Results: {result1}, {result2}")

asyncio.run(main())

#OUTPUT
"""
Fetching data for DB query...
Fetching data for API call...
Tasks created, main continues
Data fetched for API call
Data fetched for DB query
Total time: 5.00081205368042
Results: User: DB query, User: API call
"""

