def create_item(item_type, name, description, location, reporter):
    return {
        "type": item_type,
        "name": name,
        "description": description,
        "location": location,
        "reporter": reporter,
        "resolved": False,
         }


def display_item(item):
    if item["resolved"]:
        status = "Claimed" or"Resolved"
    else:
        status = "Open"
    print( item["type"].upper() + " ITEM")
    print("Item:", item["name"])
    print("Description:", item["description"])
    print("Location:", item["location"])
    print("Reported by:", item["reporter"])
    print("Status:", status)
