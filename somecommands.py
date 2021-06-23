import discord, time, os
from discord.ext import commands
from dotenv import load_dotenv

class SomeCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None

    @commands.command(name='hello')
    async def hello_world(self, ctx: commands.Context):
        await ctx.send('Hello!!')

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        start_time = time.time()
        message = await ctx.send("Pinging...")
        end_time = time.time()
        await message.edit(content=f"Pong! {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")

    @commands.command(name="setstatus")
    async def setstatus(self, ctx: commands.Context, *, text: str):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text))

    @commands.command(name="snipe")
    async def snipe(self, ctx: commands.Context):
        if not self.last_msg:
            await ctx.send("There is no message to snipe!")
            return

        author = self.last_msg.author
        content = self.last_msg.content

        embed = discord.Embed(title=f"Message from {author}", description=content)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member, message=None):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}. A DM has been sent to you, please check'.format(member))
            message = 'Klik huruf dibawah ini berdasarkan tema pelatihan yang diikuti (pilih/klik dengan teliti). \n :thumbsup: :-1: '
            await member.send(message)




    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.last_msg = message

def setup(bot: commands.Bot):
    bot.add_cog(SomeCommands(bot))

