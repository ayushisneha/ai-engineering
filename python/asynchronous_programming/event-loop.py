# Create own event loop with asyncio
# Create a co-routine and run it in using own event loop

import asyncio

# new event loop
loop = asyncio.new_event_loop()

#define task
task = asyncio.sleep(5)

#execute task in the event loop
loop.run_until_complete(task)

print("Task completed")