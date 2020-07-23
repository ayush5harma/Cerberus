# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

# By Priyam Kalra
# Syntax (.hl <link>)

from telethon import events
from telethon.tl import functions, types
from userbot import CMD_HELP
from userbot.events import register
import asyncio


@register(outgoing=True, pattern=r"^.hl(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input = event.pattern_match.group(1)
    await event.edit("[ㅤㅤㅤㅤㅤㅤㅤ](" + input + ")")
CMD_HELP.update({
    "hl":
    "Use :- .hl <word> <link>"})
