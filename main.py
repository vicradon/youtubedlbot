from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os
import subprocess
import threading
import aiofiles

import asyncio
import nats

load_dotenv()


async def video_downloader(context, url):
    out = subprocess.run(["yt-dl", "--format", "mp4", url], capture_output=True)
    download_output_text = out.stdout.decode('utf-8')

    print(download_output_text)

    output_text = "Video retrived successfully"

    f = open("first-part.mp4", "rb")

    # await context.bot.send_document(chat_id=context._chat_id, document=f)
    await context.bot.send_message(chat_id=context._chat_id, text=output_text)


    # async with open("README.md") as file:
    #     # print(file)
    #     await context.bot.send_document(chat_id=context._chat_id, document=file)


async def download_full_video(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    # await nc.publish('hello', b'Hello World!')
    # print(out)

    try:
        # handling the case where a video input has already been processed when an edit happened
        args = update.message.text.split(" ")
        
        await update.message.reply_text("I've started working on it!")
        # threading.Thread(target=video_downloader, args=(context, args[1])).start()

        # async with aiofiles.open("README.md") as file:
        #     await context.bot.send_document(chat_id=context._chat_id, document=file)

        asyncio.create_task(video_downloader(context, args[1]))


    except AttributeError:
        pass


def main():
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    app.add_handler(CommandHandler("download", download_full_video))

    app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())