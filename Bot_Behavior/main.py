from Bot_Behavior.bot_behavior import *

# BOT_KEY
BOT_KEY = get_bot_key("BOT_KEY")

# Shortcut for ConversationHandler.END
END = ConversationHandler.END

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_KEY).build()

    description_conv = [
        CallbackQueryHandler(change_age, pattern="^" + str(dialog_states.CHANGE_AGE) + "$"),
        CallbackQueryHandler(change_city, pattern="^" + str(dialog_states.CHANGE_CITY) + "$"),
        CallbackQueryHandler(change_gender, pattern="^" + str(dialog_states.CHANGE_GENDER) + "$"),
        CallbackQueryHandler(change_search_of, pattern="^" + str(dialog_states.CHANGE_SEARCH_OF) + "$"),
        CallbackQueryHandler(change_music, pattern="^" + str(dialog_states.CHANGE_MUSIC) + "$"),
        CallbackQueryHandler(change_description, pattern="^" + str(dialog_states.CHANGE_DESCRIPTION) + "$"),
        CallbackQueryHandler(change_images, pattern="^" + str(dialog_states.CHANGE_IMAGES) + "$"),
    ]

    Page_handler = ConversationHandler(
        entry_points=[MessageHandler(callback=change_age, filters=filters.TEXT)],
        states=
        {
            dialog_states.PAGE_CUSTOMIZE: [MessageHandler(callback=change_age, filters=filters.TEXT)],
            dialog_states.CHANGE_CITY: [MessageHandler(callback=change_city, filters=filters.TEXT),
                                        CallbackQueryHandler(change_name, pattern=f"^" + dialog_states.CHANGE_NAME + "$")],
            dialog_states.CHANGE_GENDER: [CallbackQueryHandler(change_age, pattern=f"^" + dialog_states.CHANGE_AGE + "$"),
                                          MessageHandler(callback=change_gender, filters=filters.TEXT)],
            dialog_states.CHANGE_SEARCH_OF: [CallbackQueryHandler(change_city, pattern=f"^" + dialog_states.CHANGE_CITY + "$"),
                                             CallbackQueryHandler(change_search_of, pattern=f"^{dialog_states.MALE}$|^{dialog_states.FEMALE}$")],
            dialog_states.CHANGE_MUSIC: [CallbackQueryHandler(change_gender, pattern=f"^" + dialog_states.CHANGE_GENDER + "$"),
                                         CallbackQueryHandler(change_music, pattern=f"^{dialog_states.MALE}$|^{dialog_states.FEMALE}$")],
            dialog_states.CHANGE_DESCRIPTION: [CallbackQueryHandler(change_search_of, pattern=f"^" + dialog_states.CHANGE_SEARCH_OF + "$"),
                                               MessageHandler(callback=change_description, filters=filters.TEXT)],
            dialog_states.CHANGE_IMAGES: [CallbackQueryHandler(change_music, pattern=f"^" + dialog_states.CHANGE_MUSIC + "$"),
                                          MessageHandler(callback=change_images, filters=filters.TEXT)],
        },
        fallbacks=[CommandHandler(dialog_states.STOP, stop)],
        map_to_parent={
            END: dialog_states.ADD_PAGE,
        },

    )

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler(dialog_states.START, start)],
        states={
            dialog_states.ADD_PAGE: [CallbackQueryHandler(change_name, pattern="^" + str(dialog_states.ADD_PAGE) + "$")],
            dialog_states.PAGE_CUSTOMIZE: [Page_handler],
            dialog_states.STOPPING: [CommandHandler(dialog_states.START, start)],
        },
        fallbacks=[CommandHandler(dialog_states.STOP, stop)],
    )

    application.add_handler(conv_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)
