from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram import Client , filters




@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
    text = """**Free Plan User**
Daily  Upload limit 5GB
Price 0

**🪙 Basic**
Daily  Upload  limit 20GB
Price Rs 69  ind /🌎 0.81$  per Month

**⚡ Standard**
Daily Upload limit 50GB
Price Rs 119  ind /🌎 1.41$  per Month

**💎 Pro**
Daily Upload limit 100GB
Price Rs 199  ind /🌎 2.35$  per Month

Payment Details :-
<b>➜ UPI ID :</b> <code>shanusoraeran.com@fam</code>

After Payment Send Screenshots Of Payment To Admin @Mikoyo"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url = "https://telegram.me/Mikoyo"),
        InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
        ])
    
    await update.message.edit(text = text,reply_markup = keybord, disable_web_page_preview=True)
    
    

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
    text = """**Free Plan User**
Daily  Upload limit 5GB
Price 0

**🪙 Basic**
Daily  Upload  limit 20GB
Price Rs 69  ind /🌎 0.81$  per Month

**⚡ Standard**
Daily Upload limit 50GB
Price Rs 199  ind /🌎 1.41$  per Month

**💎 Pro**
Daily Upload limit 100GB
Price Rs 199  ind /🌎 2.35$  per Month

Payment Details :-
<b>➜ UPI ID :</b> <code>shanusoraeran.com@fam</code>

After Payment Send Screenshots Of Payment To Admin @Mikoyo"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url = "https://telegram.me/Mikoyo"),
        InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
        ])
    
    await message.reply_text(text=text, reply_markup=keybord, quote=True, disable_web_page_preview=True)
