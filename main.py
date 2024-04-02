from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os
import subprocess
import uuid
import asyncio

load_dotenv()


async def video_downloader(context, url):
    save_directory = f"/tmp/{str(uuid.uuid4())}"
    os.makedirs(save_directory)

    out = subprocess.run(["yt-dl", "-o", "%(title)s.%(ext)s", "-P", save_directory, "-S", "res", "ext:mp4:m4a", "--recode", "mp4", "--no-simulate", url], capture_output=True)

    download_output_text = out.stdout.decode('utf-8')

    downloaded_video_path = f"{save_directory}/{os.listdir(save_directory)[0]}"

    output_text = "Video retrived successfully"

    video_file = open(downloaded_video_path, "rb")

    await context.bot.send_message(chat_id=context._chat_id, text="Now sending video...")

    await context.bot.send_video(chat_id=context._chat_id, video=video_file, supports_streaming=True)
    await context.bot.send_message(chat_id=context._chat_id, text=output_text)


async def download_full_video(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        # handling the case where a video input has already been processed when an edit happened
        args = update.message.text.split(" ")
        
        await update.message.reply_text("I've started working on it!")

        # threading.Thread(target=video_downloader, args=(context, args[1])).start()
        asyncio.create_task(video_downloader(context, args[1]))


    except AttributeError:
        pass


def main():
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    app.add_handler(CommandHandler("download", download_full_video))

    app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
