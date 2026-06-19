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
    """Display the bot banner"""
    banner = """
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║            🤖 ABHINAV DM BOT v2.0 🤖            ║
    ║                                                   ║
    ║      Send DMs to Discord Users with Tokens       ║
    ║                                                   ║
    ║            Multi-Token Support (5 Bots)          ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
    """
    print(Fore.CYAN + banner)

def print_menu():
    """Display the main menu"""
    print(Fore.GREEN + "\n" + "="*55)
    print(Fore.YELLOW + "MAIN MENU")
    print(Fore.GREEN + "="*55)
    print(Fore.WHITE + "1. View Available Tokens")
    print(Fore.WHITE + "2. Send Single DM")
    print(Fore.WHITE + "3. Send Multiple DMs (by Count)")
    print(Fore.WHITE + "4. Reload Tokens from .env")
    print(Fore.WHITE + "5. Exit")
    print(Fore.GREEN + "="*55)

def view_tokens():
    """View all loaded tokens from .env"""
    if not TOKENS:
        print(Fore.RED + "✗ No tokens loaded! Check your .env file.")
        return
    
    print(Fore.GREEN + f"\n✓ Loaded {len(TOKENS)} Bot Token(s)")
    print(Fore.GREEN + "-"*55)
    for i, token in enumerate(TOKENS, 1):
        masked_token = token[:15] + "*" * (len(token) - 30) + token[-15:]
        print(Fore.YELLOW + f"Bot {i}: {masked_token}")
    print(Fore.GREEN + "-"*55)

def reload_tokens():
    """Reload tokens from .env file"""
    count = load_tokens_from_env()
    if count > 0:
        print(Fore.GREEN + f"✓ Successfully loaded {count} token(s) from .env file!")
    else:
        print(Fore.RED + "✗ No valid tokens found in .env file!")

async def send_dm(token, user_id, message):
    """Send a single DM using a token"""
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    
    try:
        async with client:
            await client.login(token)
            user = await client.fetch_user(int(user_id))
            await user.send(message)
            print(Fore.GREEN + f"✓ DM sent to {user.name}#{user.discriminator}")
            return True
    except discord.Forbidden:
        print(Fore.RED + f"✗ Cannot DM user (privacy settings or bot permissions)")
        return False
    except discord.NotFound:
        print(Fore.RED + f"✗ User not found!")
        return False
    except discord.InvalidToken:
        print(Fore.RED + f"✗ Invalid token!")
        return False
    except discord.HTTPException as e:
        print(Fore.RED + f"✗ HTTP Error: {str(e)}")
        return False
    except Exception as e:
        print(Fore.RED + f"✗ Error: {str(e)}")
        return False

async def send_single_dm():
    """Send a single DM to a user"""
    if not TOKENS:
        print(Fore.RED + "✗ No tokens available! Load tokens first.")
        return
    
    try:
        print(Fore.CYAN + "\n--- Send Single DM ---")
        
        print(Fore.YELLOW + "Available Bot Tokens:")
        for i, token in enumerate(TOKENS, 1):
            masked = token[:15] + "*" * (len(token) - 30) + token[-15:]
            print(Fore.WHITE + f"{i}. {masked}")
        
        token_idx = int(input(Fore.CYAN + "Select Bot (number): ")) - 1
        if token_idx < 0 or token_idx >= len(TOKENS):
            print(Fore.RED + "✗ Invalid selection!")
            return
        
        user_id = input(Fore.CYAN + "Enter User ID: ").strip()
        message = input(Fore.CYAN + "Enter Message: ").strip()
        
        if not user_id or not message:
            print(Fore.RED + "✗ User ID and message required!")
            return
        
        print(Fore.YELLOW + "Sending DM...")
        await send_dm(TOKENS[token_idx], user_id, message)
        
    except ValueError:
        print(Fore.RED + "✗ Invalid input!")
    except Exception as e:
        print(Fore.RED + f"✗ Error: {str(e)}")

async def send_multiple_dms():
    """Send multiple DMs to a user"""
    if not TOKENS:
        print(Fore.RED + "✗ No tokens available! Load tokens first.")
        return
    
    try:
        print(Fore.CYAN + "\n--- Send Multiple DMs ---")
        
        print(Fore.YELLOW + "Available Bot Tokens:")
        for i, token in enumerate(TOKENS, 1):
            masked = token[:15] + "*" * (len(token) - 30) + token[-15:]
            print(Fore.WHITE + f"{i}. {masked}")
        
        token_idx = int(input(Fore.CYAN + "Select Bot (number): ")) - 1
        if token_idx < 0 or token_idx >= len(TOKENS):
            print(Fore.RED + "✗ Invalid selection!")
            return
        
        user_id = input(Fore.CYAN + "Enter User ID: ").strip()
        message = input(Fore.CYAN + "Enter Message: ").strip()
        count = int(input(Fore.CYAN + "Enter message count: ").strip())
        
        if not user_id or not message or count <= 0:
            print(Fore.RED + "✗ Invalid input!")
            return
        
        print(Fore.YELLOW + f"\nSending {count} DMs to user {user_id}...")
        print(Fore.RED + "⚠ WARNING: Sending too many messages may trigger Discord rate limits!")
        confirm = input(Fore.YELLOW + "Continue? (yes/no): ").strip().lower()
        
        if confirm != "yes":
            print(Fore.YELLOW + "Cancelled!")
            return
        
        success = 0
        failed = 0
        
        for i in range(count):
            print(Fore.CYAN + f"[{i+1}/{count}] Sending...")
            if await send_dm(TOKENS[token_idx], user_id, message):
                success += 1
            else:
                failed += 1
            await asyncio.sleep(2)  # 2 second delay between messages to avoid rate limiting
        
        print(Fore.GREEN + f"\n✓ Completed - Sent: {success}, Failed: {failed}")
        
    except ValueError:
        print(Fore.RED + "✗ Invalid input!")
    except Exception as e:
        print(Fore.RED + f"✗ Error: {str(e)}")

async def main():
    """Main program loop"""
    print_banner()
    
    # Load tokens on startup
    token_count = load_tokens_from_env()
    if token_count > 0:
        print(Fore.GREEN + f"✓ Loaded {token_count} bot token(s) from .env file!\n")
    else:
        print(Fore.RED + "✗ No tokens found in .env file!")
        print(Fore.YELLOW + "Please add bot tokens to .env file in format: BOT_TOKEN_1, BOT_TOKEN_2, etc.\n")
    
    while True:
        print_menu()
        choice = input(Fore.CYAN + "Enter choice: ").strip()
        
        if choice == "1":
            view_tokens()
        elif choice == "2":
            await send_single_dm()
        elif choice == "3":
            await send_multiple_dms()
        elif choice == "4":
            reload_tokens()
        elif choice == "5":
            print(Fore.YELLOW + "\nGoodbye! 👋")
            break
        else:
            print(Fore.RED + "✗ Invalid choice!")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\nInterrupted by user!")
    except Exception as e:
        print(Fore.RED + f"\n✗ Fatal error: {str(e)}")
