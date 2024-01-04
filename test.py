import asyncio
from util.delay_functions import delay
from util.async_timed import async_timed

@async_timed()
async def add_one(number: int) -> int:
    return number + 1

@async_timed()
async def main() -> None:
    one_plus_one = await add_one(1)
    two_plus_one = await add_one(2)
    print(one_plus_one)
    print(two_plus_one)

loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()

assert loop.is_closed() == True, "Event loop is not closed"

