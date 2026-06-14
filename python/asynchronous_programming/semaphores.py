"""
Semaphores are a synchronization primitive used to control access to a shared resource in concurrent programming. 
They are often used to limit the number of threads or processes that can access a particular resource at the same time.

For 1000 users,
await asyncio.gather(*[fetch_data(user) for user in users]) 

-> 1000 simultaneous DB connections -> DB overload -> DB crash/performance degradation.

To prevent this, we can use a semaphore to limit the number of concurrent connections to the DB.

"""

import asyncio
import time

async def fetch_data(user, semaphore):
    async with semaphore: # acquire the semaphore before accessing the DB
        print(f"Fetching data for {user}...")
        await asyncio.sleep(2) # Simulate DB query
        print(f"Data fetched for {user}")

async def main():
    users = [f"User {i}" for i in range(10)]
    semaphore = asyncio.Semaphore(3) # Limit to 3 concurrent connections

    start_time = time.time()
    query = [fetch_data(user, semaphore) for user in users]
    await asyncio.gather(*query)
    end_time = time.time()
    print(f"Total time: {end_time - start_time}")

asyncio.run(main())

#OUTPUT
"""
Fetching data for User 0...
Fetching data for User 1...
Fetching data for User 2...
Data fetched for User 0
Data fetched for User 1
Data fetched for User 2
Fetching data for User 3...
Fetching data for User 4...
Fetching data for User 5...
Data fetched for User 3
Data fetched for User 4
Data fetched for User 5
Fetching data for User 6...
Fetching data for User 7...
Fetching data for User 8...
Data fetched for User 6
Data fetched for User 7
Data fetched for User 8
Fetching data for User 9...
Data fetched for User 9
Total time: 8.00529408454895
"""