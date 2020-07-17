# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# Module By ElytrA8
from telethon import events

import asyncio

import os

import sys

import random

from userbot import CMD_HELP

from userbot.events import register



@register(pattern="^.thought(?: |$)(.*)")

async def _(event):

    if event.fwd_from:

        return

    await event.edit("`TESLA presents you some thoughts of greatest minds.`")

    await asyncio.sleep(2)

    x=(random.randrange(1,13))

    if x==1:

        await event.edit("`The Man have more expressions than woman, but they didn't express it. \n [Anonymous]`")

    if x==2:
    	
        await event.edit("`Try not to become man of success, but rather try to become a man of value. \n [Albert Einstein]`")

    if x==3:
    	
    	await event.edit("`Success is one percent inspiration, ninety-nine percent perspiration. \n [Thomas Edison]`")
    	
    if x==4:
    	
    	await event.edit("`Act as though it is impossible to fail. \n [Dorothea Brande]`")
    	    	
    if x==5:
    	
    	await event.edit("`Do or do not. There is no try. \n [yoda]`")
    	    	    	
    if x==6:
    	
    	await event.edit("`God gave us two ends: one to sit on and one to think with. Success depends on which one you use. Heads you win; tails, you lose. \n [Anonymous]`")
    	    	    	    	
    if x==7:
    	
    	await event.edit("`If you can't explain it simply, you don't understand it well enough \n [Albert Einstein]`")
    	    	    	    	    	
    if x==8:
    	
    	await event.edit("`What if i fall?  /n oh, but my darling /n what if you fly? \n [e.h.]`")
    	    	    	    	    	    	
    if x==9:
    	
    	await event.edit("`Only a life lived for others is worth living. \n [Albert Einstein]`")
    	    	    	    	    	    	    	
    if x==10:
    	
    	await event.edit("`Your Clock Will Never Slap you if you west your time, But destiny will one day. \n [Yaganesh Derasari]`")
    	    	    	    	    	    	    	    	
    if x==11:
    	
    	await event.edit("`Practice kindness all day to everybody and you will realize you’re already in heaven now. \n [Jack Kerouac]`")
    	    	    	    	    	    	    	    	    	
    if x==12:
    	
    	await event.edit("`Love only grows by sharing. You can only have more for yourself by giving it away to others. \n [Brain Tracy]`")
    	    	    	    	    	    	    	    	    	    	
    if x==13:
    	
    	await event.edit("`Change your life today. Don’t gamble on the future, act now, without delay. \n [Simone de Beauvoir]`")
