import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Dictionary to store tasks per user ID
tasks = {}

@bot.command()
async def addtask(ctx, *, task):
    user = ctx.author.id
    tasks.setdefault(user, []).append(task)
    await ctx.send(f"✅ Task added for {ctx.author.name}: `{task}`")

@bot.command()
async def listtasks(ctx):
    user = ctx.author.id
    user_tasks = tasks.get(user, [])
    if not user_tasks:
        await ctx.send("❌ You have no tasks.")
    else:
        msg = "\n".join(f"{i+1}. {t}" for i, t in enumerate(user_tasks))
        await ctx.send(f"📝 Your tasks:\n{msg}")

@bot.command()
async def removetask(ctx, index: int):
    user = ctx.author.id
    user_tasks = tasks.get(user, [])
    if 0 < index <= len(user_tasks):
        removed = user_tasks.pop(index - 1)
        await ctx.send(f"🗑️ Removed task: `{removed}`")
    else:
        await ctx.send("❌ Invalid task number.")

# Run the bot
bot.run("PASTE_YOUR_TOKEN_HERE")
