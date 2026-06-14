import asyncio

# Context manager example using async with. 
# This is useful for managing resources like database connections, file handles, etc. 
# It ensures that resources are properly acquired and released, even if an error occurs.


# without async_with, if error occurs while fetching data, the session will not be closed properly, leading to resource leaks.
# like here session never resets to None if error occurs while fetching data.
# This is dangerous because it can lead to resource leaks. DB connection remain open, connection pool will get exhausted and app will crash.
"""
async def get_data():
    session = "DB session opened"
    print(session)

    result = await asyncio.sleep(1)

    raise ValueError("An error occurred while fetching data")

    session = None
"""

# asnc-with -> cleanup happen even if error occur, without async-with cleanup is skipped if error. 
class DBSession:
    async def __aenter__(self):
        self.session = "DB session opened"
        print(self.session)
        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.session = None
        print("DB session closed")

async def get_data_safe():
    async with DBSession() as session:
        print(session)
        await asyncio.sleep(1)
        raise ValueError("An error occurred while fetching data")

asyncio.run(get_data_safe())