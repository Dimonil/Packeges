import asyncio
import aiohttp
import sys
import logging


stop = False


if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def foo(url, timeout=60):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=timeout) as responce:
            if not stop:

                r_json = await responce.json()
                try:
                    return r_json['temperatureC']
                except :
                    message = f'Ошибка по указанному  url:{url}'
                    logging.warning(message)
                    return 'нет данных'



async def get_temp_list(arr, timeout=60):
    if not stop:

        responce_list = await asyncio.gather(*[foo(url, timeout) for url in arr])
        return responce_list
    else:
        return


def main(arr, timeout=60):
    return asyncio.run(get_temp_list(arr, timeout))





