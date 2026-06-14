import time
import asyncio

def fetch(name, seconds):
    print(f"Fetching {name}...")
    time.sleep(seconds)
    print(f"Finished fetching {name}.")

def main():
    time_start = time.time()
    fetch("DB start", 5)
    fetch("API call", 3)
    fetch("File read", 2)
    time_end = time.time()
    print(f"Total time: {time_end - time_start}")

print("Starting synchronous tasks")
main()

print("*******************************")
async def fetch_async(name, seconds):
    print(f"Fetching {name}...")
    await asyncio.sleep(seconds)
    print(f"Finished fetching {name}.")

async def main_async():
    time_start = time.time()
    await asyncio.gather(
        fetch_async("DB start", 5),
        fetch_async("API call", 3),
        fetch_async("File read", 2)
    )
    time_end = time.time()
    print(f"Total time: {time_end - time_start}")

print("Starting asynchronous tasks")
asyncio.run(main_async())


# OUTPUT Starting synchronous tasks
"""
Fetching DB start...
Finished fetching DB start.
Fetching API call...
Finished fetching API call.
Fetching File read...
Finished fetching File read.
Total time: 10.012988090515137
*******************************
Starting asynchronous tasks
Fetching DB start...
Fetching API call...
Fetching File read...
Finished fetching File read.
Finished fetching API call.
Finished fetching DB start.
Total time: 5.001688003540039
"""