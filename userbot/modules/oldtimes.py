from telethon import events
from userbot.events import register
from userbot import CMD_HELP

normiefont = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
oldengfont = ['𝔄', '𝔅', 'ℭ', '𝔇', '𝔈', '𝔉', '𝔊', 'ℌ', 'ℑ', '𝔍', '𝔎', '𝔏', '𝔐', '𝔑', '𝔒', '𝔓', '𝔔', 'ℜ', '𝔖', '𝔗', '𝔘', '𝔙', '𝔚', '𝔛', '𝔜', 'ℨ']



@register(outgoing=True, pattern="^.oldeng(?: |$)(.*)")
async def oldy(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`What, I am Supposed To Work with text only`")
        return
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
           oldycharacter = oldengfont[normiefont.index(normiecharacter)]
           string = string.replace(normiecharacter, oldycharacter)
    await event.edit(string)
CMD_HELP.update({
"oldengfont":
"old eng font \
\nUse:- .oldeng (text)"
})
