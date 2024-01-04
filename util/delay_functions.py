import asyncio

# Template
async def delay(delay_seconds):
    print(f"Sleep for {delay_seconds} s")
    await asyncio.sleep(delay_seconds)
    print(f"Woke up after {delay_seconds} s")
    return delay_seconds