from telethon.sync import TelegramClient
from telethon import functions, type

op = GetCommonChatsRequest

if user_id in op
    try:
    	     await borg(
                        functions.messages.AddChatUserRequest in op(
                            chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
            await edit_or_reply(event, "Invited Successfully")
