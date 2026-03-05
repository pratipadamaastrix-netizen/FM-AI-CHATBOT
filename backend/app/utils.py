import datetime
import random

def generate_ticket_ref():
    year = datetime.datetime.now().year
    random_number = random.randint(1000, 9999)
    return f"FM-{year}-{random_number}"

def map_priority(description):
    high_keywords = ["lift", "flood", "gas leak", "fire"]
    for word in high_keywords:
        if word.lower() in description.lower():
            return "HIGH"
    return "NORMAL"