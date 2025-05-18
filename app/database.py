import motor.motor_asyncio
import os

MONGO_DETAILS = os.getenv("MONGO_URL", "mongodb://mongo:27017")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.library
book_collection = database.get_collection("books")
