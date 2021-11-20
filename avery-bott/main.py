import discord
import os
from dotenv import load_dotenv
from quart import Quart, render_template, session, request, redirect, url_for  
from oauth import Oauth
from quart_discord import DiscordOAuth2Session
import requests
from discord.ext import ipc

'''
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
'''
app=Quart(__name__)
ipc_client=ipc.Client(secret_key='secret-key')
app.config["SECRET_KEY"]="uhfiu8f7hw77298mom981"
app.config["DISCORD_CLIENT_ID"]="832188057742213152"
app.config["DISCORD_CLIENT_SECRET"]="ZODt24M3-W7pVfv7npuV5PIOutPSKtij"
app.config["DISCORD_REDIRECT_URI"]="http://127.0.0.1:5000/callback"

discord = DiscordOAuth2Session(app)




@app.route("/")
async def home():
	return await render_template("index.html", authorized = await discord.authorized)

@app.route("/login")
async def login():
	return await discord.create_session()

@app.route("/callback")
async def callback():
	try:
		await discord.callback()
	except Exception:
		pass

	return redirect(url_for("dashboard"))

@app.route("/dashboard")
async def dashboard():
	if not await discord.authorized:
		return redirect(url_for("login")) 

	guild_count = await ipc_client.request("get_guild_count")
	guild_ids = await ipc_client.request("get_guild_ids")

	user_guilds = await discord.fetch_guilds()

	guilds = []

	for guild in user_guilds:
		if guild.permissions.administrator:			
			guild.class_color = "green-border" if guild.id in guild_ids else "red-border"
			guilds.append(guild)

	guilds.sort(key = lambda x: x.class_color == "red-border")
	name = (await discord.fetch_user()).name
	return await render_template("dashboard.html", guild_count = guild_count, guilds = guilds, username=name)

@app.route("/dashboard/<int:guild_id>")
async def dashboard_server(guild_id):
    if not await discord.authorized:
        return redirect(url_for('login'))
    
    guild=await ipc_client.request('get_guild',guild_id=guild_id)
    if guild is None:
	    return redirect(f'https://discord.com/oauth2/authorize?&client_id={app.config["DISCORD_CLIENT_ID"]}&scope=bot&permissions=8&guild_id={guild_id}&response_type=code&redirect_uri={app.config["DISCORD_REDIRECT_URI"]}')
    return guild['name']


if __name__=="__main__":
    app.run(debug=True)
