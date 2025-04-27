import asyncio
from aiohttp import ClientSession
from datetime import datetime
from utils import log_to_file

# Daftar situs yang akan dimonitor
WEBSITES = [
    "https://openai.com",
    "https://example.com",
    "https://github.com",
    "https://google.com",
    "https://youtube.com"
]

async def check_website(session, url):
    try:
        async with session.get(url) as response:
            status = response.status
            now = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            message = f"{now} {url} - Status: {status}"
            if status != 200:
                message += "      SITE DOWN!\a"  # Bonus: bunyi notifikasi
            print(message)
            log_to_file(message)
    except Exception as e:
        now = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        message = f"{now} {url} - ERROR: {e}\a"
        print(message)
        log_to_file(message)

async def monitor_websites():
    async with ClientSession() as session:
        while True:
            tasks = [check_website(session, url) for url in WEBSITES]
            await asyncio.gather(*tasks)
            await asyncio.sleep(10)  # Tunggu 10 detik

if __name__ == "__main__":
    asyncio.run(monitor_websites())
