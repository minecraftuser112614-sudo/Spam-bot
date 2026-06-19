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
    """Display the bot banner - BIG AND IMPRESSIVE"""
    banner = """
    
    
╔════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                    ║
║     ███████╗██████╗ █████╗ ███╗   ███╗    ██████╗  ██████╗ ████████╗             ║
║     ██╔════╝██╔══██╗██╔══██╗████╗ ████║    ██╔══██╗██╔═══██╗╚══██╔══╝             ║
║     ███████╗██████╔╝███████║██╔████╔██║    ██████╔╝██║   ██║   ██║                ║
║     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ██╔══██╗██║   ██║   ██║                ║
║     ███████║██║     ██║  ██║██║ ╚═╝ ██║    ██████╔╝╚██████╔╝   ██║                ║
║     ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝  ╚═════╝    ╚═╝                 ║
║                                                                                    ║
║                          🤖 ABHINAV DM BOT v3.0 🤖                               ║
║                                                                                    ║
║                  🚀 ULTRA-FAST MULTI-TOKEN DM SENDER 🚀                          ║
║                                                                                    ║
║              📨 Lightning Speed • Auto Mention • Simultaneous Send 📨             ║
║                                                                                    ║
╚════════════════════════════════════════════════════════════════════════════════════╝
    
    
"""
    print(Fore.CYAN + banner)

def print_menu():
    """Display the main menu"""
    print(Fore.GREEN + "\n" + "="*80)
    print(Fore.YELLOW + "                             MAIN MENU")
    print(Fore.GREEN + "="*80)
    print(Fore.WHITE + "  1. View Available Tokens")
    print(Fore.WHITE + "  2. Send DM with Selected Tokens (with @mention)")
    print(Fore.WHITE + "  3. Send DM with ALL Tokens (with @mention)")
    print(Fore.WHITE + "  4. Send DM Multiple Times with COUNT (with @mention)")
    print(Fore.WHITE + "  5. Reload Tokens from .env")
    print(Fore.WHITE + "  6. Exit")
    print(Fore.GREEN + "="*80)

def view_tokens():
    """View all loaded tokens from .env"""
    if not TOKENS:
        print(Fore.RED + "\n✗ No tokens loaded! Check your .env file.\n")
        return
    
    print(Fore.GREEN + f"\n✓ Loaded {len(TOKENS)} Bot Token(s)")
    print(Fore.GREEN + "-"*80)
    for i, token in enumerate(TOKENS, 1):
        masked_token = token[:15] + "*" * (len(token) - 30) + token[-15:]
        print(Fore.YELLOW + f"  Bot {i}: {masked_token}")
    print(Fore.GREEN + "-"*80 + "\n")

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
        return True, f"✓ Sent to {user.name}"
    except discord.Forbidden:
        try:
            await client.close()
        except:
            pass
        return False, "✗ Cannot DM (privacy)"
    except discord.NotFound:
        try:
            await client.close()
        except:
            pass
        return False, "✗ User not found"
    except discord.InvalidToken:
        try:
            await client.close()
        except:
            pass
        return False, "✗ Invalid token"
    except Exception as e:
        try:
            await client.close()
        except:
            pass
        return False, f"✗ Error"

async def send_dm_with_selected_tokens():
    """Send DM to user using selected bot tokens - FAST"""
    if not TOKENS:
        print(Fore.RED + "\n✗ No tokens available! Load tokens first.\n")
        return
    
    try:
        print(Fore.CYAN + "\n--- Send DM with Selected Tokens ---")
        
        print(Fore.YELLOW + "\nAvailable Bot Tokens:")
        for i, token in enumerate(TOKENS, 1):
            masked = token[:15] + "*" * (len(token) - 30) + token[-15:]
            print(Fore.WHITE + f"  {i}. {masked}")
        
        # Get selected tokens
        print(Fore.CYAN + "\nEnter token numbers separated by commas (e.g., 1,2,3)")
        selection = input(Fore.CYAN + "Select tokens: ").strip()
        
        selected_indices = []
        for num_str in selection.split(','):
            try:
                idx = int(num_str.strip()) - 1
                if 0 <= idx < len(TOKENS):
                    selected_indices.append(idx)
            except ValueError:
                pass
        
        if not selected_indices:
            print(Fore.RED + "✗ No valid tokens selected!\n")
            return
        
        user_id = input(Fore.CYAN + "Enter User ID: ").strip()
        message = input(Fore.CYAN + "Enter Message: ").strip()
        
        if not user_id or not message:
            print(Fore.RED + "✗ User ID and message required!\n")
            return
        
        print(Fore.YELLOW + f"\n⚡ SENDING DM to user {user_id} with {len(selected_indices)} bot(s)...")
        print(Fore.YELLOW + "   (Auto-mentioning user in every message)\n")
        
        success = 0
        failed = 0
        
        # Send all at once (concurrent) for ULTRA FAST speed
        tasks = []
        indices_map = {}
        for idx in selected_indices:
            task = send_dm(TOKENS[idx], user_id, message)
            tasks.append(task)
            indices_map[len(tasks) - 1] = idx + 1
        
        results = await asyncio.gather(*tasks)
        
        for i, (success_flag, status) in enumerate(results):
            bot_num = indices_map[i]
            if success_flag:
                print(Fore.GREEN + f"  ✓ Bot {bot_num}: {status}")
                success += 1
            else:
                print(Fore.RED + f"  {status} (Bot {bot_num})")
                failed += 1
        
        print(Fore.GREEN + f"\n✓ COMPLETED - Success: {success}, Failed: {failed}\n")
        
    except Exception as e:
        print(Fore.RED + f"✗ Error: {str(e)}\n")

async def send_dm_with_all_tokens():
    """Send DM to user using ALL bot tokens at once - ULTRA FAST"""
    if not TOKENS:
        print(Fore.RED + "\n✗ No tokens available! Load tokens first.\n")
        return
    
    try:
        print(Fore.CYAN + "\n--- Send DM with ALL Tokens ---")
        
        user_id = input(Fore.CYAN + "\nEnter User ID: ").strip()
        message = input(Fore.CYAN + "Enter Message: ").strip()
        
        if not user_id or not message:
            print(Fore.RED + "✗ User ID and message required!\n")
            return
        
        print(Fore.YELLOW + f"\n⚡ SENDING DM to user {user_id} with ALL {len(TOKENS)} bot(s)...")
        print(Fore.YELLOW + "   (Auto-mentioning user in every message)\n")
        
        success = 0
        failed = 0
        
        # Send DM with all tokens SIMULTANEOUSLY for ULTRA FAST speed
        tasks = []
        for idx, token in enumerate(TOKENS):
            task = send_dm(token, user_id, message)
            tasks.append((idx + 1, task))
        
        results = await asyncio.gather(*[task for _, task in tasks])
        
        for (bot_num, _), (success_flag, status) in zip(tasks, results):
            if success_flag:
                print(Fore.GREEN + f"  ✓ Bot {bot_num}: {status}")
                success += 1
            else:
                print(Fore.RED + f"  {status} (Bot {bot_num})")
                failed += 1
        
        print(Fore.GREEN + f"\n✓ COMPLETED - Success: {success}, Failed: {failed}\n")
        
    except Exception as e:
        print(Fore.RED + f"✗ Error: {str(e)}\n")

async def send_dm_multiple_times():
    """Send DM multiple times using all tokens - FAST"""
    if not TOKENS:
        print(Fore.RED + "\n✗ No tokens available! Load tokens first.\n")
        return
    
    try:
        print(Fore.CYAN + "\n--- Send DM Multiple Times ---")
        
        user_id = input(Fore.CYAN + "\nEnter User ID: ").strip()
        message = input(Fore.CYAN + "Enter Message: ").strip()
        count = int(input(Fore.CYAN + "Enter message count: ").strip())
        
        if not user_id or not message or count <= 0:
            print(Fore.RED + "✗ Invalid input!\n")
            return
        
        print(Fore.YELLOW + f"\n⚡ SENDING {count} DMs to user {user_id} with ALL {len(TOKENS)} bot(s)...")
        print(Fore.YELLOW + "   (Auto-mentioning user in every message)")
        print(Fore.RED + "   ⚠ WARNING: This may trigger Discord rate limits!\n")
        confirm = input(Fore.YELLOW + "Continue? (yes/no): ").strip().lower()
        
        if confirm != "yes":
            print(Fore.YELLOW + "Cancelled!\n")
            return
        
        total_success = 0
        total_failed = 0
        
        for count_num in range(count):
            print(Fore.CYAN + f"\n[{count_num + 1}/{count}] Sending with ALL {len(TOKENS)} bots...")
            
            # Send all bots SIMULTANEOUSLY for each iteration
            tasks = []
            for idx, token in enumerate(TOKENS):
                task = send_dm(token, user_id, message)
                tasks.append((idx + 1, task))
            
            results = await asyncio.gather(*[task for _, task in tasks])
            
            for (bot_num, _), (success_flag, status) in zip(tasks, results):
                if success_flag:
                    print(Fore.GREEN + f"    ✓ Bot {bot_num}: {status}")
                    total_success += 1
                else:
                    print(Fore.RED + f"    {status} (Bot {bot_num})")
                    total_failed += 1
            
            # Fast delay between iterations
            if count_num < count - 1:
                await asyncio.sleep(0.5)
        
        print(Fore.GREEN + f"\n✓ COMPLETED - Total Success: {total_success}, Failed: {total_failed}\n")
        
    except ValueError:
        print(Fore.RED + "✗ Invalid input!\n")
    except Exception as e:
        print(Fore.RED + f"✗ Error: {str(e)}\n")

async def main():
    """Main program loop"""
    print_banner()
    
    # Load tokens on startup
    token_count = load_tokens_from_env()
    if token_count > 0:
        print(Fore.GREEN + f"\n✓ Loaded {token_count} bot token(s) from .env file!")
        print(Fore.YELLOW + "Ready to send DMs with ultra-fast speed!\n")
    else:
        print(Fore.RED + "\n✗ No tokens found in .env file!")
        print(Fore.YELLOW + "Please add bot tokens to .env file in format: BOT_TOKEN_1, BOT_TOKEN_2, etc.\n")
    
    while True:
        print_menu()
        choice = input(Fore.CYAN + "Enter choice: ").strip()
        
        if choice == "1":
            view_tokens()
        elif choice == "2":
            await send_dm_with_selected_tokens()
        elif choice == "3":
            await send_dm_with_all_tokens()
        elif choice == "4":
            await send_dm_multiple_times()
        elif choice == "5":
            reload_tokens()
        elif choice == "6":
            print(Fore.YELLOW + "\nGoodbye! 👋\n")
            break
        else:
            print(Fore.RED + "\n✗ Invalid choice!\n")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\nInterrupted by user!")
    except Exception as e:
        print(Fore.RED + f"\n✗ Fatal error: {str(e)}")
