import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# MENÚ PRINCIPAL
def main_menu():
    keyboard = [
        [InlineKeyboardButton("📅 Citas extranjería", callback_data="citas")],
        [InlineKeyboardButton("📄 Documentos", callback_data="docs")],
        [InlineKeyboardButton("🤖 Marketing", callback_data="marketing")],
        [InlineKeyboardButton("💰 Facturas", callback_data="facturas")],
        [InlineKeyboardButton("ℹ️ Legal", callback_data="legal")]
    ]
    return InlineKeyboardMarkup(keyboard)

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Bienvenido a KLYX HUB\n\nSelecciona una opción:",
        reply_markup=main_menu()
    )

# BOTONES
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "citas":
        text = "📅 Gestión de citas de extranjería."
    elif data == "docs":
        text = "📄 Asistencia en documentos."
    elif data == "marketing":
        text = "🤖 Servicios de marketing digital."
    elif data == "facturas":
        text = "💰 Generación de propuestas y facturas."
    elif data == "legal":
        text = "ℹ️ Política de privacidad y términos."
    else:
        text = "Opción no válida."

    keyboard = [[InlineKeyboardButton("⬅️ Volver", callback_data="back")]]
    await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard))

    if data == "back":
        await query.edit_message_text(
            "👋 Menú principal:",
            reply_markup=main_menu()
        )

# MAIN
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()

if __name__ == "__main__":
    main()
