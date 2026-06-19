#!/usr/bin/env python3
import discord
from discord.ext import commands
import asyncio
import os
from colorama import Fore, Style, init
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize colorama for colored output
init(autoreset=True)

# Store tokens from .env
TOKENS = []

def load_tokens_from_env():
    """Load bot tokens from .env file"""
    global TOKENS
    TOKENS = []
    
    for i in range(1, 6):
        token = os.getenv(f'BOT_TOKEN_{i}')
        if token and token != f'your_bot_token_{i}_here':
            TOKENS.append(token)
    
    return len(TOKENS)

def print_banner():
    """Display the bot banner - MASSIVE AND IMPRESSIVE"""
    banner = r"""
    
    
    
 ███████╗██████╗ █████╗ ███╗   ███╗     ██████╗  ██████╗ ████████╗    ██╗   ██╗██████╗ 
 ██╔════╝██╔══██╗██╔══██╗████╗ ████║    ██╔══██╗██╔═══██╗╚══██╔══╝    ██║   ██║╚════██╗
 ███████╗██████╔╝███████║██╔████╔██║    ██████╔╝██║   ██║   ██║       ██║   ██║ █████╔╝
 ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ██╔══██╗██║   ██║   ██║       ╚██╗ ██╔╝██╔═══╝ 
 ███████║██║     ██║  ██║██║ ╚═╝ ██║    ██████╔╝╚██████╔╝   ██║        ╚████╔╝ ███████╗
 ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝  ╚═════╝    ╚═╝         ╚═══╝  ╚══════╝

╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                ║
║                            🤖 ABHINAV ULTRA SPAM BOT v4.0 🤖                                                 ║
║                                                                                                                ║
║                         🚀 ALL BOTS • ALL AT ONCE • LIGHTNING FAST 🚀                                        ║
║                                                                                                                ║
║                   💥 Multiple Messages • Simultaneous Bots • Auto Mention 💥                                 ║
║                                                                                                                ║
║                        ⚡ FASTEST DM SPAM TOOL ON THE MARKET ⚡                                              ║
║                                                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    
    
"""
    print(Fore.CYAN + banner)

def print_menu():
    """Display the main menu"""
    print(Fore.GREEN + "\n" + "="*110)
    print(Fore.YELLOW + "                                        ⚡ MAIN MENU ⚡")
    print(Fore.GREEN + "="*110)
    print(Fore.WHITE + "  1️⃣  View Available Tokens")
    print(Fore.WHITE + "  2️⃣  🔥 SPAM USER - All Bots • Multiple Messages • Lightning Fast 🔥")
    print(Fore.WHITE + "  3️⃣  View Token Status")
    print(Fore.WHITE + "  4️⃣  Reload Tokens from .env")
    print(Fore.WHITE + "  5️⃣  Exit")
    print(Fore.GREEN + "="*110)

def view_tokens():
    """View all loaded tokens from .env"""
    if not TOKENS:
        print(Fore.RED + "\n✗ No tokens loaded! Check your .env file.\n")
        return
    
    print(Fore.GREEN + f"\n✓ Loaded {len(TOKENS)} Bot Token(s)")
    print(Fore.GREEN + "-"*110)
    for i, token in enumerate(TOKENS, 1):
        masked_token = token[:15] + "*" * (len(token) - 30) + token[-15:]
        print(Fore.YELLOW + f"  Bot {i}: {masked_token}")
    print(Fore.GREEN + "-"*110 + "\n")

def reload_tokens():
    """Reload tokens from .env file"""
    count = load_tokens_from_env()
    if count > 0:
        print(Fore.GREEN + f"\n✓ Successfully loaded {count} token(s) from .env file!\n")
    else:
        print(Fore.RED + "\n✗ No valid tokens found in .env file!\n")

async def send_dm(token, user_id, message):
    """Send a single DM using a token - ULTRA FAST"""
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    
    try:
        await client.login(token)
        user = await client.fetch_user(int(user_id))
        # Add @mention to message
        mention_msg = f"<@{user_id}> {message}"
        await user.send(mention_msg)
        await client.close()
        return True, f"✓ Sent"
    except discord.Forbidden:
        try:
            await client.close()
        except:
            pass
        return False, "✗ Privacy"
    except discord.NotFound:
        try:
            await client.close()
        except:
            pass
        return False, "✗ Not found"
    except discord.InvalidToken:
        try:
            await client.close()
        except:
            pass
        return False, "✗ Bad token"
    except Exception as e:
        try:
            await client.close()
        except:
            pass
        return False, f"✗ Error"

async def spam_user():
    """MAIN FEATURE: Spam user with ALL bots and multiple messages - ULTRA FAST"""
    if not TOKENS:
        print(Fore.RED + "\n✗ No tokens available! Load tokens first.\n")
        return
    
    try:
        print(Fore.CYAN + "\n" + "█"*110)
        print(Fore.YELLOW + "                       🔥 SPAM USER WITH ALL BOTS & MULTIPLE MESSAGES 🔥")
        print(Fore.CYAN + "█"*110 + "\n")
        
        user_id = input(Fore.CYAN + "Enter User ID to spam: ").strip()
        message = input(Fore.CYAN + "Enter Message: ").strip()
        count = int(input(Fore.CYAN + "Enter number of messages PER BOT: ").strip())
        
        if not user_id or not message or count <= 0:
            print(Fore.RED + "✗ Invalid input!\n")
            return
        
        total_messages = len(TOKENS) * count
        
        print(Fore.YELLOW + f"\n⚡ READY TO SEND {total_messages} MESSAGES!")
        print(Fore.YELLOW + f"   • User ID: {user_id}")
        print(Fore.YELLOW + f"   • Bots: {len(TOKENS)}")
        print(Fore.YELLOW + f"   • Messages per bot: {count}")
        print(Fore.YELLOW + f"   • Total messages: {total_messages}")
        print(Fore.RED + "   ⚠️  WARNING: This will SPAM the user heavily!")
        confirm = input(Fore.YELLOW + "\nContinue? (YES/NO): ").strip().lower()
        
        if confirm != "yes":
            print(Fore.YELLOW + "Cancelled!\n")
            return
        
        print(Fore.CYAN + "\n" + "█"*110)
        print(Fore.GREEN + "                              🚀 SENDING SPAM MESSAGES 🚀")
        print(Fore.CYAN + "█"*110 + "\n")
        
        total_success = 0
        total_failed = 0
        
        for msg_num in range(count):
            print(Fore.MAGENTA + f"▶ MESSAGE {msg_num + 1}/{count} - SENDING WITH ALL {len(TOKENS)} BOTS...")
            
            # Create tasks for ALL bots to send SIMULTANEOUSLY
            tasks = []
            bot_numbers = []
            
            for bot_idx, token in enumerate(TOKENS):
                task = send_dm(token, user_id, message)
                tasks.append(task)
                bot_numbers.append(bot_idx + 1)
            
            # Send all at the SAME TIME (concurrent)
            results = await asyncio.gather(*tasks)
            
            for bot_num, (success_flag, status) in zip(bot_numbers, results):
                if success_flag:
                    print(Fore.GREEN + f"     ✓ Bot {bot_num}: {status}", end="  ")
                    total_success += 1
                else:
                    print(Fore.RED + f"     {status} (Bot {bot_num})", end="  ")
                    total_failed += 1
            
            print()  # New line
            
            # NO DELAY - Send next batch immediately for LIGHTNING FAST speed
            if msg_num < count - 1:
                await asyncio.sleep(0.1)  # Minimal delay between message batches
        
        print(Fore.CYAN + "\n" + "█"*110)
        print(Fore.GREEN + "                              ✅ SPAM COMPLETE! ✅")
        print(Fore.CYAN + "█"*110)
        print(Fore.GREEN + f"\n  ✓ Total Messages Sent: {total_success}")
        print(Fore.RED + f"  ✗ Failed Messages: {total_failed}")
        print(Fore.YELLOW + f"  📊 Success Rate: {(total_success/(total_success+total_failed)*100):.1f}%\n")
        
    except ValueError:
        print(Fore.RED + "✗ Invalid input!\n")
    except Exception as e:
        print(Fore.RED + f"✗ Error: {str(e)}\n")

def view_token_status():
    """View detailed token status"""
    if not TOKENS:
        print(Fore.RED + "\n✗ No tokens loaded!\n")
        return
    
    print(Fore.GREEN + "\n" + "="*110)
    print(Fore.YELLOW + "                              TOKEN STATUS")
    print(Fore.GREEN + "="*110)
    print(Fore.WHITE + f"  Total Tokens Loaded: {len(TOKENS)}")
    print(Fore.WHITE + f"  Total Bots Available: {len(TOKENS)}")
    print(Fore.WHITE + f"  Status: ✅ READY TO SPAM")
    print(Fore.GREEN + "="*110 + "\n")

async def main():
    """Main program loop"""
    print_banner()
    
    # Load tokens on startup
    token_count = load_tokens_from_env()
    if token_count > 0:
        print(Fore.GREEN + f"\n✓✓✓ Loaded {token_count} bot token(s) from .env file!")
        print(Fore.YELLOW + f"⚡ Ready to send MASSIVE spam with ALL {token_count} bots!\n")
    else:
        print(Fore.RED + "\n✗✗✗ No tokens found in .env file!")
        print(Fore.YELLOW + "Please add bot tokens to .env file in format: BOT_TOKEN_1, BOT_TOKEN_2, etc.\n")
    
    while True:
        print_menu()
        choice = input(Fore.CYAN + "Enter choice: ").strip()
        
        if choice == "1":
            view_tokens()
        elif choice == "2":
            await spam_user()
        elif choice == "3":
            view_token_status()
        elif choice == "4":
            reload_tokens()
        elif choice == "5":
            print(Fore.YELLOW + "\n👋 Goodbye! Thanks for using SPAM BOT v4.0 👋\n")
            break
        else:
            print(Fore.RED + "\n✗ Invalid choice!\n")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\n⛔ Interrupted by user!")
    except Exception as e:
        print(Fore.RED + f"\n✗ Fatal error: {str(e)}")
