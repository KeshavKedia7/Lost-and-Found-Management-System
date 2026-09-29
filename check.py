def valid_text(value):
    return len(value) > 0

def valid_item_type(item_type):
    item_type = item_type.title()
    if item_type == "Lost":
        return True
    elif item_type == "Found":
        return True
    return False

def valid_number(value):
    return value.strip().isdigit()
