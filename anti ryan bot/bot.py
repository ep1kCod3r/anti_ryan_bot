import hikari, lightbulb

bot = lightbulb.BotApp(
    token="token"
)

@bot.listen()
async def on_bot_started(event: hikari.StartedEvent):
    print("Bot is ready.")
    await bot.update_presence(status=hikari.Status.IDLE, activity=hikari.Activity(name="game"))
    
@bot.listen
async def delete_ryan_messages(event: hikari.MessageCreateEvent):
    await print(event.author_id())


bot.run(
    
)