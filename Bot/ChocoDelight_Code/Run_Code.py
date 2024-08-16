import asyncio
from dotenv import load_dotenv

from Bot.ChocoDelight_Code.Commands import commands

load_dotenv()


async def main():
    print("Starting .......")
    from Hendlers import dp
    from Hendlers import bot
    await bot.set_my_commands(commands=commands)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
