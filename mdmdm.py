import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} был забанен')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} был кикнут')

@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(role, reason=reason)
    await ctx.send(f'{member} замьючен')

@bot.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.remove_roles(role, reason=reason)
    await ctx.send(f'{member} размьючен')

@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f'{member} получил роль {role}')

@bot.command()
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    await ctx.send(f'{member} лишился роли {role}')


def has_role(ctx, role_name):
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    return role in ctx.author.roles


@bot.command()
@commands.check(lambda ctx: has_role(ctx, "Developer"))
async def command_name(ctx):
    await ctx.send("Только пользователи с определённой ролью могут использовать данную команду!")


bot.run('MTEwNDEyMjc0OTU0NDMwNDY0MA.G0SNSA.KeNmDDmQPO9dIg4CnQchvP8stZoKt-5R_lEMRo')