class User:

    collection = None

    def __init__(self):
        pass

    @staticmethod
    async def get_user(db, uid):
        return await db.users.find_one(uid)
