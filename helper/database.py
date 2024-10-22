# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
# Special Thanks To (https://github.com/JayMahakal98)
# Update Channel @Digital_Botz & @DigitalBotz_Support

import motor.motor_asyncio, datetime, pytz
from config import Config
from helper.utils import send_log

class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.user
        self.premium = self.db.premium

    def new_user(self, id):
        return dict(
            _id=int(id),
            join_date=datetime.date.today().isoformat(),
            file_id=None,
            caption=None,
            prefix=None,
            suffix=None,
            used_limit=0,
            usertype="Free",
            uploadlimit=0,
            daily=0,
            metadata_mode=False,
            metadata_code=""" -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @Rkn_Bots" -metadata author="@RknDeveloper" -metadata:s:s title="Subtitled By :- @Rkn_Bots" -metadata:s:a title="By :- @RknDeveloper" -metadata:s:v title="By:- @Rkn_Bots" """,
            expiry_time=None,
            has_free_trial=False,
            ban_status=dict(
                is_banned=False,
                ban_duration=0,
                banned_on=datetime.date.max.isoformat(),
                ban_reason=''
            )
        )

    async def add_user(self, b, m):
        u = m.from_user
        if not await self.is_user_exist(u.id):
            user = self.new_user(u.id)
            await self.col.insert_one(user)            
            await send_log(b, u)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return bool(user)

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    async def delete_user(self, user_id):
        await self.col.delete_many({'_id': int(user_id)})
    
    async def set_thumbnail(self, id, file_id):
        await self.col.update_one({'_id': int(id)}, {'$set': {'file_id': file_id}})

    async def get_thumbnail(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('file_id', None)

    async def set_caption(self, id, caption):
        await self.col.update_one({'_id': int(id)}, {'$set': {'caption': caption}})

    async def get_caption(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('caption', None)

    async def set_prefix(self, id, prefix):
        await self.col.update_one({'_id': int(id)}, {'$set': {'prefix': prefix}})

    async def get_prefix(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('prefix', None)

    async def set_suffix(self, id, suffix):
        await self.col.update_one({'_id': int(id)}, {'$set': {'suffix': suffix}})

    async def get_suffix(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('suffix', None)

    async def set_metadata_mode(self, id, bool_meta):
        await self.col.update_one({'_id': int(id)}, {'$set': {'metadata_mode': bool_meta}})

    async def get_metadata_mode(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('metadata_mode', None)

    async def set_metadata_code(self, id, metadata_code):
        await self.col.update_one({'_id': int(id)}, {'$set': {'metadata_code': metadata_code}})

    async def get_metadata_code(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('metadata_code', None)

    async def set_used_limit(self, id, used):
        await self.col.update_one({'_id': int(id)}, {'$set': {'used_limit': used}})
      
    async def set_usertype(self, id, type):
        await self.col.update_one({'_id': int(id)}, {'$set': {'usertype': type}})

    async def set_uploadlimit(self, id, limit):
        await self.col.update_one({'_id': int(id)}, {'$set': {'uploadlimit': limit}})
  
    async def set_reset_dailylimit(self, id, date):
        await self.col.update_one({'_id': int(id)}, {'$set': {'daily': date}})
    
    async def get_user(self, user_id):
        user_data = await self.premium.find_one({"id": user_id})
        return user_data
        
    async def addpremium(self, user_id, user_data):    
        await self.premium.update_one({"id": user_id}, {"$set": user_data}, upsert=True)

    async def remove_premium(self, user_id):
        await self.premium.update_one({"id": user_id}, {"$set": {"expiry_time": None}})

    async def checking_remaining_time(self, user_id):
        user_data = await self.get_user(user_id)
        expiry_time = user_data.get("expiry_time")
        time_left_str = expiry_time - datetime.datetime.now()
        return time_left_str

    async def has_premium_access(self, user_id):
        user_data = await self.get_user(user_id)
        if user_data:
            expiry_time = user_data.get("expiry_time")
            if expiry_time is None:
                # User previously used the free trial, but it has ended.
                return False
            elif isinstance(expiry_time, datetime.datetime) and datetime.datetime.now() <= expiry_time:
                return True
            else:
                await self.premium.update_one({"id": user_id}, {"$set": {"expiry_time": None}})
        return False

    async def total_premium_users_count(self):
        count = await self.premium.count_documents({"expiry_time": {"$gt": datetime.datetime.now()}})
        return count

    async def get_all_premium_users(self):
        all_premium_users = self.premium.find({"expiry_time": {"$gt": datetime.datetime.now()}})
        return all_premium_users

    async def get_free_trial_status(self, user_id):
        user_data = await self.get_user(user_id)
        if user_data:
            return user_data.get("has_free_trial", False)
        return False

    async def give_free_trail(self, user_id):
        seconds = 720*60         
        expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
        user_data = {"id": user_id, "expiry_time": expiry_time, "has_free_trial": True}
        await self.premium.update_one({"id": user_id}, {"$set": user_data}, upsert=True)

    async def remove_ban(self, id):
        ban_status = dict(
            is_banned=False,
            ban_duration=0,
            banned_on=datetime.date.max.isoformat(),
            ban_reason=''
        )
        await self.col.update_one({'_id': int(id)}, {'$set': {'ban_status': ban_status}})

    async def ban_user(self, user_id, ban_duration, ban_reason):
        ban_status = dict(
            is_banned=True,
            ban_duration=ban_duration,
            banned_on=datetime.date.today().isoformat(),
            ban_reason=ban_reason
        )
        await self.col.update_one({'_id': int(user_id)}, {'$set': {'ban_status': ban_status}})

    async def get_ban_status(self, id):
        default = dict(
            is_banned=False,
            ban_duration=0,
            banned_on=datetime.date.max.isoformat(),
            ban_reason=''
        )
        user = await self.col.find_one({'_id': int(id)})
        return user.get('ban_status', default)

    async def get_all_banned_users(self):
        banned_users = self.col.find({'ban_status.is_banned': True})
        return banned_users
        
digital_botz = Database(Config.DB_URL, Config.DB_NAME)

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
