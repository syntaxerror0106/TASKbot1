import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

user_tasks = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def addtask(ctx, *, task: str):
    user = ctx.author.id
    user_tasks.setdefault(user, []).append(task)
    await ctx.send(f"✅ Task added: `{task}`")

@bot.command()
async def listtasks(ctx):
    user = ctx.author.id
    tasks = user_tasks.get(user, [])
    if not tasks:
        await ctx.send("📭 You have no tasks.")
    else:
        task_list = "\n".join([f"{i+1}. {t}" for i, t in enumerate(tasks)])
        await ctx.send(f"📝 **Your Tasks:**\n{task_list}")

@bot.command()
async def removetask(ctx, index: int):
    user = ctx.author.id
    tasks = user_tasks.get(user, [])
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        await ctx.send(f"🗑️ Removed task: `{removed}`")
    else:
        await ctx.send("❌ Invalid task number.")

# Replace with your bot's token
bot.run("YOUR_DISCORD_BOT_TOKEN")
