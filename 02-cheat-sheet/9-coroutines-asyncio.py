#!/usr/bin/env python

import asyncio


# A coroutine is typed like a normal function.
async def countdown(tag: str, count: int) -> None:
    while count > 0:
        print(f"T-minus {count} {tag}")
        await asyncio.sleep(0.3)
        count -= 1
    print("Blastoff!")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(countdown("seconds", 10))
