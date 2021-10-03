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

from DaisyXMusic.config import ASSISTANT_NAME, PROJECT_NAME


class Messages:
    START_MSG = "**Привіт 👋 [{}](tg://user?id={})!**\n\n🤖 Я бот, для відтворення музики в голосових чатах Telegram.\n\n✅ Надішли /help для більш детальної інформації."
    HELP_MSG = [
        ".",
        f"""
**Ей 👋 Ласкаво просимо назад {PROJECT_NAME}

⚪️ {PROJECT_NAME} може відтворювати музику в голосовому чаті вашої групи, а також голосовому чаті каналу

⚪️ Імя Ассистента >> @{ASSISTANT_NAME}\n\nНатисніть далі, щоб отримати інструкції**
""",
        f"""
**Налаштування**

1) Видайте боту адмінку
2) Почніть голосовий чат
3) Впишіть /play [назва пісні]
*) Якщо бот приєднався то насолоджуйтеся музикою, Якщо не додати @{ASSISTANT_NAME} до вашого чату повторіть ще раз

**Для відтворення музики каналу**
1) Видайте боту адмінку
2) Надішліть /userbotjoinchannel  у зв'язаній групі
3) Тепер надсилайте команди у зв'язаній групі
""",
        f"""
**Команди**

**=>> Song Playing 🎧**

- /play: Відтворення медіа чату
- /play [yt url] : Відтворення за ссилкою YouTube
- /splay: Відтворення пісні через jio saavn
- /ytplay: Відтворювати пісню через Youtube Music

**=>> Відтворення ⏯**

- /player: Відкрити меню налаштувань програвача
- /skip: Пропустити поточний трек
- /pause: Призупинити трек
- /resume: Відновлення призупиненого треку
- /end: Припинення відтворення медіафайлів
- /current: Показати поточний трек
- /playlist: Показати плейлист

""",
        f"""
**=>> Відтворення музики каналу 🛠**

⚪️ Лише для адміністраторів зв'язаних груп:

- /cplay [назва пісні] - Відтворення
- /csplay [назва пісні] - Відтворення через jio saavn
- /cplaylist - Показати список відтворення
- /cccurrent - Показати що зараз відтворюється
- /cplayer - відкрити панель налаштувань музичного програвача
- /cpause - призупинити відтворення пісні
- /cresume - відновити відтворення пісні
- /cskip - відтворити наступну пісню
- /cend - зупинити відтворення музики
- /userbotjoinchannel - Добавити ассистента у ваш чат

⚪️ Якщо ви не любите слухати у пов'язаній групі:

1) Отримайте ID каналу.
2) Створіть групу з титлою: Музика каналу: your_channel_id
3) Добавте бота як адміністратора з усіма правами
4) Добавте @{ASSISTANT_NAME} каналу як адміністратору.
5) Просто надсилайте команди у своїй групі. (не забувайте використовувати /ytplay instead /play)
""",
        f"""
**=>> Більше налаштуваннь 🧑‍🔧**

- /musicplayer [on/off]: Увімкнення або вимкнення музичного програвача
- /admincache: Оновлення адмінів у вашому чаті, якщо бот не розпізнає адміністратора
- /userbotjoin: Запросити @{ASSISTANT_NAME} бота до вашого чату
""",
        f"""
**=>> Завантаження пісні 🎸**

- /video [назва пісні]: Завантажити відео пісню з YouTube
- /song [назва пісні]:  Завантажити аудіо пісню з YouTube
- /saavn [назва пісні]: Завантажити пісню з saavn
- /deezer [назва пісні]: Завантажити пісню з deezer

**=>> Засоби пошуку 📄**

- /search [назва пісні]: Пошук пісень на YouTube
- /lyrics [назва пісні]: Отримати текст пісні
""",
        f"""
**=>> Команди для користувачів Sudo ⚔️**

 - /userbotleaveall - видалити помічника з усіх чатів
 - /broadcast <реплей> - глобально трансльоване повідомлення усім чатам
 - /pmpermit [on/off] - увімкнути/вимкнути повідомлення у приватні повідомлення
*Користувачі Sudo можуть виконувати будь-яку команду в будь-яких групах

""",
    ]
