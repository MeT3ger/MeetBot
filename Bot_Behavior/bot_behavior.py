from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update
from telebot import types
import Logger
from Bot_Behavior.botkeygetter import get_bot_key
from telegram import Update
from telegram.ext import filters, CallbackQueryHandler, MessageHandler, ApplicationBuilder, ContextTypes, \
    CommandHandler, Updater, \
    ConversationHandler
import dialog_states
import bot_reactions
import buttons_titles


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        bot_reactions.REACTION_CREATE_PAGE
    )

    buttons = [
        [
            InlineKeyboardButton(text=buttons_titles.BUTTON_CREATE_PAGE, callback_data=str(dialog_states.ADD_PAGE))
        ]
    ]

    keyboard = InlineKeyboardMarkup(buttons)

    if context.user_data.get(dialog_states.START_OVER):
        await update.callback_query.answer()
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=keyboard)

    else:

        await update.message.reply_text(
            bot_reactions.REACTION_FIRST_MESSAGE
        )
        await update.message.reply_text(text=text, reply_markup=keyboard)

    context.user_data[dialog_states.START_OVER] = False
    return dialog_states.ADD_PAGE


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """End Conversation by command."""
    await update.message.reply_text(bot_reactions.REACTION_BYE_MESSAGE)

    return END


async def change_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        bot_reactions.REACTION_GET_NAME
    )

    if context.user_data.get(dialog_states.START_OVER):
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text)
    else:
        await update.callback_query.answer()
        await context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                                    message_id=update.callback_query.message.message_id,
                                                    reply_markup=None)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    return dialog_states.PAGE_CUSTOMIZE


async def change_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        bot_reactions.REACTION_GET_AGE
    )

    buttons = [
        [
            InlineKeyboardButton(text=buttons_titles.BUTTON_BACK, callback_data=str(dialog_states.CHANGE_NAME))
        ]
    ]

    keyboard = InlineKeyboardMarkup(buttons)

    if context.user_data.get(dialog_states.START_OVER):
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=keyboard)
        if (update.callback_query):
            await context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                                        message_id=update.callback_query.message.message_id,
                                                        reply_markup=None)

    return dialog_states.CHANGE_CITY


async def change_city(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        bot_reactions.REACTION_GET_CITY
    )

    buttons = [
        [
            InlineKeyboardButton(text=buttons_titles.BUTTON_BACK, callback_data=str(dialog_states.CHANGE_AGE))
        ]
    ]

    keyboard = InlineKeyboardMarkup(buttons)

    if context.user_data.get(dialog_states.START_OVER):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=keyboard)
    else:
        if (update.callback_query):
            await update.callback_query.answer()
            await context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                                        message_id=update.callback_query.message.message_id,
                                                        reply_markup=None)
        else:
            await context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                                        message_id=update.message.message_id - 1,
                                                        reply_markup=None)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=keyboard)

    return dialog_states.CHANGE_GENDER


async def change_gender(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        bot_reactions.REACTION_GET_GENDER
    )

    buttons = [
        [
            InlineKeyboardButton(text=buttons_titles.BUTTON_MALE, callback_data=str(dialog_states.MALE)),
            InlineKeyboardButton(text=buttons_titles.BUTTON_FEMALE, callback_data=str(dialog_states.FEMALE)),
            InlineKeyboardButton(text=buttons_titles.BUTTON_BACK, callback_data=str(dialog_states.CHANGE_CITY)),
        ]
    ]

    keyboard = InlineKeyboardMarkup(buttons)

    keyboard = InlineKeyboardMarkup(buttons)

    if context.user_data.get(dialog_states.START_OVER):
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    else:
        if (update.callback_query):
            await update.callback_query.answer()
            await context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                                        message_id=update.callback_query.message.message_id,
                                                        reply_markup=None)
        else:
            await context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                                        message_id=update.message.message_id - 1,
                                                        reply_markup=None)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=keyboard)

    return dialog_states.CHANGE_SEARCH_OF


async def change_search_of(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        bot_reactions.REACTION_GET_SEARCH_GENDER
    )

    buttons = [
        [
            InlineKeyboardButton(text=buttons_titles.BUTTON_MALE, callback_data=dialog_states.MALE),
            InlineKeyboardButton(text=buttons_titles.BUTTON_FEMALE, callback_data=dialog_states.FEMALE),
            InlineKeyboardButton(text=buttons_titles.BUTTON_BACK, callback_data=str(dialog_states.CHANGE_GENDER)),
        ]
    ]

    keyboard = InlineKeyboardMarkup(buttons)

    if context.user_data.get(dialog_states.START_OVER):
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    else:
        print(update.callback_query.message)
        if (update.callback_query):
            await update.callback_query.answer()
            await context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                                        message_id=update.callback_query.message.message_id,
                                                        reply_markup=None)
        else:
            await context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                                        message_id=update.message.message_id - 1,
                                                        reply_markup=None)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=keyboard)

    return dialog_states.CHANGE_MUSIC


async def change_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        bot_reactions.REACTION_GET_MUSIC
    )

    buttons = [
        [
            InlineKeyboardButton(text=buttons_titles.BUTTON_BACK, callback_data=str(dialog_states.CHANGE_SEARCH_OF)),
        ]
    ]

    keyboard = InlineKeyboardMarkup(buttons)

    if context.user_data.get(dialog_states.START_OVER):
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    else:
        if (update.callback_query):
            await update.callback_query.answer()
            await context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                                        message_id=update.callback_query.message.message_id,
                                                        reply_markup=None)
        else:
            await context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                                        message_id=update.message.message_id - 1,
                                                        reply_markup=None)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=keyboard)

    return dialog_states.CHANGE_DESCRIPTION


async def change_description(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        bot_reactions.REACTION_GET_DESCRIPTION
    )

    buttons = [
        [
            InlineKeyboardButton(text=buttons_titles.BUTTON_BACK, callback_data=str(dialog_states.CHANGE_MUSIC)),
        ]
    ]

    keyboard = InlineKeyboardMarkup(buttons)

    if context.user_data.get(dialog_states.START_OVER):
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    else:
        if (update.callback_query):
            await update.callback_query.answer()
            await context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                                        message_id=update.callback_query.message.message_id - 1,
                                                        reply_markup=None)
        else:
            await context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                                        message_id=update.message.message_id - 1,
                                                        reply_markup=None)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=keyboard)

    return dialog_states.CHANGE_IMAGES


async def change_images(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        bot_reactions.REACTION_GET_PHOTO
    )

    buttons = [
        [
            InlineKeyboardButton(text=buttons_titles.BUTTON_BACK, callback_data=str(dialog_states.CHANGE_DESCRIPTION)),
        ]
    ]

    keyboard = InlineKeyboardMarkup(buttons)

    if context.user_data.get(dialog_states.START_OVER):
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    else:
        if (update.callback_query):
            await update.callback_query.answer()
            await context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                                        message_id=update.callback_query.message.message_id - 1,
                                                        reply_markup=None)
        else:
            await context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                                        message_id=update.message.message_id - 1,
                                                        reply_markup=None)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=keyboard)

    return END

