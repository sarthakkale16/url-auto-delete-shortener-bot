import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://beingtek.com/ref/GreyMatter658')
    START_TXT = environ.get("START_TXT", '''<b>𝙃𝙚𝙮 👋🏻 {} 𝙄 𝘼𝙢 𝙏𝙚𝙨𝙨𝙖𝙐𝙍𝙇 𝘽𝙤𝙩!\n✰ 𝙄 𝘼𝙢 𝘼 𝙊𝙥𝙚𝙣 𝙎𝙤𝙪𝙧𝙘𝙚 𝘾𝙤𝙙𝙚 𝘽𝙤𝙩 !\n✰ 𝙅𝙪𝙨𝙩 𝘼𝙙𝙙 𝙈𝙚 𝙄𝙣 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 𝘼𝙨 𝘼𝙙𝙢𝙞𝙣 𝘼𝙣𝙙 𝙎𝙚𝙚 𝙏𝙝𝙚 𝙈𝙖𝙜𝙞𝙘 ☆</b>

<i>✰ 𝙄 𝘼𝙢 𝘼𝙪𝙩𝙤𝙛𝙞𝙡𝙩𝙚𝙧 𝘽𝙤𝙩 𝙁𝙤𝙧 𝙔𝙤𝙪𝙧 𝙃𝙚𝙡𝙥 \n✰ 𝙂𝙚𝙩 𝙀𝙫𝙚𝙧𝙮 𝙈𝙤𝙫𝙞𝙚 𝘽𝙮 𝙅𝙪𝙨𝙩 𝘼𝙙𝙙𝙞𝙣𝙜 𝙈𝙚 𝙏𝙤 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 \n✰ 𝙄𝙣𝙡𝙞𝙣𝙚 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝘼𝙙𝙙𝙚𝙙</i>''')
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """<b><i>My Updates : <a href=https://t.me/rb1bots><b>TessaURL</b></a>\n
👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/know_sarthak16>✰ sᴀʀᴛʜᴀᴋ ✰</a>\n
☆ L𝙸B𝚁𝙰𝚁Y : 𝘔𝘈𝘕𝘎𝘖 𝘋𝘉\n
☆ L𝙰N𝙶𝚄A𝙶E : 𝘗𝘠𝘛𝘏𝘖𝘕 3.4+\n
☆ 𝗦𝘁𝗮𝘁𝘂𝘀 : <a href=https://t.me/rb1bots>✶ 𝗕𝗼𝘁 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 ✶</a>\n
✰ Ｓｏｕｒｃｅ: <a https://telegram.dog/sarthakkale16>⋆ 𝙰𝚜𝚔 𝙷𝚎𝚛𝚎 ⋆</a>\n
☆ D𝙰𝚃AB𝙰S𝙴 : 𝘗𝘳𝘪𝘷𝘢𝘵𝘦 𝘕𝘰𝘸"""
    SOURCE_TXT = """<b>𝐂𝐫𝐞𝐚𝐭𝐞 𝐎𝐧𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬:</b>
☛  <a href=https://github.com/sarthakkale16>★ 𝗙𝗼𝗿𝗸 𝗔𝗻𝘆 𝗥𝗲𝗽𝗼 𝗔𝗻𝗱 𝗚𝗶𝘃𝗲 𝗦𝘁𝗮𝗿 ★</a>\n★ 𝙄 𝘼𝙢 𝙉𝙤𝙩 𝙏𝙝𝙚 𝘾𝙧𝙚𝙖𝙩𝙤𝙧 𝙊𝙛 𝙏𝙝𝙞𝙨 𝙎𝙤𝙪𝙧𝙘𝙚 𝙄 𝙃𝙖𝙫𝙚 𝙅𝙪𝙨𝙩 𝙈𝙤𝙙𝙞𝙛𝙞𝙚𝙙 𝙄𝙩 😌 !\n★ 𝙏𝙝𝙞𝙨 𝙄𝙨 𝙈𝙤𝙙𝙞𝙛𝙞𝙚𝙙 𝙑𝙚𝙧𝙨𝙞𝙤𝙣 𝙊𝙛 𝘼𝙪𝙩𝙤 𝙁𝙞𝙡𝙩𝙚𝙧 𝘽𝙤𝙩 𝙒𝙞𝙩𝙝 𝙐𝙍𝙇 𝙎𝙃𝙊𝙍𝙏𝙉𝙀𝙍!\n➣ 𝗜𝗳 𝗬𝗼𝘂 𝗪𝗮𝗻𝘁 𝗕𝗼𝘁 𝗟𝗶𝗸𝗲 𝗧𝗵𝗶𝘀 𝗧𝗵𝗲𝗻
➣ 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗠𝗲 ➺ @helpsarthak_bot<b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Search Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Search Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Search Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Search Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/rb1official)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Search Bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """╭──── #𝗚𝗿𝗼𝘂𝗽 𝗕𝘆 𝗧𝗲𝘀𝘀𝗮𝗨𝗥𝗟
    
<b>᚛› 𝗚𝗿𝗼𝘂𝗽 ☞ {}(<code>{}</code>)</b>
<b>᚛› 𝗧𝗼𝘁𝗮𝗹 𝗠𝗲𝗺𝗯𝗲𝗿𝘀 ☞ <code>{}</code></b>

<b>᚛› 𝗔𝗱𝗱𝗲𝗱 𝗕𝘆 ☞ {}</b>
<b> ★ 𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 @rb1bots
╰────"""
    LOG_TEXT_P = """#𝗡𝗲𝘄𝗨𝘀𝗲𝗿 𝗕𝘆 𝗧𝗲𝘀𝘀𝗮𝗨𝗥𝗟
    
<b>᚛› 𝗜𝗗 ☞ - <code>{}</code></b>
<b>᚛› 𝗡𝗮𝗺𝗲 ☞ - {}</b>
"""
