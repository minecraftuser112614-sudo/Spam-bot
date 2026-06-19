# 🤖 ABHINAV DM BOT v2.0

A powerful Discord bot for sending DMs to users with support for **5 multiple bot tokens**. Perfect for Termux and other environments.

## ✨ Features

✅ **Multi-Token Support** - Use up to 5 Discord bot tokens simultaneously  
✅ **Environment Variables** - Secure token management with `.env` file  
✅ **Single DM** - Send a single message to any user  
✅ **Multiple DMs** - Send the same message multiple times (with count)  
✅ **Colored Output** - Beautiful terminal interface with colorama  
✅ **User ID & Message Input** - Easy to use menu-based interface  
✅ **Rate Limit Handling** - Built-in delays to avoid Discord rate limits  
✅ **Termux Compatible** - Works perfectly on Android with Termux  

---

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Discord bot tokens (create at [Discord Developer Portal](https://discord.com/developers/applications))

---

## 🚀 Installation

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install discord.py==2.3.2
pip install python-dotenv==1.0.0
pip install colorama==0.4.6
```

### Step 2: Configure Your Tokens

Edit the `.env` file and add your bot tokens:

```env
BOT_TOKEN_1=your_first_bot_token_here
BOT_TOKEN_2=your_second_bot_token_here
BOT_TOKEN_3=your_third_bot_token_here
BOT_TOKEN_4=your_fourth_bot_token_here
BOT_TOKEN_5=your_fifth_bot_token_here
```

**How to get a bot token:**
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to "Bot" section and click "Add Bot"
4. Copy the token under the bot name
5. Paste it in the `.env` file

### Step 3: Run the Bot

```bash
python3 abhinav_dm_bot.py
```

Or make it executable:

```bash
chmod +x abhinav_dm_bot.py
./abhinav_dm_bot.py
```

---

## 📖 Usage Guide

### Main Menu Options:

```
╔═══════════════════════════════════════════════════╗
║            🤖 ABHINAV DM BOT v2.0 🤖            ║
║                                                   ║
║      Send DMs to Discord Users with Tokens       ║
║                                                   ║
║            Multi-Token Support (5 Bots)          ║
╚═══════════════════════════════════════════════════╝

MAIN MENU
=======================================================
1. View Available Tokens
2. Send Single DM
3. Send Multiple DMs (by Count)
4. Reload Tokens from .env
5. Exit
=======================================================
```

### Option 1: View Available Tokens
- Shows all loaded bot tokens (masked for security)
- Displays how many tokens are currently active

### Option 2: Send Single DM
- Select which bot token to use (1-5)
- Enter the **User ID** (numeric Discord ID)
- Enter the **Message** (text to send)
- Bot sends the DM to the user

### Option 3: Send Multiple DMs
- Select which bot token to use (1-5)
- Enter the **User ID** (numeric Discord ID)
- Enter the **Message** (text to send)
- Enter the **Count** (how many times to send)
- Bot sends the message multiple times with 2-second delays

### Option 4: Reload Tokens
- Refreshes tokens from `.env` file without restarting

### Option 5: Exit
- Safely exits the application

---

## 🎯 Example Usage

### Send a Single DM:

```
Select Bot (number): 1
Enter User ID: 123456789
Enter Message: Hello! This is a test message.
✓ DM sent to username#1234
```

### Send Multiple DMs (5 times):

```
Select Bot (number): 2
Enter User ID: 987654321
Enter Message: Check out this cool bot!
Enter message count: 5

Sending 5 DMs to user 987654321...
⚠ WARNING: Sending too many messages may trigger Discord rate limits!
Continue? (yes/no): yes

[1/5] Sending...
✓ DM sent to cooluser#5678
[2/5] Sending...
✓ DM sent to cooluser#5678
... (continues)

✓ Completed - Sent: 5, Failed: 0
```

---

## 🔍 How to Get User ID

### Method 1: Enable Developer Mode
1. Open Discord Settings → Advanced
2. Enable **Developer Mode**
3. Right-click on a user → Copy User ID

### Method 2: Mention and Copy
1. Type `@username` in any server
2. Right-click the mention and copy the ID

---

## ⚙️ .env File Format

```env
# Discord Bot Tokens
BOT_TOKEN_1=MzA5NzY0NzEwMzQ5NzY0NzEw.C9IIqQ.xxxxxxxxxxxxxxxxxxxx
BOT_TOKEN_2=MzA5NzY0NzEwMzQ5NzY0NzEw.C9IIqQ.xxxxxxxxxxxxxxxxxxxx
BOT_TOKEN_3=MzA5NzY0NzEwMzQ5NzY0NzEw.C9IIqQ.xxxxxxxxxxxxxxxxxxxx
BOT_TOKEN_4=MzA5NzY0NzEwMzQ5NzY0NzEw.C9IIqQ.xxxxxxxxxxxxxxxxxxxx
BOT_TOKEN_5=MzA5NzY0NzEwMzQ5NzY0NzEw.C9IIqQ.xxxxxxxxxxxxxxxxxxxx
```

**⚠️ Important:** Never share your `.env` file or bot tokens publicly!

---

## 🐛 Troubleshooting

### Error: "No tokens loaded"
- Make sure `.env` file exists in the same directory as the bot script
- Check that tokens are formatted correctly
- Verify tokens are valid Discord bot tokens

### Error: "Cannot DM user"
- User's privacy settings may block DMs
- Bot may not have permission to DM in the server
- Check Discord bot permissions

### Error: "User not found"
- Verify the User ID is correct
- User ID must be numeric only
- Check that the user hasn't deleted their account

### Rate Limiting
- The bot adds 2-second delays between messages to prevent rate limiting
- If you get rate limit errors, increase the delay
- Don't send too many messages at once

### Invalid Token Error
- Copy your token again from Discord Developer Portal
- Make sure there are no extra spaces
- Token must start with "Mz..." or similar

---

## 📁 Project Structure

```
.
├── abhinav_dm_bot.py      # Main bot script
├── .env                   # Bot tokens (create this)
├── .env.example          # Example .env file
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

---

## 🔐 Security Tips

✅ **DO:**
- Keep your `.env` file private
- Use strong, unique tokens
- Don't share your bot tokens
- Add `.env` to `.gitignore` if using Git

❌ **DON'T:**
- Commit `.env` file to GitHub
- Share tokens in public channels
- Use tokens in public code repositories
- Leave the bot unattended with active tokens

---

## 📝 Requirements

- `discord.py` - Discord API wrapper
- `python-dotenv` - Environment variable management
- `colorama` - Colored terminal output

All requirements are listed in `requirements.txt`

---

## 💡 Tips & Tricks

1. **Test your bot first** - Send a test message to yourself
2. **Use multiple bots** - Different bots for different purposes
3. **Check user settings** - Some users may have DMs disabled
4. **Monitor rate limits** - Don't spam messages
5. **Reload tokens** - Use option 4 if you update `.env`

---

## ⚠️ Disclaimer

This tool is for **legitimate purposes only**. Users are responsible for:
- Complying with Discord Terms of Service
- Not using the bot for spam or harassment
- Following Discord's bot policies
- Respecting user privacy

Misuse of this bot may result in account termination by Discord.

---

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section above
2. Verify your `.env` file configuration
3. Make sure Python 3.8+ is installed
4. Check Discord Developer Portal for token validity

---

## 📄 License

This project is open-source and available for educational and personal use.

---

## 🙏 Credits

Created with ❤️ for Discord bot automation enthusiasts

---

**Made by: ABHINAV**  
**Version: 2.0**  
**Last Updated: 2026-06-19**
