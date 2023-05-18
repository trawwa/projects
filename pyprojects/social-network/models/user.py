import hashlib
from motor.motor_asyncio import AsyncIOMotorDatabase


class User:

    def __init__(self):
        pass

    @classmethod
    async def get_user(cls, uid):
        pass

    @staticmethod
    async def create_new_user(db: AsyncIOMotorDatabase, data):
        email = data['email']
        user = await db.users.find_one({'email': email})
        if user:
            return dict(error='User with email {} is exist'.format(email))

        if data['first_name'] and data['last_name'] and data['password']:
            data = dict(data)
            data['password'] = hashlib.sha256(data['password'].encode(utf-8)).hexdigest()
            result = await db.users.insert_one(data)
            return result
        else:
            return dict(error='Missing user data parameters')
