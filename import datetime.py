import datetime
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔑 Your Bot Token from BotFather
BOT_TOKEN = "8312132381:AAGTK2VQ3jJSM3U5rAiFK-4SiOfHAIbhKsY"

# 👁️ You (parent/controller) get secret updates
PARENT_TELEGRAM_ID = 1753998047  # Replace with YOUR Telegram ID

# 📚 Your GitHub-hosted story
STORY_URL = "https://github.com/storiesforu433/hindi-stories/blob/main/hindistories.txt"

# ✅ Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Namaste! Hindi kahani padhne ke liye /story likho.")

# 📖 Story sending with secret logging
async def send_story(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    try:
        response = requests.get(STORY_URL)
        story = response.text.strip()

        await update.message.reply_text(story[:4096])

        # Secret log for you
        log = f"""
📚 *Story Read*
👤 User: @{user.username or 'NoUsername'}
🆔 ID: {user.id}
🕒 Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
📖 File: {STORY_URL.split('/')[-1]}
"""
        await context.bot.send_message(chat_id=PARENT_TELEGRAM_ID, text=log, parse_mode="Markdown")

    except Exception as e:
        await update.message.reply_text("Kahani load nahi ho paayi 😔")
        print(f"Error: {e}")
