

from telethon import events
from userbot.events import register
from userbot import CMD_HELP

normiefont = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
circlyfont = ['🅐', '🅑', '🅒', '🅓', '🅔', '🅕', '🅖', '🅗', '🅘', '🅙', '🅚', '🅛', '🅜', '🅝', '🅞', '🅟', '🅠', '🅡', '🅢', '🅣', '🅤',
             '🅥', '🅦', '🅧', '🅨', '🅩']

@register(outgoing=True, pattern="^.circlify(?: |$)(.*)")
async def circly(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`What I am Supposed to circlyfy U Dumb`")
        return
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            circlycharacter = circlyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, circlycharacter)
    await event.edit(string)
CMD_HELP.update({
"circlify":
"circlifies your text.\
\nUse:- .circlify (text)"
})
