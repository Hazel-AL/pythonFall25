import faker
import json
import random
from datetime import date
from datetime import timedelta

fake = faker.Faker()

print(fake.email())
print(fake.address())
print(fake.company())

users = []
for i in range(10):
    user = {
        "username": fake.unique.user_name(),
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "age": fake.random_int(min=18, max=90)
    }
    users.append(user)

with open ("users.json", "w") as file:
    json.dump(users, file, indent=4)

# create an ad campaign
# start and end dates
# target user age

def getDates():
    duration = random.randint(1, 2 * 360)
    offset = random.randint(-365, 365)
    start = date.today() - timedelta(days=offset)
    end = start + timedelta(days=duration)

    return start.strftime("%Y%m%d"), end.strftime("%Y%m%d")
print(getDates())

def getAgeRange():
    age = random.randrange(20, 46, 5)
    diff = random.randrange(5, 21, 5)
    return f"{age}-{age+diff}"
print(getAgeRange())

def getCurrency():
    return random.choice(("GBP", "USD", "JPY", "EUR"))

def getName():
    i, j = getDates()
    return f"<{i}>_<{j}>_<{getAgeRange()}>_<{getCurrency()}>"
print(getName())

def getCampaignData():
    name = getName()
    budget = random.randint(10**3, 10**12)
    spent = random.randint(10**2, budget)

    return {
        "cmp_name": name,
        "cmp_budget": budget,
        "cmp_spent": spent
    }
print(getCampaignData())

def getRawData(users):
    raw = []
    for user in users:
        campaigns = [getCampaignData() for _ in range(random.randint(2, 8))]
        raw.append({"user": user, "campaigns": campaigns})
    return raw

with open("rawData.json", "w") as file:
    json.dump(getRawData(users,file, indent=4))