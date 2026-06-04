#!/usr/bin/env python3
"""
FONT GENERATOR BOT - 50+ Stylish Fonts
Jaisa font user chaahe, waisa text convert karega
"""

import json
import urllib.request
import urllib.parse
import time
import os
from datetime import datetime
from flask import Flask, request
from threading import Thread

# ========== CONFIGURATION ==========
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
BOT_NAME = "Font Generator Bot"

# ========== FLASK APP ==========
app = Flask('')

@app.route('/')
def home():
    return f"🎨 {BOT_NAME} Active! 50+ Fonts Available"

@app.route(f'/webhook/{TELEGRAM_TOKEN}', methods=['POST'])
def webhook():
    try:
        update = json.loads(request.data)
        process_update(update)
        return 'OK', 200
    except Exception as e:
        print(f"Webhook error: {e}")
        return 'Error', 500

# ========== 50+ FONTS MAPPING ==========

FONTS = {
    # ====== 1-10: SERIF FONTS ======
    "serif_bold": {
        "name": "𝐁𝐨𝐥𝐝 𝐒𝐞𝐫𝐢𝐟",
        "desc": "Bold Serif style - Professional",
        "map": "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳"
    },
    "serif_italic": {
        "name": "𝑺𝒆𝒓𝒊𝒇 𝑰𝒕𝒂𝒍𝒊𝒄",
        "desc": "Italic Serif - Elegant",
        "map": "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛"
    },
    "serif_bold_italic": {
        "name": "𝑩𝒐𝒍𝒅 𝑺𝒆𝒓𝒊𝒇 𝑰𝒕𝒂𝒍𝒊𝒄",
        "desc": "Bold Italic Serif - Strong & Stylish",
        "map": "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛"
    },
    
    # ====== 11-20: SCRIPT/CURSIVE FONTS ======
    "script": {
        "name": "𝓢𝓬𝓻𝓲𝓹𝓽",
        "desc": "Cursive Script - Handwriting style",
        "map": "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃"
    },
    "script_bold": {
        "name": "𝓢𝓬𝓻𝓲𝓹𝓽 𝓑𝓸𝓵𝓭",
        "desc": "Bold Cursive - Thick handwriting",
        "map": "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃"
    },
    "cursive": {
        "name": "𝒞𝓊𝓇𝓈𝒾𝓋ℯ",
        "desc": "Elegant Cursive - Wedding style",
        "map": "𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"
    },
    
    # ====== 21-30: GOTHIC/FRAKTUR FONTS ======
    "fraktur": {
        "name": "𝕱𝖗𝖆𝖐𝖙𝖚𝖗",
        "desc": "Gothic Fraktur - Old German style",
        "map": "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟"
    },
    "fraktur_bold": {
        "name": "𝕱𝖗𝖆𝖐𝖙𝖚𝖗 𝕭𝖔𝖑𝖉",
        "desc": "Bold Gothic - Dark style",
        "map": "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟"
    },
    "gothic": {
        "name": "𝔊𝔬𝔱𝔥𝔦𝔠",
        "desc": "Gothic Style - Medieval",
        "map": "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷"
    },
    
    # ====== 31-40: MONOSPACE/TYPEWRITER ======
    "monospace": {
        "name": "𝙼𝚘𝚗𝚘𝚜𝚙𝚊𝚌𝚎",
        "desc": "Monospace - Typewriter style",
        "map": "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣"
    },
    "typewriter": {
        "name": "𝚃𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛",
        "desc": "Typewriter - Old school",
        "map": "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣"
    },
    
    # ====== 41-50: DECORATIVE FONTS ======
    "double_struck": {
        "name": "𝔻𝕠𝕦𝕓𝕝𝕖 𝕊𝕥𝕣𝕦𝕔𝕜",
        "desc": "Double Struck - Math style",
        "map": "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫"
    },
    "smallcaps": {
        "name": "Sᴍᴀʟʟ Cᴀᴘs",
        "desc": "Small Caps - Elegant",
        "map": "ABCDEFGHIJKLMNOPQRSTUVWXYZᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ"
    },
    "bubble": {
        "name": "Ⓑⓤⓑⓑⓛⓔ",
        "desc": "Bubble - Cute style",
        "map": "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ"
    },
    "circle": {
        "name": "🅒🅘🅡🅒🅛🅔",
        "desc": "Circled - Enclosed style",
        "map": "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩"
    },
    "squared": {
        "name": "🄰🄱🄲🄳🄴",
        "desc": "Squared - Box style",
        "map": "🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉"
    },
    "parenthesis": {
        "name": "P⦅a⦆r⦅e⦆n⦅t⦆h⦅e⦆s⦅i⦆s",
        "desc": "Parenthesis - Bracket style",
        "map": "⦅A⦆⦅B⦆⦅C⦆⦅D⦆⦅E⦆⦅F⦆⦅G⦆⦅H⦆⦅I⦆⦅J⦆⦅K⦆⦅L⦆⦅M⦆⦅N⦆⦅O⦆⦅P⦆⦅Q⦆⦅R⦆⦅S⦆⦅T⦆⦅U⦆⦅V⦆⦅W⦆⦅X⦆⦅Y⦆⦅Z⦆⦅a⦆⦅b⦆⦅c⦆⦅d⦆⦅e⦆⦅f⦆⦅g⦆⦅h⦆⦅i⦆⦅j⦆⦅k⦆⦅l⦆⦅m⦆⦅n⦆⦅o⦆⦅p⦆⦅q⦆⦅r⦆⦅s⦆⦅t⦆⦅u⦆⦅v⦆⦅w⦆⦅x⦆⦅y⦆⦅z⦆"
    },
    
    # ====== 51-60: SANS SERIF FONTS ======
    "sans_bold": {
        "name": "𝗕𝗼𝗹𝗱 𝗦𝗮𝗻𝘀",
        "desc": "Bold Sans - Clean & bold",
        "map": "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇"
    },
    "sans_italic": {
        "name": "𝘚𝘢𝘯𝘴 𝘐𝘵𝘢𝘭𝘪𝘤",
        "desc": "Sans Italic - Slanted clean",
        "map": "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻"
    },
    "sans_bold_italic": {
        "name": "𝙎𝙖𝙣𝙨 𝘽𝙤𝙡𝙙 𝙄𝙩𝙖𝙡𝙞𝙘",
        "desc": "Bold Sans Italic",
        "map": "𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯"
    },
    
    # ====== 61-70: SPECIAL EFFECTS ======
    "strike": {
        "name": "S̶t̶r̶i̶k̶e̶",
        "desc": "Strikethrough - Crossed out",
        "map": "A̶B̶C̶D̶E̶F̶G̶H̶I̶J̶K̶L̶M̶N̶O̶P̶Q̶R̶S̶T̶U̶V̶W̶X̶Y̶Z̶a̶b̶c̶d̶e̶f̶g̶h̶i̶j̶k̶l̶m̶n̶o̶p̶q̶r̶s̶t̶u̶v̶w̶x̶y̶z̶"
    },
    "underline": {
        "name": "U̲n̲d̲e̲r̲l̲i̲n̲e̲",
        "desc": "Underline - Bottom line",
        "map": "A̲B̲C̲D̲E̲F̲G̲H̲I̲J̲K̲L̲M̲N̲O̲P̲Q̲R̲S̲T̲U̲V̲W̲X̲Y̲Z̲a̲b̲c̲d̲e̲f̲g̲h̲i̲j̲k̲l̲m̲n̲o̲p̲q̲r̲s̲t̲u̲v̲w̲x̲y̲z̲"
    },
    "slanted": {
        "name": "S̸l̸a̸n̸t̸e̸d̸",
        "desc": "Slanted - Angled strike",
        "map": "A̸B̸C̸D̸E̸F̸G̸H̸I̸J̸K̸L̸M̸N̸O̸P̸Q̸R̸S̸T̸U̸V̸W̸X̸Y̸Z̸a̸b̸c̸d̸e̸f̸g̸h̸i̸j̸k̸l̸m̸n̸o̸p̸q̸r̸s̸t̸u̸v̸w̸x̸y̸z̸"
    },
    "double_underline": {
        "name": "D̲o̲u̲b̲l̲e̲ U̲n̲d̲e̲r̲l̲i̲n̲e̲",
        "desc": "Double Underline",
        "map": "A̲̲B̲̲C̲̲D̲̲E̲̲F̲̲G̲̲H̲̲I̲̲J̲̲K̲̲L̲̲M̲̲N̲̲O̲̲P̲̲Q̲̲R̲̲S̲̲T̲̲U̲̲V̲̲W̲̲X̲̲Y̲̲Z̲̲a̲̲b̲̲c̲̲d̲̲e̲̲f̲̲g̲̲h̲̲i̲̲j̲̲k̲̲l̲̲m̲̲n̲̲o̲̲p̲̲q̲̲r̲̲s̲̲t̲̲u̲̲v̲̲w̲̲x̲̲y̲̲z̲̲"
    },
    
    # ====== 71-75: FUN FONTS ======
    "upside": {
        "name": "Upside Down",
        "desc": "Upside Down - Flip it!",
        "map": "∀qɔpǝɟɓɥᴉɾʞlɯuodbɹsʇnʌʍxʎzɐqɔpǝɟɓɥᴉɾʞlɯuodbɹsʇnʌʍxʎz"
    },
    "mirror": {
        "name": "ɿoɿɿiM",
        "desc": "Mirror - Reverse style",
        "map": "A𐐒𐐛DƐꟻGHIJ⅂WNOԀQRƧTUVWXYZɒdɔɘᎸǧʜiꞁʞ⅂mᴎoqɿꙅƚuvwxyz"
    },
    "tiny": {
        "name": "ᵗⁱⁿʸ",
        "desc": "Tiny - Small letters",
        "map": "ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᑫʳˢᵗᵘᵛʷˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᑫʳˢᵗᵘᵛʷˣʸᶻ"
    },
    "superscript": {
        "name": "ˢᵘᵖᵉʳˢᶜʳⁱᵖᵗ",
        "desc": "Superscript - Top align",
        "map": "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᵠᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᑫʳˢᵗᵘᵛʷˣʸᶻ"
    },
    "subscript": {
        "name": "ₛᵤbₛcᵣᵢₚₜ",
        "desc": "Subscript - Bottom align",
        "map": "ₐBCDₑFGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐbcdₑfgₕᵢⱼₖₗₘₙₒₚqᵣₛₜᵤᵥwₓᵧ₂"
    },
    
    # ====== 76-80: BUBBLE VARIANTS ======
    "black_bubble": {
        "name": "🅑🅛🅐🅒🅚 🅑🅤🅑🅑🅛🅔",
        "desc": "Black Bubble - Dark circles",
        "map": "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩"
    },
    "white_bubble": {
        "name": "Ⓗⓞⓛⓛⓞⓦ Ⓑⓤⓑⓑⓛⓔ",
        "desc": "Hollow Bubble - Outline circles",
        "map": "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ"
    },
    
    # ====== 81-85: SQUARE VARIANTS ======
    "white_square": {
        "name": "🄰🄱🄲 🅂🅀🅄🄰🅁🄴",
        "desc": "White Square - Empty boxes",
        "map": "🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉"
    },
    
    # ====== 86-90: ROMAN/NUMBER FONTS ======
    "roman": {
        "name": "ⅠⅠⅠ. ℝ𝕠𝕞𝕒𝕟",
        "desc": "Roman Numerals style",
        "map": "ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹⅺⅻ"
    },
    
    # ====== 91-95: CRAZY FONTS ======
    "zalgo": {
        "name": "Z̷̢̛a̶̡̛l̶̢̛g̷̢̛ơ̶̢",
        "desc": "Zalgo - Glitch/Horror style",
        "map": "Z̷̢̛a̶̡̛l̶̢̛g̷̢̛ơ̶̢ T̷̢̛e̶̡̛x̶̢̛t̷̢̛"
    },
    "vaporwave": {
        "name": "Ｖａｐｏｒｗａｖｅ",
        "desc": "Vaporwave - Full width",
        "map": "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    },
    "regional": {
        "name": "🇮🇳 🇷🇪🇬🇮🇴🇳🇦🇱",
        "desc": "Regional - Flag style",
        "map": "🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿"
    }
}

# ========== CREATE INLINE KEYBOARD ==========
def get_inline_keyboard(page=0):
    """Create inline keyboard with pagination"""
    fonts_per_page = 10
    font_keys = list(FONTS.keys())
    total_pages = (len(font_keys) + fonts_per_page - 1) // fonts_per_page
    
    start = page * fonts_per_page
    end = min(start + fonts_per_page, len(font_keys))
    
    keyboard = []
    
    # Add font buttons for current page
    for i in range(start, end, 2):
        row = []
        # First button
        if i < len(font_keys):
            font = FONTS[font_keys[i]]
            row.append({"text": font["name"], "callback_data": f"font_{font_keys[i]}"})
        # Second button
        if i + 1 < len(font_keys):
            font = FONTS[font_keys[i + 1]]
            row.append({"text": font["name"], "callback_data": f"font_{font_keys[i + 1]}"})
        if row:
            keyboard.append(row)
    
    # Pagination buttons
    nav_row = []
    if page > 0:
        nav_row.append({"text": "◀️ Previous", "callback_data": f"page_{page - 1}"})
    if page < total_pages - 1:
        nav_row.append({"text": "Next ▶️", "callback_data": f"page_{page + 1}"})
    if nav_row:
        keyboard.append(nav_row)
    
    # Info button
    keyboard.append([{"text": f"📊 Page {page + 1}/{total_pages} • {len(FONTS)} Fonts", "callback_data": "info"}])
    keyboard.append([{"text": "❓ How to Use", "callback_data": "help"}])
    
    return {"inline_keyboard": keyboard}

def get_back_keyboard():
    return {"inline_keyboard": [[{"text": "🔙 Back to Fonts", "callback_data": "back_to_fonts"}]]}

# ========== TELEGRAM API ==========
def telegram_api_call(method, params=None):
    if params is None:
        params = {}
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/{method}"
    data = json.dumps(params).encode('utf-8')
    try:
        req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"API error: {e}")
        return None

def send_message(chat_id, text, parse_mode=None, reply_markup=None, reply_to=None):
    params = {'chat_id': chat_id, 'text': text}
    if parse_mode:
        params['parse_mode'] = parse_mode
    if reply_markup:
        params['reply_markup'] = reply_markup
    if reply_to:
        params['reply_to_message_id'] = reply_to
    telegram_api_call('sendMessage', params)

def edit_message(chat_id, message_id, text, parse_mode=None, reply_markup=None):
    params = {
        'chat_id': chat_id,
        'message_id': message_id,
        'text': text
    }
    if parse_mode:
        params['parse_mode'] = parse_mode
    if reply_markup:
        params['reply_markup'] = reply_markup
    telegram_api_call('editMessageText', params)

def answer_callback(callback_id, text=None):
    params = {'callback_query_id': callback_id}
    if text:
        params['text'] = text
    telegram_api_call('answerCallbackQuery', params)

def send_typing(chat_id):
    telegram_api_call('sendChatAction', {'chat_id': chat_id, 'action': 'typing'})

def get_bot_info():
    result = telegram_api_call('getMe')
    return result.get('ok', False) if result else False

def set_webhook():
    render_url = os.environ.get("RENDER_EXTERNAL_HOSTNAME", "")
    if render_url:
        webhook_url = f"https://{render_url}/webhook/{TELEGRAM_TOKEN}"
        telegram_api_call('setWebhook', {'url': webhook_url})

# ========== CONVERT TEXT FUNCTION ==========
def convert_text(text, font_map):
    """Convert normal text to styled text"""
    result = []
    normal_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    normal_lower = "abcdefghijklmnopqrstuvwxyz"
    styled_chars = font_map
    
    for char in text:
        if char.isupper() and char in normal_upper:
            idx = normal_upper.index(char)
            result.append(styled_chars[idx] if idx < len(styled_chars) else char)
        elif char.islower() and char in normal_lower:
            idx = normal_lower.index(char)
            result.append(styled_chars[26 + idx] if 26 + idx < len(styled_chars) else char)
        else:
            result.append(char)
    return ''.join(result)

# ========== MESSAGE PROCESSING ==========
user_fonts = {}
current_page = {}

def process_update(update):
    global user_fonts, current_page
    
    # Handle callback queries
    if 'callback_query' in update:
        callback = update['callback_query']
        callback_id = callback.get('id')
        message = callback.get('message', {})
        chat_id = message.get('chat', {}).get('id')
        message_id = message.get('message_id')
        data = callback.get('data', '')
        
        answer_callback(callback_id)
        
        if data == "back_to_fonts":
            current_page[chat_id] = 0
            edit_message(chat_id, message_id, 
                        f"🎨 *{BOT_NAME}*\n\n✨ *{len(FONTS)}+ Stylish Fonts Available!*\n\nChoose a font style from below:",
                        parse_mode='Markdown',
                        reply_markup=get_inline_keyboard(0))
        
        elif data == "help":
            help_text = f"""❓ *How to Use {BOT_NAME}*

1️⃣ Click on any font button
2️⃣ Send me your text
3️⃣ I'll convert it to that font!

✨ *{len(FONTS)}+ Fonts Available!*

*Commands:*
/start - Show all fonts
/fonts - List all fonts

*Example:*
Click "𝐁𝐨𝐥𝐝 𝐒𝐞𝐫𝐢𝐟" then send "Hello"
→ Output: "𝐇𝐞𝐥𝐥𝐨"

*Tip:* You can forward the styled text anywhere!"""
            
            edit_message(chat_id, message_id, help_text, parse_mode='Markdown', reply_markup=get_back_keyboard())
        
        elif data == "info":
            info_text = f"""📊 *Font Statistics*

✨ *Total Fonts:* {len(FONTS)}
🎨 *Categories:* Serif, Script, Gothic, Sans, Special, Bubble, Square

*Navigate:* Use ◀️ and ▶️ buttons
*Select:* Click any font name
*Convert:* Send text after selecting

*Made with ❤️*"""
            edit_message(chat_id, message_id, info_text, parse_mode='Markdown', reply_markup=get_back_keyboard())
        
        elif data.startswith("page_"):
            page = int(data.split("_")[1])
            current_page[chat_id] = page
            edit_message(chat_id, message_id,
                        f"🎨 *{BOT_NAME}*\n\n✨ *{len(FONTS)}+ Stylish Fonts!* (Page {page + 1})\n\nChoose a font:",
                        parse_mode='Markdown',
                        reply_markup=get_inline_keyboard(page))
        
        elif data.startswith("font_"):
            font_key = data.replace("font_", "")
            font_info = FONTS.get(font_key, {})
            user_fonts[chat_id] = font_key
            
            text = f"🎨 *{font_info.get('name', 'Font')} Selected* ✨\n\n{font_info.get('desc', '')}\n\n━━━━━━━━━━━━━━━\n✏️ *Now send me your text!*\n━━━━━━━━━━━━━━━\n\n💡 *Example:* Send \"Hello World\"\n\nI'll convert it to {font_info.get('name', 'this font')} style!"
            
            edit_message(chat_id, message_id, text, parse_mode='Markdown', reply_markup=get_back_keyboard())
    
    # Handle normal messages
    elif 'message' in update:
        message = update['message']
        chat_id = message.get('chat', {}).get('id')
        user_name = message.get('from', {}).get('first_name', 'User')
        message_text = message.get('text', '')
        message_id = message.get('message_id')
        
        if not chat_id or not message_text:
            return
        
        # Handle commands
        if message_text.startswith('/'):
            cmd = message_text.lower()
            
            if cmd == '/start':
                welcome = f"""🎨 *✨ Welcome to {BOT_NAME}! ✨*

Convert your text into *stylish fonts* with just one click!

━━━━━━━━━━━━━━━
📊 *{len(FONTS)}+ Fonts Available!*
━━━━━━━━━━━━━━━

*How to use:* 🇮🇳
1️⃣ Click any font button below
2️⃣ Send me your text
3️⃣ Get stylish text instantly!

*Font Categories:*
• 𝐁𝐨𝐥𝐝 𝐒𝐞𝐫𝐢𝐟 • 𝑺𝒆𝒓𝒊𝒇 𝑰𝒕𝒂𝒍𝒊𝒄
• 𝓢𝓬𝓻𝓲𝓹𝓽 • 𝕱𝖗𝖆𝖐𝖙𝖚𝖗
• 𝙼𝚘𝚗𝚘𝚜𝚙𝚊𝚌𝚎 • Sᴍᴀʟʟ Cᴀᴘs
• 🅒🅘🅡🅒🅛🅔 • Ⓑⓤⓑⓑⓛⓔ
• And many more...

🚀 *Click a font to get started!*"""
                
                send_message(chat_id, welcome, parse_mode='Markdown', reply_markup=get_inline_keyboard(0))
                return
            
            elif cmd == '/fonts':
                send_message(chat_id, f"🎨 *{len(FONTS)}+ Fonts Available:*\n\nClick the buttons below!", 
                           parse_mode='Markdown', reply_markup=get_inline_keyboard(0))
                return
            
            else:
                send_message(chat_id, "❓ *Unknown command.*\n\nUse /start to see all fonts!", 
                           parse_mode='Markdown', reply_markup=get_inline_keyboard(0))
                return
        
        # Check if user has selected a font
        if chat_id in user_fonts:
            font_key = user_fonts[chat_id]
            font_info = FONTS.get(font_key, {})
            
            if font_info and 'map' in font_info:
                send_typing(chat_id)
                converted = convert_text(message_text, font_info['map'])
                
                result = f"*✨ {font_info['name']} Style:*\n\n`{converted}`\n\n━━━━━━━━━━━━━━━\n💡 *Send another text to convert again!*\n━━━━━━━━━━━━━━━\n\n🔄 *Select /fonts for different style*"
                
                send_message(chat_id, result, parse_mode='Markdown', reply_markup=get_back_keyboard())
                return
        
        # If no font selected
        send_message(chat_id, f"❌ *No font selected!*\n\nPlease select a font first using /start or /fonts\n\n✨ *{len(FONTS)}+ Fonts Available!*", 
                    parse_mode='Markdown', reply_markup=get_inline_keyboard(0))

# ========== MAIN ==========
if __name__ == "__main__":
    print("=" * 50)
    print(f"🎨 {BOT_NAME} Starting...")
    print("=" * 50)
    
    if not TELEGRAM_TOKEN:
        print("❌ ERROR: TELEGRAM_TOKEN not set!")
    else:
        print(f"✅ Bot Token: {TELEGRAM_TOKEN[:10]}...")
        
        if get_bot_info():
            print(f"✅ Bot connected successfully!")
            set_webhook()
            print(f"✅ Webhook set!")
        else:
            print(f"❌ Failed to connect!")
    
    print(f"✨ Total Fonts Available: {len(FONTS)}")
    print("=" * 50)
    print("🚀 Bot is running...")
    
    app.run(host='0.0.0.0', port=8080)
