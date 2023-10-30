import functools
import requests
import asyncio
from concurrent.futures import ProcessPoolExecutor


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        urls = ['https://www.google.com' for _ in range(1000)]
        tasks = [loop.run_in_executor(pool, functools.partial(get_status_code, urls))]
        results = await asyncio.gather(*tasks)
        print(results)

asyncio.run(main())

# script does not work