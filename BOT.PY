import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    response = model.generate_content(
        "Sen foydali va xushmuomala AI yordamchisan. Har doim o'zbek tilida javob ber.\n\n"
        + user_text
    )

    await update.message.reply_text(response.text)


app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
)

print("🤖 Gemini AI bot ishga tushdi...")
app.run_polling()
