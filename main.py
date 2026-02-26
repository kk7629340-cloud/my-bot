import asyncio
import random
from highrise import BaseBot, User, Position
from highrise.models import SessionMetadata
from highrise.__main__ import run

class MyBot(BaseBot):
    def __init__(self):
        super().__init__()
        # --- الإعدادات ---
        self.room_id = "68bb81b6b3ad4d2c8d06e70d"
        self.api_token = "a7bc6b92e7aab123e5a044d7ce4d252671ae12cf7554a58fe4c1012a882d8d4f"
        self.owner_name = "Karim__vims"
        
        # إحداثيات الباب (ثابتة 100%)
        self.door_pos = Position(x=0.5, y=0.0, z=0.5, facing='front')
        
        # إحداثيات الطوابق
        self.p1_pos = Position(x=15.0, y=5.0, z=15.0)  
        self.vip_pos = Position(x=20.0, y=10.0, z=20.0) 

        # --- قائمة الـ 200 رقصة ---
        self.dance_list = {
            1:"Hip Hop", 2:"Salsa", 3:"Moonwalk", 4:"Shuffle", 5:"Twerk",
            6:"Breakdance", 7:"TikTok Dance", 8:"Robot", 9:"Party Dance", 10:"Club Vibes",
            11:"Groove Step", 12:"Street Bounce", 13:"Funky Slide", 14:"Power Spin", 15:"Wave Flow",
            16:"Trap Move", 17:"Night Bounce", 18:"Fire Step", 19:"Cool Swing", 20:"Disco Fever",
            21:"Pop Lock", 22:"Body Roll", 23:"Side Shuffle", 24:"Jump Twist", 25:"Slide Left",
            26:"Slide Right", 27:"Flash Move", 28:"Energy Jump", 29:"Smooth Walk", 30:"Crazy Spin",
            31:"Sky Step", 32:"Shadow Move", 33:"Neon Dance", 34:"Fast Feet", 35:"Thunder Step",
            36:"Lightning Spin", 37:"Glow Shuffle", 38:"Party Rock", 39:"Bounce Flow", 40:"Star Move",
            41:"VIP Groove", 42:"Royal Step", 43:"Elite Spin", 44:"Diamond Dance", 45:"Golden Move",
            46:"Silver Shuffle", 47:"Luxury Walk", 48:"Crown Bounce", 49:"King Step", 50:"Queen Groove",
            51:"Fire Twist", 52:"Ice Slide", 53:"Lava Jump", 54:"Storm Spin", 55:"Ocean Wave",
            56:"Wind Move", 57:"Earth Step", 58:"Galaxy Flow", 59:"Cosmic Spin", 60:"Sunset Groove",
            61:"Sunrise Dance", 62:"Midnight Move", 63:"Dream Step", 64:"Savage Bounce", 65:"Flex Groove",
            66:"Hype Jump", 67:"Party King", 68:"Party Queen", 69:"Funk Wave", 70:"Street King",
            71:"Street Queen", 72:"Magic Spin", 73:"Boom Step", 74:"Energy Flow", 75:"Rhythm Bounce",
            76:"Fast Spin", 77:"Cool Jump", 78:"Vibe Move", 79:"Beat Step", 80:"Glow Move",
            81:"Power Groove", 82:"Mega Spin", 83:"Hyper Step", 84:"Turbo Bounce", 85:"Flash Groove",
            86:"Heat Move", 87:"Frost Step", 88:"Blaze Spin", 89:"Night Groove", 90:"City Bounce",
            91:"Urban Step", 92:"Club Spin", 93:"Trap Groove", 94:"Bass Move", 95:"DJ Bounce",
            96:"Party Flex", 97:"Smooth Bounce", 98:"Wave Jump", 99:"Quick Spin", 100:"Star Groove",
            101:"Royal Spin", 102:"Diamond Step", 103:"Gold Bounce", 104:"Silver Move", 105:"Neon Spin",
            106:"Shadow Step", 107:"Fire Groove", 108:"Ice Groove", 109:"Thunder Move", 110:"Storm Bounce",
            111:"Sky Groove", 112:"Dream Bounce", 113:"Savage Spin", 114:"Glow Step", 115:"Flash Bounce",
            116:"Turbo Spin", 117:"Mega Groove", 118:"Hyper Bounce", 119:"Cosmic Groove", 120:"Galaxy Step",
            121:"King Bounce", 122:"Queen Spin", 123:"Elite Groove", 124:"Crown Step", 125:"Luxury Spin",
            126:"Hype Groove", 127:"Boom Bounce", 128:"Energy Spin", 129:"Rhythm Step", 130:"Viral Dance",
            131:"Street Flex", 132:"Party Slide", 133:"Club Jump", 134:"Urban Groove", 135:"Trap Spin",
            136:"Beat Bounce", 137:"Night Spin", 138:"Flash Step", 139:"Power Bounce", 140:"Star Spin",
            141:"Heaven Move", 142:"Inferno Step", 143:"Crystal Spin", 144:"Phantom Groove", 145:"Ghost Walk",
            146:"Ninja Step", 147:"Samurai Spin", 148:"Pirate Dance", 149:"Zombie Move", 150:"Alien Groove",
            151:"Cyber Step", 152:"Future Spin", 153:"Retro Dance", 154:"Classic Groove", 155:"Modern Step",
            156:"Fusion Spin", 157:"Electric Move", 158:"Dynamic Groove", 159:"Epic Bounce", 160:"Legend Spin",
            161:"Mythic Step", 162:"Hero Groove", 163:"Villain Spin", 164:"Champion Move", 165:"Master Groove",
            166:"Pro Step", 167:"Rookie Dance", 168:"Boss Move", 169:"Ultimate Spin", 170:"Infinity Groove",
            171:"Shadow Bounce", 172:"Light Step", 173:"Dark Spin", 174:"Flame Groove", 175:"Aqua Move",
            176:"Terra Step", 177:"Volt Spin", 178:"Pulse Groove", 179:"Echo Dance", 180:"Nova Move",
            181:"Meteor Spin", 182:"Orbit Groove", 183:"Zen Step", 184:"Aura Spin", 185:"Spirit Dance",
            186:"Beast Move", 187:"Angel Groove", 188:"Demon Spin", 189:"Glitch Dance", 190:"Pixel Move",
            191:"Arcade Groove", 192:"Carnival Step", 193:"Festival Spin", 194:"Holiday Dance", 195:"Summer Groove",
            196:"Winter Step", 197:"Autumn Spin", 198:"Spring Dance", 199:"Final Groove", 200:"Ultimate Dance"
        }

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("البوت راهو عساس ثابت عند الباب!")
        # يروح للباب مرة وحدة برك ويحبس
        await self.highrise.walk_to(self.door_pos)
        asyncio.create_task(self.auto_dance_loop())

    async def on_user_join(self, user: User, position: Position) -> None:
        welcomes = ["مرحبا يا عسل", "مرحبا يا شيكور", "نورت الروم", "تواحشتك بزااف!"]
        await self.highrise.chat(f"{random.choice(welcomes)} {user.username}")
        # يشطحلو وهو في بلاصتو عند الباب
        random_dance = random.choice(list(self.dance_list.values()))
        await self.highrise.send_emote(random_dance)

    async def on_chat(self, user: User, message: str) -> None:
        msg = message.lower().strip()
        user_name = user.username.lower()
        owner_name = self.owner_name.lower()
        
        permissions = await self.highrise.get_room_privileges()
        is_mod = user.id in permissions.moderators or user_name == owner_name

        # --- أوامر المالك فقط ---
        if user_name == owner_name:
            if msg == "لبسة":
                outfit = await self.highrise.get_user_outfit(user.id)
                await self.highrise.set_outfit(outfit.outfit)

        # --- أوامر المشرفين (هات، اديني، VIP) ---
        if is_mod:
            if msg.startswith("هات @"):
                target = msg.split("@")[1].strip()
                room_users = (await self.highrise.get_room_users()).content
                target_id = next((u.id for u, p in room_users if u.username.lower() == target.lower()), None)
                if target_id:
                    # المشرف يجرجر الغاشي لعندو، البوت يبقى في بلاصتو عند الباب
                    u_pos = next(p for u, p in room_users if u.id == user.id)
                    await self.highrise.teleport(target_id, u_pos)
            
            elif msg.startswith("اديني @"):
                target = msg.split("@")[1].strip()
                room_users = (await self.highrise.get_room_users()).content
                target_pos = next((p for u, p in room_users if u.username.lower() == target.lower()), None)
                if target_pos:
                    # المشرف يروح لعند الشخص، البوت ما يتحركش
                    await self.highrise.teleport(user.id, target_pos)

            elif msg == "vip":
                await self.highrise.teleport(user.id, self.vip_pos)

        # --- أوامر الجميع ---
        if msg.isdigit():
            num = int(msg)
            if num == 0: await self.highrise.send_emote("idle-loop-sitfloor")
            elif num in self.dance_list: await self.highrise.send_emote(self.dance_list[num])

        if msg == "p1":
            await self.highrise.teleport(user.id, self.p1_pos)

    async def auto_dance_loop(self):
        while True:
            # يرقص وهو عند الباب كل 15 ثانية
            random_dance = random.choice(list(self.dance_list.values()))
            try:
                await self.highrise.send_emote(random_dance)
            except: pass
            await asyncio.sleep(15)

ROOM_ID = "68bb81b6b3ad4d2c8d06e70d" 
    TOKEN = "a7bc6b92e7aab123e5a044d7ce4d252671ae12cf7554a58fe4c1012a882d8d4f"

    
