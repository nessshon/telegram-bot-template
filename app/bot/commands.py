from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


async def setup(bot: Bot):
    commands = {
        "en": [
            BotCommand("start", "Restart"),
        ],
        "ru": [
            BotCommand("start", "Перезапустить"),
        ]
    }

    await bot.set_my_commands(
        commands=commands["ru"],
        scope=BotCommandScopeAllPrivateChats(),
        language_code="ru"
    )
    await bot.set_my_commands(
        commands=commands["en"],
        scope=BotCommandScopeAllPrivateChats(),
    )


def register(dp: Dispatcher):
    ...
