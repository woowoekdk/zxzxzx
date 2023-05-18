import telethon
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -

# -

sython1.start()
sython2.start()
sython3.start()
sython4.start()
sython5.start()


c = requests.session()
bot_username = '@zmmbot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'

LOGS = logging.getLogger(__name__)
DEVS = [5159123009]


async def join_channel():
    try:
        await sython(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass


@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@d3boot_7"))
    except BaseException:
        pass
        
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@DzDDDD"))
    except BaseException:
        pass
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@botbillion"))
    except BaseException:
        pass
        
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@fvvvv"))
    except BaseException:
        pass

@sython2.on(events.NewMessage)

async def join_channel(event):

    try:

        await sython2(JoinChannelRequest("@d3boot_7"))

    except BaseException:

        pass

        

        

@sython2.on(events.NewMessage)

async def join_channel(event):

    try:

        await sython2(JoinChannelRequest("@DzDDDD"))

    except BaseException:

        pass

        

@sython2.on(events.NewMessage)

async def join_channel(event):

    try:

        await sython2(JoinChannelRequest("@botbillion"))

    except BaseException:

        pass

        

        

@sython2.on(events.NewMessage)

async def join_channel(event):

    try:

        await sython2(JoinChannelRequest("@fvvvv"))

    except BaseException:

        pass
        
@sython3.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython3(JoinChannelRequest("@d3boot_7"))
    except BaseException:
        pass
        
        
@sython3.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython3(JoinChannelRequest("@DzDDDD"))
    except BaseException:
        pass
        
@sython3.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython3(JoinChannelRequest("@botbillion"))
    except BaseException:
        pass
        
        
@sython3.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython3(JoinChannelRequest("@fvvvv"))
    except BaseException:
        pass


@sython4.on(events.NewMessage)

async def join_channel(event):

    try:

        await sython4(JoinChannelRequest("@d3boot_7"))

    except BaseException:

        pass

        

        

@sython4.on(events.NewMessage)

async def join_channel(event):

    try:

        await sython4(JoinChannelRequest("@DzDDDD"))

    except BaseException:

        pass

        

@sython4.on(events.NewMessage)

async def join_channel(event):

    try:

        await sython4(JoinChannelRequest("@botbillion"))

    except BaseException:

        pass

        

        

@sython4.on(events.NewMessage)

async def join_channel(event):

    try:

        await sython4(JoinChannelRequest("@fvvvv"))

    except BaseException:

        pass
        
@sython5.on(events.NewMessage)

async def join_channel(event):

    try:

        await sython5(JoinChannelRequest("@d3boot_7"))

    except BaseException:

        pass

        

        

@sython5.on(events.NewMessage)

async def join_channel(event):

    try:

        await sython5(JoinChannelRequest("@DzDDDD"))

    except BaseException:

        pass

        

@sython5.on(events.NewMessage)

async def join_channel(event):

    try:

        await sython5(JoinChannelRequest("@botbillion"))

    except BaseException:

        pass

        

        

@sython5.on(events.NewMessage)

async def join_channel(event):

    try:

        await sython5(JoinChannelRequest("@fvvvv"))

    except BaseException:

        pass
        
        
@sython1.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')

@sython2.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')


@sython3.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')


@sython4.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')

@sython5.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')

@sython1.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 مرحبا بك في قائمة اوامر حساب المسؤل

• @ZMMBOT -` /point1`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`**""")

@sython2.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 مرحبا بك في قائمة اوامر حساب المسؤل

• @ZMMBOT -` /point1`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`**""")

@sython3.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 مرحبا بك في قائمة اوامر حساب المسؤل

• @ZMMBOT -` /point1`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`**""")


@sython4.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 مرحبا بك في قائمة اوامر حساب المسؤل

• @ZMMBOT -` /point1`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`**""")

@sython5.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 مرحبا بك في قائمة اوامر حساب المسؤل

• @ZMMBOT -` /point1`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`**""")





@sython1.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**〠 مرحبا بك في قائمة اوامر حساب المسؤل

• @ZMMBOT - `/point1`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`**""")


@sython2.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**〠 مرحبا بك في قائمة اوامر حساب المسؤل

• @ZMMBOT - `/point1`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`**""")


@sython3.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**〠 مرحبا بك في قائمة اوامر حساب المسؤل

• @ZMMBOT - `/point1`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`**""")

@sython4.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**〠 مرحبا بك في قائمة اوامر حساب المسؤل

• @ZMMBOT - `/point1`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`**""")


@sython1.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗬𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗦𝗔𝗬𝗧𝗛𝗢𝗡𝗛    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟬 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗛𝗨𝗦𝗔𝗠.𝗙𝗔  ※

╰───⌯𝗦𝗬𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

@sython1.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython1.get_entity(bot_username)
        await sython1.send_message('@zmmbot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython1.get_entity(bot_username)
        await sython1.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython1.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython1.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع !")

@sython1.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython1.get_entity(bot_usernamee)
        await sython1.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython1.get_entity(bot_usernamee)
        await sython1.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython1.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython1.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع !")
      
  
@sython1.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython1.get_entity(bot_usernameee)
        await sython1.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython1.get_entity(bot_usernameee)
        await sython1.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython1.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython1.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython1.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython1.get_entity(bot_usernameeee)
        await sython1.send_message('@xnsex21bot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython1.get_entity(bot_usernameeee)
        await sython1.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython1.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython1.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython1.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython1.get_entity(bot_username)
        await sython1.send_message('@zmmbot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython1.get_entity(bot_username)
        await sython1.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython1.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython1.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython1.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع الجوكر"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython1.get_entity(bot_usernamee)
        await sython1.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython1.get_entity(bot_usernamee)
        await sython1.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython1.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython1.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython1.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العرب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython1.get_entity(bot_usernameeee)
        await sython1.send_message('@xnsex21bot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython1.get_entity(bot_usernameeee)
        await sython1.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython1.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython1.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع !")



@sython1.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العقاب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython1.get_entity(bot_usernameee)
        await sython1.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython1.get_entity(bot_usernameee)
        await sython1.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython1.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython1.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع !")



##########################################

@sython2.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗬𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗦𝗔𝗬𝗧𝗛𝗢𝗡𝗛    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟬 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗛𝗨𝗦𝗔𝗠.𝗙𝗔  ※

╰───⌯𝗦𝗬𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

@sython2.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython2.get_entity(bot_username)
        await sython2.send_message('@zmmbot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython2.get_entity(bot_username)
        await sython2.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython2.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython2.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython2(ImportChatInviteRequest(bott))
                msg2 = await sython2.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython2.send_message(event.chat_id, "تم الانتهاء من التجميع !")

@sython2.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython2.get_entity(bot_usernamee)
        await sython2.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython2.get_entity(bot_usernamee)
        await sython2.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython2.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython2.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython2(ImportChatInviteRequest(bott))
                msg2 = await sython2.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython2.send_message(event.chat_id, "تم الانتهاء من التجميع !")
      
  
@sython2.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython2.get_entity(bot_usernameee)
        await sython2.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython2.get_entity(bot_usernamee)
        await sython2.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython2.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython2.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython2(ImportChatInviteRequest(bott))
                msg2 = await sython2.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython2.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython2.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython2.get_entity(bot_usernameeee)
        await sython2.send_message('@xnsex21bot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython2.get_entity(bot_usernameeee)
        await sython2.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython2.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython2.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython2(ImportChatInviteRequest(bott))
                msg2 = await sython2.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython2.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython2.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython2.get_entity(bot_username)
        await sython2.send_message('@zmmbot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython2.get_entity(bot_username)
        await sython2.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython2.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython2.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython2(ImportChatInviteRequest(bott))
                msg2 = await sython2.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython2.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython2.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع الجوكر"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython2.get_entity(bot_usernamee)
        await sython2.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython2.get_entity(bot_usernamee)
        await sython2.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython2.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython2.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython2(ImportChatInviteRequest(bott))
                msg2 = await sython2.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython2.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython2.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العرب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython2.get_entity(bot_usernameeee)
        await sython2.send_message('@xnsex21bot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython2.get_entity(bot_usernameeee)
        await sython2.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython2.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython2.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython2(ImportChatInviteRequest(bott))
                msg2 = await sython2.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython2.send_message(event.chat_id, "تم الانتهاء من التجميع !")



@sython2.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العقاب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython2.get_entity(bot_usernameee)
        await sython2.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython2.get_entity(bot_usernameee)
        await sython2.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython2.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython2.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython2(ImportChatInviteRequest(bott))
                msg2 = await sython2.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython2.send_message(event.chat_id, "تم الانتهاء من التجميع !")




##########################################

@sython3.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗬𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗦𝗔𝗬𝗧𝗛𝗢𝗡𝗛    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟬 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗛𝗨𝗦𝗔𝗠.𝗙𝗔  ※

╰───⌯𝗦𝗬𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

@sython3.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython3.get_entity(bot_username)
        await sython3.send_message('@zmmbot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython3.get_entity(bot_username)
        await sython3.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython3.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython3.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython3(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython3.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython3(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython3(ImportChatInviteRequest(bott))
                msg2 = await sython3.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython3.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython3.send_message(event.chat_id, "تم الانتهاء من التجميع !")

@sython3.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython3.get_entity(bot_usernamee)
        await sython3.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython3.get_entity(bot_usernamee)
        await sython3.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython3.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython3.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython3(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython3.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython3(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython3(ImportChatInviteRequest(bott))
                msg2 = await sython3.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython3.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython3.send_message(event.chat_id, "تم الانتهاء من التجميع !")
        
@sython3.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython3.get_entity(bot_usernameee)
        await sython3.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython3.get_entity(bot_usernameee)
        await sython3.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython3.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython3.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython3(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython3.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython3(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython3(ImportChatInviteRequest(bott))
                msg2 = await sython3.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython3.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython3.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython3.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython3.get_entity(bot_usernameeee)
        await sython3.send_message('@xnsex21bot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython3.get_entity(bot_usernameeee)
        await sython3.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython3.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython3.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython3(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython3.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython3(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython3(ImportChatInviteRequest(bott))
                msg2 = await sython3.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython3.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython3.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython3.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython3.get_entity(bot_username)
        await sython3.send_message('@zmmbot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython3.get_entity(bot_username)
        await sython3.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython3.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython3.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython3(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython3.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython3(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython3(ImportChatInviteRequest(bott))
                msg2 = await sython3.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython3.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython3.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython3.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع الجوكر"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython3.get_entity(bot_usernamee)
        await sython3.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython3.get_entity(bot_usernamee)
        await sython3.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython3.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython3.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython3(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython3.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython3(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython3(ImportChatInviteRequest(bott))
                msg2 = await sython3.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython3.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython3.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython3.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العرب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython3.get_entity(bot_usernameeee)
        await sython3.send_message('@xnsex21bot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython3.get_entity(bot_usernameeee)
        await sython3.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython3.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython3.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython3(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython3.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython3(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython3(ImportChatInviteRequest(bott))
                msg2 = await sython3.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython3.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython3.send_message(event.chat_id, "تم الانتهاء من التجميع !")



@sython3.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العقاب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython3.get_entity(bot_usernameee)
        await sython3.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython3.get_entity(bot_usernameee)
        await sython3.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython3.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython3.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython3(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython3.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython3(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython3(ImportChatInviteRequest(bott))
                msg2 = await sython3.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython3.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython3.send_message(event.chat_id, "تم الانتهاء من التجميع !")




##########################################

@sython4.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗬𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗦𝗔𝗬𝗧𝗛𝗢𝗡𝗛    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟬 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗛𝗨𝗦𝗔𝗠.𝗙𝗔  ※

╰───⌯??𝗬𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

@sython4.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython4.get_entity(bot_username)
        await sython4.send_message('@zmmbot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython4.get_entity(bot_username)
        await sython4.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython4.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython4.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython4(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython4.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython4(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython4(ImportChatInviteRequest(bott))
                msg2 = await sython4.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython4.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython4.send_message(event.chat_id, "تم الانتهاء من التجميع !")

@sython4.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython4.get_entity(bot_usernamee)
        await sython4.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython4.get_entity(bot_usernamee)
        await sython4.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython4.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython4.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython4(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython4.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython4(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython4(ImportChatInviteRequest(bott))
                msg2 = await sython4.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython4.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython4.send_message(event.chat_id, "تم الانتهاء من التجميع !")
        
@sython4.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython4.get_entity(bot_usernameee)
        await sython4.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython4.get_entity(bot_usernameee)
        await sython4.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython4.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython4.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython4(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython4.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython4(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython4(ImportChatInviteRequest(bott))
                msg2 = await sython4.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython4.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython4.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython4.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython4.get_entity(bot_usernameeee)
        await sython4.send_message('@xnsex21bot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython4.get_entity(bot_usernameeee)
        await sython4.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython4.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython4.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython4(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython4.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython4(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython4(ImportChatInviteRequest(bott))
                msg2 = await sython4.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython4.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython4.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython4.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython4.get_entity(bot_username)
        await sython4.send_message('@zmmbot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython4.get_entity(bot_username)
        await sython4.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython4.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython4.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython4(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython4.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython4(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython4(ImportChatInviteRequest(bott))
                msg2 = await sython4.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython4.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython4.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython4.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع الجوكر"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython4.get_entity(bot_usernamee)
        await sython4.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython4.get_entity(bot_usernamee)
        await sython4.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython4.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython4.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython4(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython4.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython4(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython4(ImportChatInviteRequest(bott))
                msg2 = await sython4.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython4.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython4.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython4.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العرب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython4.get_entity(bot_usernameeee)
        await sython4.send_message('@xnsex21bot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython4.get_entity(bot_usernameeee)
        await sython4.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython4.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython4.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython4(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython4.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython4(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython4(ImportChatInviteRequest(bott))
                msg2 = await sython4.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython4.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython4.send_message(event.chat_id, "تم الانتهاء من التجميع !")



@sython4.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العقاب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython4.get_entity(bot_usernameee)
        await sython4.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython4.get_entity(bot_usernameee)
        await sython4.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython4.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython4.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython4(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython4.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython4(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython4(ImportChatInviteRequest(bott))
                msg2 = await sython4.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython4.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython4.send_message(event.chat_id, "تم الانتهاء من التجميع !")




##########################################

@sython5.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗬𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗦𝗔𝗬𝗧𝗛𝗢𝗡𝗛    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟬 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗛𝗨𝗦𝗔𝗠.𝗙𝗔  ※

╰───⌯𝗦𝗬𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

@sython5.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython5.get_entity(bot_username)
        await sython5.send_message('@zmmbot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython5.get_entity(bot_username)
        await sython5.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython5.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython5.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython5(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython5.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython5(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython5(ImportChatInviteRequest(bott))
                msg2 = await sython5.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython5.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython5.send_message(event.chat_id, "تم الانتهاء من التجميع !")

@sython5.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython5.get_entity(bot_usernamee)
        await sython5.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython5.get_entity(bot_usernamee)
        await sython5.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython5.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython5.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython5(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython5.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython5(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython5(ImportChatInviteRequest(bott))
                msg2 = await sython5.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython5.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython5.send_message(event.chat_id, "تم الانتهاء من التجميع !")
        
@sython5.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython5.get_entity(bot_usernameee)
        await sython5.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython5.get_entity(bot_usernameee)
        await sython5.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython5.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython5.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython5(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython5.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython5(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython5(ImportChatInviteRequest(bott))
                msg2 = await sython5.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython5.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython5.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython5.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython5.get_entity(bot_usernameeee)
        await sython5.send_message('@xnsex21bot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython5.get_entity(bot_usernameeee)
        await sython5.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython5.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython5.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython5(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython5.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython5(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython5(ImportChatInviteRequest(bott))
                msg2 = await sython5.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython5.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython5.send_message(event.chat_id, "تم الانتهاء من التجميع !")

@sython5.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython5.get_entity(bot_username)
        await sython5.send_message('@zmmbot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython5.get_entity(bot_username)
        await sython5.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython5.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython5.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython5(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython5.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython5(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython5(ImportChatInviteRequest(bott))
                msg2 = await sython5.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython5.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython5.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython5.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع الجوكر"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython5.get_entity(bot_usernamee)
        await sython5.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython5.get_entity(bot_usernamee)
        await sython5.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython5.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython5.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython5(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython5.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython5(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython5(ImportChatInviteRequest(bott))
                msg2 = await sython5.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython5.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython5.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython5.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العرب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython5.get_entity(bot_usernameeee)
        await sython5.send_message('@xnsex21bot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython5.get_entity(bot_usernameeee)
        await sython5.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython5.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython5.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython5(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython5.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython5(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython5(ImportChatInviteRequest(bott))
                msg2 = await sython5.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython5.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython5.send_message(event.chat_id, "تم الانتهاء من التجميع !")



@sython5.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العقاب"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython5.get_entity(bot_usernameee)
        await sython5.send_message('@MARKTEBOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython5.get_entity(bot_usernameee)
        await sython5.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython5.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython5.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython5(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython5.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython5(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython5(ImportChatInviteRequest(bott))
                msg2 = await sython5.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython5.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython5.send_message(event.chat_id, "تم الانتهاء من التجميع !")



##########################################

print("💠 Sython Userbot Running 💠")
sython1.run_until_disconnected()
sython2.run_until_disconnected()
sython3.run_until_disconnected()
sython4.run_until_disconnected()
sython5.run_until_disconnected()
