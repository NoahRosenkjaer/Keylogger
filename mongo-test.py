from datetime import datetime
import pymongo

def connect():
    name = "keylogger-test"
    client = pymongo.MongoClient("localhost", 27017)

    db = client["Test-db"]
    collection = db["Test-collection"]
    return db, collection

dataB = connect()
sensor_data = {
    "temperature": 100,
    "humidity": 100,
    "pressure": 1011.4,
    "timestamp": datetime.now().isoformat() # ISO date
}
result = dataB[1].insert_one(sensor_data)
