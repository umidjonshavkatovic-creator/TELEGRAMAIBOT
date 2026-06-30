import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from groq import Groq

TOKEN = os.getenv("BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Sen foydali va xushmuomala AI yordamchisan. Har doim o'zbek tilida javob ber."
            },
            {
                "role": "user",
                "content": user_text
            }
        ]
    )

    answer = response.choices[0].message.content
    await update.message.reply_text(answer)

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
)

print("🤖 Groq AI bot ishga tushdi...")
app.run_polling() 