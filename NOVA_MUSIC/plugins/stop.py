from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from NOVA_MUSIC import app
from NOVA_MUSIC.core.call import NOVA
from NOVA_MUSIC.utils.database import set_loop
from NOVA_MUSIC.utils.decorators import AdminRightsCheck
from NOVA_MUSIC.utils.inline.play import close_keyboard

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await NOVA.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.first_name),
        reply_markup=close_keyboard,
    )
