import asyncio
import time
from service import get_user_summary

async def main():
    sem = asyncio.Semaphore(3) # limit concurrent DB access to 3
    start_time = time.time()

    results = await asyncio.gather(
        *[get_user_summary(i, sem) for i in range(1, 11)],
        return_exceptions=True, # to handle exceptions without stopping the entire execution
    )

    for r in results:
        if isinstance(r, Exception):
            print(f"Error: {r}")
        else:
            print(f"{r['name']} - {r['status']}")

    end_time = time.time()
    print(f"Total time: {end_time - start_time}")

asyncio.run(main())

#OUTPUT
"""
Alice - normal
Bob - normal
Charlie - normal
David - normal
Eve - normal
Frank - normal
Grace - normal
Heidi - normal
Ivan - rich
Judy - rich
Total time: 4.024118185043335
"""