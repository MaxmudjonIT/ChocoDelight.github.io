import asyncio
from dotenv import load_dotenv

load_dotenv()


async def main():
    print("Starting .......")
    from Hendlers import dp
    from Hendlers import bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
