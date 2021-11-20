# repl-hosted-discord-bot
A slapdash discord bot for a spelling bee hosted on repl by taking advantage of repl's specific features.  
  
The discord bot simply deletes messages from a defined "Responses" channel where participants type in their answer.  
These deleted messages are then reposted to a private channel only accessible by mods.  
This effectively results in a write-only text-channel where people can send messages, but can't read any messages.  


## Hosting on repl.it  
repl.it provides users with a way to execute their code, this includes live discord bots.  
The only issue is that repl.it terminates the execution after an hour of inactivity, as a result, hosting a discord bot on repl can't be done directly.
### The workaroaund:  
keepAlive.py runs a webserver on a different thread, parallel to the discord bot. This webserver can be pinged using a free monitor provided by .
Since the webserver is pinged every 10 minutes, repl.it never times out, and it doesn't terminate the execution.  
The end result? A discord bot hosted indeterminately on repl.it.  
### Uptime Robot Setup:  
Run the code on repl.it and grab the URL for the webserver:
![image](https://user-images.githubusercontent.com/60308157/114558170-09460080-9c88-11eb-9483-367e5a7960b2.png)
Create a monitor on https://uptimerobot.com/ with the following settings(select any interval you're comfortable with):
![image](https://user-images.githubusercontent.com/60308157/114558445-4dd19c00-9c88-11eb-99d4-4fe8c1494498.png)
The monitor will ping the webserver and keep it up indefinitely.


## Avery Bott
Avery bott is a practice bot to test discord bot dashboards
