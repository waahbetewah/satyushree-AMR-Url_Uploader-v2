from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hello,
i am Telegram URL Upload Bot! Created by @shreevish

Please send me any direct download URL Link, i can upload to telegram as File/Video

 ๐จ . . . Note : its support almost all direct Url's except torrent link & some links . . . ๐จ
 
๐จ PRON video๐ Links gives you PERMANENT BAN ๐จ

       โโโโขโข๐โฟโค๏ธโฟ๐โขโขโโโ
       
URL-UPLOADER bot created by @shreevish

โผ/start = To Check whether the bot is alive or not
โผ/help = To Know how to use me! 
โผ/about = To know what am I !

โ ๏ธNote :- Join My Channel before paste the link"""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "Contact @shreevish for Details"
    FORMAT_SELECTION = """๐ญ ๐ฆ๐ฒ๐น๐ฒ๐ฐ๐ ๐๐ป๐ฑ ๐๐ต๐ผ๐๐ฒ ๐ฌ๐ผ๐๐ฟ ๐๐ผ๐ฟ๐บ๐ฎ๐๐

๐๏ธ ๐ฉ๐๐๐๐ข = Upload as Streamble.

๐ ๐๐๐๐ = Upload as File.
โขโขโขโขโขโขโขโขโขโขโขโขโขโขโขโขโขโขโข

โผ/delthum = To Delet thumbnail

โผpLease send photo to save Thumblail before you press any Below Button

๐ฒPowered By: @All_Movie_Rockers.
"""
    HELP_TEXT = """
<b>1.<u>Link to Media or File</u></b>
โ  Send a link for upload to telegram file or media.

<b>2.<u>Set Thumbnail</u></b>
โ  Send a photo to make it as permanent thumbnail.

<b>3.<u>To download</u></b>
Select the button.
   ๐SVideo๐ - Give File as video with Screenshots
   ๐๏ธDFile๐๏ธ  - Give File with Screenshots
   ๐Video๐  - Give File as video without Screenshots
   ๐๏ธDFile๐๏ธ  - Give File without Screenshots

<b><u>Deleting Thumbnail</u></b>
โ  Send /delthumb to deleting thumbnail.

<b><u>Show Thumbnail</u></b>
โ  Send /showthumb to view custom thumbnail.

Made by @shreevish
"""
    ABOUT_TEXT = """
- **Bot :** `URL Uploader`
- **Creator :** [๊งโHACKERโ๊ง](https://telegram.me/shreevish)
- **Channel :** [Aสส Mแดแด ษชแด Rแดแดแดแดสs](https://telegram.me/FayasNoushad)
- **Credits :** `Everyone in this journey`
- **Source :** [Click here](https://github.com/Satyamurthi/AMR-Url_Uploader)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('๐Channel๐', url='https://telegram.me/All_Movie_Rockers'),
        InlineKeyboardButton('Creator โ๏ธ', url='https://telegram.me/shreevish')
        ],[
        InlineKeyboardButton('๐กHelp๐ก', callback_data='help'),
        InlineKeyboardButton('๐ทAbout๐ท', callback_data='about'),
        InlineKeyboardButton('๐Close๐', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('๐ Home๐ ', callback_data='home'),
        InlineKeyboardButton('๐ทAbout๐ท', callback_data='about'),
        InlineKeyboardButton('๐Close๐', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('๐ Home๐ ', callback_data='home'),
        InlineKeyboardButton('๐กHelp๐ก', callback_data='help'),
        InlineKeyboardButton('๐Close๐', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = """<b>Select the desired format:</b> <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /delthumb to delete the auto-generated thumbnail."""
    CHECKING_LINK = "Analysing Your Link โณ"
    BANNED_USER_TEXT = "You are B A N N E D ๐คฃ๐คฃ๐คฃ๐คฃ"
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos Follow the steps :-

โฒFor Custom Name
โผURL | FileName.Extension

โฒFor Premium Videos
โผURL | FileName.Extension | username | password"""
    DOWNLOAD_START = " ๐ฅ Downloading to my server \n๐ฅ Please wait...โณ ๐๐๐ \nIt takes time depend on File Size "    
    UPLOAD_START = " ๐ค Yay,File Download Successfully ๐ \nNow Uploading to Telegram ๐ค "
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = " ๐ค Downloaded in {} seconds. \n\nUploaded in {} seconds."
    RCHD_TG_API_LIMIT = " ๐ค Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    CUSTOM_CAPTION_UL_FILE = "<b>Join :-</b> @All_Movie_Rockers"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    NO_VOID_FORMAT_FOUND = "{}"
    REPORT_SITE_TEXT = "๐โโ๏ธSorry not uploading in this site here because this site is reporting site.๐โ"
    SOMETHING_WRONG = "Something Wrong. Try again."
    FORCE_SUBSCRIBE_TEXT = "**Join My Updates Channel to use ME ๐ ๐คญ**"
    FREE_USER_LIMIT_Q_SZE = "Sorry Friend, Free users can only 1 request per {} minutes. Please try again after {} seconds later."
