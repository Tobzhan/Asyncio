import aiohttp
import asyncio
from util.async_timed import async_timed
from aiohttp import ClientSession
from chapter_04 import fetch_status

# @async_timed()
# async def add_one(number: int) -> int:
#     return number + 1

# @async_timed()
# async def main() -> None:
#     one_plus_one = await add_one(1)
#     two_plus_one = await add_one(2)
#     print(one_plus_one)
#     print(two_plus_one)

# loop = asyncio.new_event_loop()

# try:
#     loop.run_until_complete(main())
# finally:
#     loop.close()

@async_timed()
async def main():
    # We create session where we will work / we can have till 100 connections by default but we can change it
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        status = await fetch_status(session, url)
        print(f"Status for {url} was {status}")

asyncio.run(main())

# assert loop.is_closed() == True, "Event loop is not closed"

