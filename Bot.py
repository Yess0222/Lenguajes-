import logging
import re

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Expresión regular para detectar mensajes que contienen "Hola"
expresion_regular = re.compile(r"hello|hi|hey|hola", re.IGNORECASE)
expresion_helado = re.compile(r"helado|sabor de helado|favorito", re.IGNORECASE)
expresion_sabor = re.compile(r"fresa|limon|chocolate", re.IGNORECASE)
expresion_correo1 = re.compile(r"puedes|correo|promociones", re.IGNORECASE)
expresion_correo = re.compile(r"^[a-zA-Z0-9_.+-]*@[hotmail|outlook|gmail]*\.(com)$")
expresion_adios = re.compile(r"adiós|bye|no", re.IGNORECASE)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message if it matches the regular expression."""
    message_text = update.message.text
    if expresion_regular.search(message_text):
        await update.message.reply_text("¡Hola! ¿Cómo estás?")
    elif expresion_helado.search(message_text):
        await update.message.reply_text("¿Cuál es tu sabor de helado favorito?")
    elif expresion_sabor.search(message_text):
        await update.message.reply_text("Uyy es muy rico")
    elif expresion_correo1.search(message_text):
        await update.message.reply_text("Me puedes dar un correo para enviarte las promociones de la semana")
    elif expresion_correo.search(message_text):
        await update.message.reply_text("Tu correo es correcto, en un momento te enviaremos nuestras promociones. Algo más en lo que pueda ayudarte??")
    elif expresion_adios.search(message_text):
        await update.message.reply_text("Fue un gusto ayudarte")
    else:
        await update.message.reply_text("No entendí tu mensaje.")


def main() -> None:
    """Start the bot."""
    application = Application.builder().token("7141491710:AAGjZh-HCLtY41FLfV2uxd7_k8WkT37wDgI").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
