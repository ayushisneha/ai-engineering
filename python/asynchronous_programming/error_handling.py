import asyncio

async def fetch(name, should_fail=False):
    print(f"Fetching data for {name}...")
    await asyncio.sleep(2)
    if should_fail:
        raise Exception(f"Failed to fetch data for {name}")
    print(f"Data fetched for {name}")
    return f"Task: {name}"

async def main():
    tasks = [
        asyncio.create_task(fetch("DB query")),
        asyncio.create_task(fetch("API call", should_fail=True)),
        asyncio.create_task(fetch("Cache update"))
    ]

    for task in tasks:
        try:
            result = await task
            print(result)
        except Exception as e:
            print(f"Error: {e}")

asyncio.run(main())

#OUTPUT
"""
Fetching data for DB query...
Fetching data for API call...
Fetching data for Cache update...
Data fetched for DB query
Data fetched for Cache update
Task: DB query
Error: Failed to fetch data for API call
Task: Cache update
"""