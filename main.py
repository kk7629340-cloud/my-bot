import json
import asyncio
import importlib.util
import os
import random

from highrise import *
from highrise import BaseBot, Position, User, __main__
from highrise.models import *
from highrise.models import (
    Item,
    Position,
    SessionMetadata,
    User,
)
from flask import Flask
from threading import Thread
from highrise.__main__ import BotDefinition
from highrise import *
from highrise.models import *
from asyncio import run as arun
from flask import Flask
from threading import Thread
import highrise
from highrise.__main__ import *

import random
import random
import time
from webserver import keep_alive
import traceback
MESSAGES = [ "dance-orangejustice"]
queeno = ["90HB"]
name_boss = ["90HB","Q._M3","2005__2"]
dabi = ["90HB"]
from mac import*
from mac import emote_map
     
class BotDefinition:
    def __init__(self, bot, room_id, api_token):
      self.bot = bot
      self.room_id = room_id
      self.api_token = api_token
      self.is_dancing = False

      self.emote_looping = False
      self.user_emote_loops = {}
      self.loop_task = None
class MyBot(BaseBot):

  def __init__(self, bot, room_id, api_token):
      self.bot = bot
      self.room_id = room_id
      self.api_token = api_token
      
      self.user_positions = {}
      
      self.user_emote_loops = {} 
      self.position_tasks = {}    
      self.reset_target_position = {}  
      self.locked_users = {} 
       # Store the custom welcome messages for each mod
      self.is_dancing = False

      self.emote_looping = False
      self.user_emote_loops = {}
      self.loop_task = None
      self.user_emote_loops = {}
      
# Load VIP users from the file
   
  message_count = {}
  
  


  greetings = [
  


   
    "حي من جانا ❤ 💕",
    
   
    
"ما تبلي هالطلة ❤ ♥🔥",
    "يلهوي عل القمر اللي دخل🫣♥",
    "فديت قلبك نورت يانجم الكوكب😉💕  ❤️",
   
   
  ]
 


  dancs = [
      "idle-loop-sitfloor", "emote-tired", "emote-pose7", "emoji-thumbsup",
      "emoji-angry", "dance-macarena", "emote-hello", "dance-weird",
      "emote-superpose", "idle-lookup", "idle-hero", "emote-wings",
      "emote-laughing", "emote-kiss", "emote-wave", "emote-hearteyes",
      "emote-theatrical", "emote-teleporting", "emote-slap", "emote-ropepull",
      "emote-think", "emote-hot", "dance-shoppingcart", "emote-greedy",
      "emote-frustrated", "emote-float", "emote-baseball", "emote-yes",
      "idle_singing", "idle-floorsleeping", "idle-loop-sitfloor",
      "idle-enthusiastic", "emote-confused", "emoji-celebrate", "emote-no",
      "emote-swordfight", "emote-shy", "dance-tiktok2", "emote-model",
      "emote-charging", "emote-snake", "dance-russian", "emote-sad",
      "emote-lust", "emoji-cursing", "emoji-flex", "emoji-gagging",
      "dance-tiktok8", "dance-blackpink", "dance-pennywise", "emote-bow",
      "emote-curtsy", "emote-snowball", "emote-snowangel", "emote-telekinesis",
      "idle-dance-tiktok4"
      "emote-maniac", "emote-energyball", "emote-frog", "emote-cute",
      "dance-tiktok9", "dancممنوعشرفينiktok10", "emote-pose7", "emote-pose8",
      "idle-dance-casual", "emote-pose1", "dance-sexy", "emote-pose3",
      "emote-pose5", "emote-cutey", "emote-Relaxing", "emote-model",
      "emote-fashionista", "emote-gravity", "emote-zombierun",
      "emoji-ceilebrate", "emoji-floss", "emote-Relaxing ", "emote-punkguitar",
      "dance-tiktok9", "dance-weird", "emote-punkguitar", "idle-uwu"
      "emote-swordfight", "emote-handstand", "emote-bow", "emote-cursty",
      "dance-breakdance", "emote-creepycute", "emote-headblowup", "idle-guitar"
  ]
  dans = [
    "emote-shrink",
      "dance-blackpink",
      "emote-punkguitar",
      "emote-telekinesis",
      "dance-tiktok2",
      "dance-tiktok8",
      "dance-weird",
      "dance-russian",
      "idle_singing",
      "idle-dance-casual",
    "emote-jinglehop"
  ]

  async def emote_loop(self):
          while True:
              try:
                  emote_name = random.choice(list(paid_emotes.keys()))
                  emote_to_send = paid_emotes[emote_name]["value"]
                  emote_time = paid_emotes[emote_name]["time"]

                  await self.highrise.send_emote(emote_id=emote_to_send)                  
                  await asyncio.sleep(emote_time)
              except Exception as e:
                  print("Error sending emote:", e) 
  async def start_emote_with_target(self, initiator_id: str, target_id: str, emote_name: str) -> None:
                                """
                                Starts an emote involving the initiator and the target user.
                                """
                                self.user_emote_loops[initiator_id] = emote_name
                                self.user_emote_loops[target_id] = emote_name

                                emote_info = emote_mapping.get(emote_name)
                                if not emote_info:
                                    print(f"Emote '{emote_name}' not found.")
                                    return

                                emote_to_send = emote_info["value"]
                                emote_time = emote_info["time"]

                                while (self.user_emote_loops.get(initiator_id) == emote_name and 
                                       self.user_emote_loops.get(target_id) == emote_name):
                                    try:
                                        # Send emote to both users
                                        await self.highrise.send_emote(emote_to_send, initiator_id)
                                        await self.highrise.send_emote(emote_to_send, target_id)
                                        await asyncio.sleep(emote_time)
                                    except Exception as e:
                                        print(f"Error sending emote to users: {e}")
                                        break





  async def on_user_leave(self, user: User) -> None:
    await self.highrise.chat(f"ذهب {user.username} من الغرفه 🥺")
    await self.highrise.send_emote("emote-sad")    

  async def stop_emote_with_target(self, user_id: str) -> None:
                                """
                                Stops the emote loop for the user and their target.
                                """
                                if user_id in self.user_emote_loops:
                                    del self.user_emote_loops[user_id]

   
  async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:
    # الحصول على الرسائل في المحادثة باستخدام معرف المحادثة
    response = await self.highrise.get_messages(conversation_id)

    # التحقق مما إذا كانت الاستجابة من النوع المتوقع
    if isinstance(response, GetMessagesRequest.GetMessagesResponse):
        # استخراج محتوى الرسالة الأخيرة من المحادثة
        message = response.messages[0].content

        # التحقق مما إذا كانت الرسالة تساوي "Hello"
        if message == "الاوامر":
            # إرسال رد برسالة "Hello World!" إلى نفس المحادثة
            await self.highrise.send_message(conversation_id, "مرحبا بكم اوامر البوت 1-اعطيني قلب 2-رقصني 3-الاذكار 4-صعدني 5-نزلني 6-ارقام الرقص من 1/113, 7-صيغه تكرار الرقصه loop ")

    
  async def unlock_user(self, message: str) -> None:
        """
        Unlocks a user, allowing them to move freely.
        Usage: unlock @username
        """
        try:
            _, mention = message.split(" ", 1)
            if not mention.startswith("@"):
                await self.highrise.chat("Incorrect content. Use 'unlock @username'")
                return

            username = mention[1:]  # Remove the '@' symbol
        except ValueError:
            await self.highrise.chat("Incorrect format. Use 'unlock @username'")
            return

        # Get the list of users in the room
        room_users = (await self.highrise.get_room_users()).content

        # Find the target user's ID
        user_id = None
        for user_entry in room_users:
            if user_entry[0].username.lower() == username.lower():
                user_id = user_entry[0].id
                break

        if not user_id:
            await self.highrise.chat(f"User '{username}' not found in the room.")
            return
      
        # Remove the user from the locked list
        if user_id in self.locked_users:
            del self.locked_users[user_id]
            await self.highrise.chat(f"تم التحرير {username}. يمكنك التحرك الان.")
        else:
            await self.highrise.chat(f"User '{username}' is not locked.")      
  async def lock_user(self, message: str) -> None:
        """
        Locks a user to their current position.
        Usage: lock @username
        """
        try:



            
            # Extract username from the command
            _, mention = message.split(" ", 1)
            if not mention.startswith("@"):
                await self.highrise.chat("Incorrct format. Use 'lock @username'")
                return

            username = mention[1:]  # Remove the '@' symbol
        except ValueError:
            await self.highrise.chat("Incorrect format. Use 'lock @username'")
            return

        # Get the list of users in the room
        room_users = (await self.highrise.get_room_users()).content

        # Find the target user's ID and current position
        user_id = None
        user_position = None
        for user_entry in room_users:
            if user_entry[0].username.lower() == username.lower():
                user_id = user_entry[0].id
                user_position = user_entry[1]  # Position of the user
                break

        if not user_id or not user_position:
            await self.highrise.chat(f"User '{username}' not found in the room.")
            return

        # Lock the user to their current position
        self.locked_users[user_id] = user_position
        await self.highrise.chat(f"لا يمكنك التحرك الان {username} تم تثبيتك ({user_position.x}, {user_position.y}, {user_position.z}).")

  async def on_user_move(self, user: User, destination: Position) -> None:
                    if user.id in self.locked_users:
                        fixed_position = self.locked_users[user.id]
                        

                        # Handle different types of position objects


                        
                        if isinstance(destination, Position) and isinstance(fixed_position, Position):
                            # Check if the user has moved from the locked position
                            if (
                                round(destination.x, 1) != round(fixed_position.x, 1)
                                or round(destination.y, 1) != round(fixed_position.y, 1)
                                or round(destination.z, 1) != round(fixed_position.z, 1)
                            ):
                                # Teleport the user back to the locked position
                                try:
                                    await self.highrise.teleport(user_id=user.id, dest=fixed_position)
                                except Exception as e:
                                    print(f"Error teleporting user {user.username}: {e}")

                        elif isinstance(destination, AnchorPosition) and isinstance(fixed_position, AnchorPosition):
                            # Handle anchor e}: { if necessary
                            if destination != fixed_position:
                                try:
                                    await self.highrise.teleport(user_id=user.id, dest=fixed_position)
                                except Exception as e:
                                    print(f"Error teleporting user {user.username}: {e}")

                        else:
                            print(f"Unsupported position type for user {user.username}.")
     

  
  async def on_start(self, session_metadata: SessionMetadata) -> None:
    print("[harby]")
      
    try:
      await self.highrise.walk_to(Position(1, 4.0, 0, facing='FrontRight'))
      
    except Exception as e:
      print(f"An exception occurred: {e}")
      
  async def on_whisper(self, user: User
                       , message: str) -> None:
          """On a received room whisper."""
          if await self.is_user_allowed(user) and message.startswith(''):
              try:
                  xxx = message[0:]
                  await self.highrise.chat(xxx)
              except:
                  print("error 3")

  async def is_user_allowed(self, user: User) -> bool:
          user_privileges = await self.highrise.get_room_privilege(user.id)
          return user_privileges.moderator or user.username in ["90HB"] 
  async def command_handler(self, user: User, message: str):
      parts = message.lower().split(" ")
      command = parts[0]
      functions_folder = "pop"
      # Check if the function exists in the module
      for file_name in os.listdir(functions_folder):
        if file_name.endswith(".py"):
          module_name = file_name[:-3]  # Remove the '.py' extension
          module_path = os.path.join(functions_folder, file_name)

          # Load the module
          spec = importlib.util.spec_from_file_location(module_name, module_path)
          module = importlib.util.module_from_spec(spec)
          spec.loader.exec_module(module)

          # Check if the function exists in the module
          if hasattr(module, command) and callable(getattr(module, command)):
            function = getattr(module, command)
            await function(self, user, message)

      # If no matching function is found
      return  
  
       
  async def on_user_join(self, user: User, position: str) -> None:
    
    try:
        await self.highrise.send_whisper(user.id, "مرحبا بكم في روم ادخل واستمتع معنا 🤍💕")
        await self.highrise.react("heart", user.id)        
        await self.highrise.send_emote("emote-tapdanc")
        await self.highrise.react("wave", user.id)        
        await self.highrise.send_emote("emoji-angry")
        await self.highrise.react("wave", user.id)        
        await self.highrise.send_emote("emote-bow")
        await self.highrise.react("wave", user.id)        
        await self.highrise.send_emote("dance-hipshake")
        await self.highrise.react("wave", user.id)        
        await self.highrise.send_emote("emote-ghost-idle")
        await self.highrise.react("wave", user.id)       
        await self.highrise.send_emote("dance-woah")  
    except Exception as e:
        print(f"Error: {e}") 
    try:
        emote_id = random.choice(self.dancs)
        await self.highrise.send_emote(emote_id, user.id)
    except:
        print(f"{emote_id}")            
    
    try:
      room_users = (await self.highrise.get_room_users()).content
      user_present = any(u[0].id == user.id for u in room_users)
      if user_present:

        greeting = random.choice(self.greetings)
        await self.highrise.chat(f"{greeting}، {user.username}!") #change welcome to this room
        
      else:
        print("User has left the room")
    except:
      print("Error sending whisper")
         
  async def on_chat(self, user: User, message: str) -> None:        
    if user.username == "u4n_":
      await self.highrise.chat("للحصول عل صلاحية (vip) قوم بي ارسل 50 قولد صلاحية لمده اسبوع❤💕  ♥")
      await self.highrise.send_emote("dance-orangejustice") 
    await asyncio.sleep(1)                    
    if "@" in message:
             parts = message.split("@")
             if len(parts) < 2:
                 return  # Invalid command format

             emote_name = parts[0].strip()
             target_username = parts[1].strip()

             # Verify the emote name and target user
             if emote_name in emote_map:
                 response = await self.highrise.get_room_users()
                 users = [content[0] for content in response.content]
                 usernames = [user.username.lower() for user in users]

                 if target_username not in usernames:
                     return  # Target user not found in the room

                 target_user_id = next((u.id for u in users if u.username.lower() == target_username), None)
                 if not target_user_id:
                     return

                 # Start the emote loop with the target user
                 await self.start_emote_with_target(user.id, target_user_id, emote_name)

    elif message in ["stop", "وقف" ,"0"]:
                                    # Stop the emote loop for the user
              await self.stop_emote_with_target(user.id)
    
    user_privileges = await self.highrise.get_room_privilege(user.id)
    
    message = message.strip().lower()
    user_id = user.id

    # Handle mass heart reaction for "H @username"
    if "قلوب" in message or "heart" in message:
        
        if (not user_privileges.moderator) and (user.username != "90HB"):
               await self.highrise.chat("انت لست مشرف لا يمكنك استخدام هذا الامر" )
               return
            
        parts = message.split("@")
        if len(parts) < 2:
            return  # Invalid command format

        target_username = parts[1].strip()

        # Get list of users in the room
        room_users = (await self.highrise.get_room_users()).content
        usernames = [u[0].username.lower() for u in room_users]

        if target_username.lower() not in usernames:
            await self.highrise.chat(f"{target_username} ليس في الغرفه الان.")
            return  # Target user not found

        target_user_id = next((u[0].id for u in room_users if u[0].username.lower() == target_username.lower()), None)
        if target_user_id:
            for _ in range(50):  # Send 50 hearts in a row
                await self.highrise.react("heart", target_user_id)
                await asyncio.sleep(0.0)  # Adjusted delay for faster reactions


    if "غمزة" in message or "winky" in message:
        
        if (not user_privileges.moderator) and (user.username != "90HB"):
               await self.highrise.chat("انت لست مشرف لا يمكنك استخدام هذا الامر" )
               return
            
        parts = message.split("@")
        if len(parts) < 2:
            return  # Invalid command format

        target_username = parts[1].strip()

        # Get list of users in the room
        room_users = (await self.highrise.get_room_users()).content
        usernames = [u[0].username.lower() for u in room_users]

        if target_username.lower() not in usernames:
            await self.highrise.chat(f"{target_username} ليس في الغرفه الان.")
            return  # Target user not found

        target_user_id = next((u[0].id for u in room_users if u[0].username.lower() == target_username.lower()), None)
        if target_user_id:
            for _ in range(50):  # Send 50 hearts in a row
                await self.highrise.react("wink", target_user_id)
                await asyncio.sleep(0.0)  # Adjusted delay for faster reactions
    
      
    emote_mapping = {
                  1: "emoji-angry",
                  2: "emote-bow",
                  3: "idle-dance-casual",
                  4: "emoji-celebrate",
                  5: "emote-charging",
                  6: "emote-confused",
                  7: "emoji-cursing",
                  8: "emote-curtsy",
                  9: "emote-cutey",
                  10: "emote-snake",
                  11: "emote-cute",
                  12: "emote-energyball",
                  13: "idle-enthusiastic",
                  14: "emote-fashionista",
                  15: "emoji-mind-blown",
                  16: "emote-float",
                  17: "emote-frog",
                  18: "emoji-gagging",
                  19: "emote-gravity",
                  20: "emote-greedy",
                  21: "emote-hello",
                  22: "emote-hot",
                  23: "dance-icecream",
                  24: "emote-kiss",
                  25: "dance-blackpink",
                  26: "emote-laughing",
                  27: "emote-lust",
                  28: "dance-macarena",
                  29: "emote-maniac",
                  30: "emote-model",
                  31: "emote-no",
                  32: "emote-pose1",
                  33: "emote-pose3",
                  34: "emote-pose5",
                  35: "emote-pose7",
                  36: "emote-pose8",
                  37: "emote-punkguitar",
                  38: "dance-russian",
                  39: "emote-sad",
                  40: "idle-dance-tiktok4",
                  41: "dance-shoppingcart",
                  42: "emote-shy",
                  43: "idle-loop-sitfloor",
                  44: "emote-snowangel",
                  45: "emote-snowball",
                  46: "emote-superpose",
                  47: "emote-telekinesis",
                  48: "emote-teleporting",
                  49: "emoji-thumbsup",
                  50: "emote-tired",
                  51: "idle-uwu",
                  52: "emote-wave",
                  53: "dance-weird",
                  54: "dance-wrong",
                  55: "emote-yes",
                  56: "emote-astronaut",
                  57: "dance-pennywise",
                  58: "emote-zombierun",
                  59: "emote-swordfight",
                  60: "idle_singing",
                  61: "dance-tiktok8",
                  62: "dance-tiktok2",
                  63: "dance-tiktok10",
                  64: "dance-tiktok9",
                  65: "dance-pinguin",
                  66: "idle-guitar",
                  67: "emote-stargazer",
                  68: "emote-boxer",
                  69: "dance-creepypuppet",
                  70: "dance-anime",
                  71: "emote-creepycute",
                  72: "emote-headblowup",
                  73: "emote-shy2",
                  74: "emote-celebrate",
                  75: "emote-pose10",
                  76: "emote-iceskating",
                  77: "idle-wild",
                  78: "idle-nervous",
                  79: "emote-timejump",
                  80: "idle-toilet",
                  81: "dance-jinglebell",
                  82: "emote-hyped",
                  83: "emote-sleigh",
                  84: "emote-pose6",
                  85: "dance-kawai",
                  86: "dance-touch",
                  87: "sit-relaxed",
                  88: "emote-celebrationstep",
                  89: "dance-employee",
                  90: "emote-launch",
                  91: "emote-cutesalute",
                  92: "emote-salute",
                  93: "dance-tiktok11",
                  94: "emote-gift",
                  95: "emote-pose9",
                  96: "emote-kissing-bound",
                  97: "dance-woah",
                  98: "dance-aerobics",
                  99: "emote-gordonshuffle",
                  100: "dance-smoothwalk",
                  101: "emote-ghost-idle",
                  102: "idle-floorsleeping2",
                  103: "idle_layingdown",
                  104: "idle-floorsleeping",
                  105: "idle-loop-aerobics",
                  106: "emote-shrink",
                  107: "dance-cheerleader",
                  108: "emote-puppet",
                  109: "sit-open",
                  110: "dance-hipshake",
                  111: "dance-orangejustice",
                  112: "idle-uwu",
                  113: "sit-idle-phone-text" 
 
    
        
              }
    if message.isdigit():  # Checks if the message is purely numeric
               try:
                   # Convert the message to an integer (the number the user typed)
                   chosen_number = int(message)

                   # Get the corresponding emote from the mapping
                   emote_id = emote_mapping.get(chosen_number)

                   if emote_id:
                       # Send the corresponding emote to the user
                       await self.highrise.send_emote(emote_id, user.id)
                   else:
                       await self.highrise.send_message(user.id, "رقم الرقصه غير صالح")

               except Exception as e:
                  await self.highrise.send_message(user.id, f"Error: {str(e)}")
    
    
    parts = message.lower().split(" ")
    if len(parts) > 0:
          command = parts[0]
          await self.command_handler(user, message)
    if message.startswith("/moveall @"):
        if user.username ==  "u4n_":

          at_index = message.find("@")
            
          if at_index != -1:
              extracted_text = message[at_index+1:]
              if extracted_text.lower() in self.rooms_list:
                destination_room_id = self.rooms_list[extracted_text.lower()]
              else:
                await self.highrise.chat(f"Error: Unknown room {extracted_text}")
                return
              room_users = (await self.highrise.get_room_users()).content
              try:
                for user_data, position in room_users:
                  user_id = user_data.id
                  await self.highrise.move_user_to_room(user_id, destination_room_id)
              except Exception as e:
                  await self.highrise.chat("Error: the bot might not be authorised to move users to that room")   

    if message.startswith("movللe") and user.username in name_boss:
        room_dictionary = {"room_1": "68bb81b6b3ad4d2c8d06e70d",
                             "room_2": "68bb81b6b3ad4d2c8d06e70d",}
        
        parts = message.split()
        if len(parts) != 3:
            await self.highrise.chat("Invalid move command format.")
            return
        command, username, room = parts
        username = username if "@" not in username else username[1:]
        if room not in room_dictionary:
            await self.highrise.chat("Invalid room, please specify a valid room.")
            return
          #check if user is in room
        room_users = (await self.highrise.get_room_users()).content
        for room_user, _pos in room_users:
            if room_user.username.lower() == username.lower():
                user_id = room_user.id
                break
        if "user_id" not in locals():
            await self.highrise.chat("User not found, please specify a valid user and coordinate")
            return
          #move user
        try:
            await self.highrise.move_user_to_room(user_id, room_dictionary[room])
        except Exception as e:
            await self.highrise.chat(f"Error: {e}")
            return

    if message.startswith("promote"):
            if user.username != "u4n_":
                await self.highrise.chat("You do not have permission to use this command.")
                return
            parts = message.split()
            if len(parts) != 3:
                await self.highrise.chat("Invalid promote command format.")
                return
            command, username, role = parts
            if "@" not in username:
                username = username
            else:
                username = username[1:]
            if role.lower() not in ["moderator", "designer"]:
                await self.highrise.chat("Invalid role, please specify a valid role.")
                return
            #check if user is in room
            room_users = (await self.highrise.get_room_users()).content
            for room_user, pos in room_users:
                if room_user.username.lower() == username.lower():
                    user_id = room_user.id
                    break
            if "user_id" not in locals():
                await self.highrise.chat("User not found, please specify a valid user and coordinate")
                return
            #promote user
            permissions = (await self.highrise.get_room_privilege(user_id))
            setattr(permissions, role.lower(), True)
            try:
                await self.highrise.change_room_privilege(user_id, permissions)
                await self.highrise.chat(f"{username} has been promoted to {role}.")
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")
                return
            
    if message.startswith("demote"):
            if user.username != "90HB":
                await self.highrise.chat("ليس لديك الاذن لتفيذ الطلب.")
                return
            parts = message.split()
            if len(parts) != 3:
                await self.highrise.chat("تنسيق الامر خطاء.")
                return
            command, username, role = parts
            if "@" not in username:
                username = username
            else:
                username = username[1:]
            if role.lower() not in ["moderator", "designer"]:
                await self.highrise.chat("Invalid role, please specify a valid role.")
                return
            #check if user is in room
            room_users = (await self.highrise.get_room_users()).content
            for room_user, pos in room_users:
                if room_user.username.lower() == username.lower():
                    user_id = room_user.id
                    break
            if "user_id" not in locals():
                await self.highrise.chat("User not found, please specify a valid user and coordinate")
                return
            #promote user
            permissions = (await self.highrise.get_room_privilege(user_id))
            setattr(permissions, role.lower(), False)
            try:
                await self.highrise.change_room_privilege(user_id, permissions)
                await self.highrise.chat(f"{username} has been demoted from {role}.")
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")
                return 
                
    user_privileges = await self.highrise.get_room_privilege(user.id)
    message = message.strip().lower()

    try:
    
       if message().startswith(("تستس")):
           if (not user_privileges.moderator) and (user.username != "90HB"):
               await self.highrise.chat("انت لست مشرفا لاستخدام الامر.")
               return
           
           response = await self.highrise.get_room_users()
           users = [content[0] for content in response.content]
           usernames = [user.username.lower() for user in users]
           parts = message.split()
           args = parts[1:]
   
           if len(args) >= 1 and args[0][0] == "@" and args[0][1:].lower() in usernames:
               target_username = args[0][1:].lower()
               if target_username == "90HB":
                   await self.highrise.chat("لا يمكنك رقص صاحب البوت ياحب ")
                   return
   
               user_id = next((u.id for u in users if u.username.lower() == target_username), None)
               
               if user_id:
                   await self.highrise.send_emote("emote-snake", user_id)
               else:
                   print("User not found")
   
    except Exception as e:
          print(f"An error occurred: {e}")
   
    

     
    user_privileges = await self.highrise.get_room_privilege(user.id)
    if message.startswith("حرر @"):
        
        if (not user_privileges.moderator) and (user.username != "90HB"):
          await self.highrise.chat("انت لست مشرفا لا يمكنك استخدام الامر.")
          return
        
     

        try:
             await self.unlock_user(message)
        except Exception as e:
             print(f"Error: {e}")
    user_privileges = await self.highrise.get_room_privilege(user.id)        
    if message.startswith("ثبت @"):
                  
            
        if (not user_privileges.moderator) and (user.username != "90HB"):
          await self.highrise.chat("انت لست مشرفا لا يمكنك استخدام الامر.")
          return
        
     

        try:
             await self.lock_user(message)
        except Exception as e:
             print(f"Error: {e}")
    user_privileges = await self.highrise.get_room_privilege(user.id)
    
    if message.startswith("متوسط"):
        
        
     

        try:
             await self.highrise.teleport(f"{user.id}", Position(15.9, 11.0, 3.8, facing='FrontRight'))
        except Exception as e:
             print(f"Error: {e}")
    

      

    if message.startswith("vps1050"):
        
        
     

        try:
             await self.highrise.teleport(f"{user.id}", Position(1.9, 1.0, 3, facing='FrontRight'))
        except Exception as e:
             print(f"Error: {e}")          
              

      
    if message.lower().lstrip().startswith(("-عصير جوفه", "عصير منجا" ,"عصير خوخ"  ,"عصير كوكتيل" ,"عصير تفاح" ,"عصير قصب" ,"ملوخيه" ,"ارز" ,"لحمه" ,"مياه" ,"خمرة" ,"شربات" ,"ارز" ,"خمره" ,"ملوخية")):
                await self.highrise.chat(f"الأوامر المطلوبه سيتم تنفيذها بعد خمس دقايق شكرا لك اذا تاخر الطلب قول طلبي او الطلب او اريد الطلب")

    if message.lower().lstrip().startswith(("-عصير جوفه", "اعطيني عصير منجا" ,"اعطيني عصير خوخ"  ,"اعطيني عصير كوكتيل" ,"اعطيني عصير تفاح" ,"اعطيني عصير قصب" ,"اعطيني ملوخيه" ,"اعطيني ارز" ,"لحمه" ,"اعطيني مياه" ,"اعطيني خمرة" ,"اعطيني شربات" ,"اعطيني ارز" ,"اعطيني خمره" ,"اعطيني ملوخية")):
                await self.highrise.chat(f"الأوامر المطلوبه سيتم تنفيذها بعد خمس دقايق شكرا لك اذا تاخر الطلب قول طلبي او الطلب او اريد الطلب")
    if message.lstrip().startswith(("طلhب", "اريدb الطلب", "طgلبي" ,"اعطيني منgيو")):
                await self.highrise.chat(f" لقد استلمت  طلبك  يافندم ")                
            
    if message.lower().lstrip().startswith(("المنيو", "مhنbيو" ,"اعطيني المنbيو")):
                await self.highrise.chat(f"عصير تفاح-عصير كوكتيل-عصير منجا-عصير جوفه-عصير خوخ-عصير قصب-عصير عنب-خمره-لحمه-ملوخيه-مياه-شربات-ارز")

    if message.lower().lstrip().startswith(("الاذكار")):
                await self.highrise.chat(f"اللهم اكفنى بحلالك عن حرامك وأغننى بفضلك عمن سواك")






    
              



      
      
    if "صعدني" in message or "فوق" in message:
        
        try:
            await self.highrise.teleport(f"{user.id}", Position(15.0, 11.0, 27.5, facing='FrontRight'))
        except:
           print("error 3")


      


    if message.startswith("تو"):
                        await self.highrise.send_emote("emote-bow", user.id) 

    if message.startswith("ولكم"):
                        await self.highrise.send_emote("emote-bow", user.id)      
        
    if message.startswith("😭"):
                        await self.highrise.send_emote("emoji-crying", user.id) 
        
    if message.startswith("🙄"):
                        await self.highrise.send_emote("emoji-eyeroll", user.id)
        
    if message.startswith("اعطيني قلب"):
            await self.highrise.react("heart", user.id)
            await self.highrise.chat(f"احلى قلب❤️@{user.username}")
      
    if "احبك" in message:  
            response = random.choice(["واني اموت عليج ♥" , "واني اعشقك "])
            await self.highrise.chat(response)
      
    if message.startswith("😂"):
                        await self.highrise.send_emote("emote-laughing", user.id)      

    if message.startswith("هه"):
                        await self.highrise.send_emote("emote-laughing", user.id) 

    if message.startswith("🤣"):
                        await self.highrise.send_emote("emote-laughing", user.id)           

    if "مح" in message:
      try:
        emote_id = "emote-kiss"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")    
    if "هلا" in message:
      try:
        emote_id = "emote-hello"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "اهلا" in message:
      try:
        emote_id = "emote-hello"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")      

    if "شكرا" in message:
      try:
        emote_id = "emote-kiss"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "لا" in message:
      try:
        emote_id = "emote-no"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print("error 3")

    if "غني" in message:
      try:
        emote_id = "idle_singing"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if "يس" in message:
      try:
        emote_id = "emote-yes"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")
    if "اوف" in message:
      try:
        emote_id = "emote-sad"
        await self.highrise.send_emote(emote_id, user.id)
      except:
        print(f"{emote_id}")

    if message.startswith("سيو"):
                        await self.highrise.send_emote("emote-hello", user.id)

    if message.startswith("سلام"):
                        await self.highrise.send_emote("emote-hello", user.id)

    if message.startswith("باي"):
                        await self.highrise.send_emote("emote-hello", user.id)      
      
    if message.startswith("vip")and user.username in name_boss: 
       await self.highrise.teleport(user.id, Position(14, 18, 4))
     
    
    if "نزلني" in message or"تحت" in message:
        
        try:
            await self.highrise.teleport(f"{user.id}", Position(13.0, 0.0, 10.0, facing='FrontRight'))
        except:
           print("error 3")

      
    if message.startswith("؟"):
                        await self.highrise.send_emote("emote-think", user.id)

    if message.startswith("?"):
                        await self.highrise.send_emote("emote-think", user.id)      
    

      
    if message.startswith("الاواgمر"):
      await self.highrise.chat(f"اعطيني المنيو-صعدني-نزلني-رقصني{user.username}")
    
    if message.startswith("كتم"):
        if user.username == "Q._M3":
          pass
        else:
          await self.highrise.chat(
              "ليس لديك الاذن لتفعيل هذي الميزه.")
          return
        #separete message into parts
        parts = message.split()
        #check if message is valid "kick @username"
        if len(parts) != 2:
          await self.highrise.chat("Invalid kick command format.")
          return
        #checks if there's a @ in the message
        username = parts[1] if "@" not in parts[1] else parts[1][1:]
        #check if user is in room
        room_users = (await self.highrise.get_room_users()).content
        for room_user, _pos in room_users:
          if room_user.username.lower() == username.lower():
            user_id = room_user.id
            break
        if "user_id" not in locals():
          await self.highrise.chat(
              "User not found, please specify a valid user and coordinate")
          return
        #kick user
        try:
          await self.highrise.moderate_room(user_id, "mute",600)
        except Exception as e:
          await self.highrise.chat(f"{e}")
          return
        #send message to chat
        await self.highrise.chat(f"{username} تم كتم المستخدم ")
      

    if message.lstrip().startswith(("حر" ,"مر")):
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]
                usernames = [user.username.lower() for user in users]
                parts = message[1:].split()
                args = parts[1:]
        
                if len(args) < 1:
                    await self.highrise.send_whisper(user.id, f"Usage: !{parts[0]} <@username>")
                    return
                elif args[0][0] != "@":
                    await self.highrise.send_whisper(user.id, f"Invalid user format. Please use '@username'.")
                    return
                elif args[0][1:].lower() not in usernames:
                    await self.highrise.send_whisper(user.id, f"{args[0][1:]} is not in the room.")
                    return
        
                user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
                if not user_id:
                    await self.highrise.send_whisper(user.id, f"User {args[0][1:]} not found")
                    return
        
                try:
                    if message.startswith("حر"):
                        
                        await self.highrise.send_emote("emote-swordfight", user.id)
                        await self.highrise.send_emote("emote-swordfight", user_id)
                    elif message.startswith("مر"):
                        
                        await self.highrise.send_emote("emote-hug", user.id)
                        await self.highrise.send_emote("emote-hug", user_id)
                    elif message.startswith("قاتلني"):
                        
                        await self.highrise.send_emote("emote-lust", user.id)
                        await self.highrise.send_emote("emote-lust", user_id)
                except Exception as e:
                    print(f"An exception occurred[Due To {parts[0][1:]}]: {e}")
    
   

    
    elif "طوvلي" in message:
        try:
            height_cm = random.randint(110, 199)
            await self.highrise.chat(f"{user.username} طولك {height_cm} سنتيمتر!")
        except Exception as e:
            print(f"Error: {e}")
    elif "وزhني" in message:
        try:
            weight_kg = random.randint(35, 150)
            await self.highrise.chat(f"{user.username} وزنك {weight_kg} كيلوجرام!")
        except Exception as e:
            print(f"Error: {e}") 

    if "نسبه bحبي" in message:
        random_years = random.randint(0, 100)
        response = f"نسبة حبك : {random_years} "
        await self.highrise.chat(response)

    if "نسبةh حبي" in message:
        random_years = random.randint(1, 100)
        response = f"نسبة حبك: {random_years} "
        await self.highrise.chat(response)
        if message.startswith("ح"):
                        
                        await self.highrise.send_emote("emote-swordfight", user.id)


      
      
    if "نسبbة زواجي" in message:
        random_years = random.randint(0,100)
        response = f"نسبه زواجك: {random_years} "
        await self.highrise.chat(response)
    if "رقصني" in message:
      try:
        emote_id = random.choice(self.dancs)
        await self.highrise.send_emote(emote_id, user.id)
      except Exception as e:
        print(f"Error: {e}")
          
             
  async def run(self):
        while True:  # Continuous loop for auto-reconnection
            try:
                print("Starting bot...")
                definitions = [BotDefinition(self, self.room_id, self.api_token)]
                await __main__.main(definitions)
            except Exception as e:
                # Log the exception details
                print(f"An exception occurred: {e}")
                traceback.print_exc()

                # Optional: Add a short delay before reconnecting
                print("Reconnecting in 5 seconds...")
                await asyncio.sleep(1)
                continue  # Retry the connection
keep_alive()
if __name__ == "__main__":
    room_id = "68bb81b6b3ad4d2c8d06e70d"
    token = "128f3aa49fbe846bfc9648b79b44a08ab97d637b7a84f3c25072c7687308ebd5"
    bot = Highrise() 
    bot_instance = MyBot(bot, room_id, token)
    asyncio.run(bot_instance.run())




    
