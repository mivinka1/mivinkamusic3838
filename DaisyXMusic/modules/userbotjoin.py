# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import asyncio

from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant

from DaisyXMusic.config import SUDO_USERS
from DaisyXMusic.helpers.decorators import authorized_users_only, errors
from DaisyXMusic.services.callsmusic import client as USER


@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Додайте мене до адміністраторів цієї групи</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "DaisyMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "Я приєднався сюди, як ви і просили")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Ассистент бот приєднався до вашого чату</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🔴 Flood Wait Error 🔴 \nUser {user.first_name} не вдалося приєднатися до вашої групи через багато спроб!Переконайтеся, що бот не заблокований у групі."         
            "\n\вручну додайте ассистента до своєї групи та повторіть спробу</b>",
        )
        return
    await message.reply_text(
        "<b>Ассистент бот приєднався до вашого чату</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>Користувач не може вийти з вашої групи!"
            "\n\nOr вручну видаліть мене з вашої групи</b>",
        )
        return


@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left = 0
        failed = 0
        lol = await message.reply("Ассистент залишив усі чати")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left + 1
                await lol.edit(
                    f"Ассистент виходить...: {left} chats. Помилка: {failed} chats."
                )
            except:
                failed = failed + 1
                await lol.edit(
                    f"Ассистент виходить...: {left} chats. Помилка: {failed} chats."
                )
            await asyncio.sleep(0.7)
        await client.send_message(
            message.chat.id, f"Left {left} chats. Помилка {failed} chats."
        )


@Client.on_message(
    filters.command(["userbotjoinchannel", "ubjoinc"]) & ~filters.private & ~filters.bot
)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
        conchat = await client.get_chat(message.chat.id)
        conid = conchat.linked_chat.id
        chid = conid
    except:
        await message.reply("Чат повязаний")
        return
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Додайте мене до адміністраторів цієї групи</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "DaisyMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "Я приєднався сюди, як ви і просили")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Ассистент бот приєднався до вашого чату</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
             f"<b>🔴 Flood Wait Error 🔴 \nUser {user.first_name} не вдалося приєднатися до вашої групи через багато спроб!Переконайтеся, що бот не заблокований у групі."
            "\n\вручну додайте ассистента до своєї групи та повторіть спробу</b>",
        )
        return
    await message.reply_text(
        "<b>Ассистент бот приєднався до вашого чату</b>",
    )
