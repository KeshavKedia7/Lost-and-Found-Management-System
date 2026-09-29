import item


def add_item(items, item_type, name, description, location, reporter):
    new_item = item.create_item(item_type, name, description, location, reporter)
    items.append(new_item)


def display_items(items):
    number = 1
    for report in items:
        print("\nReport no.:", number)
        item.display_item(report)
        number += 1


def search_items(items, keyword):
    results = []
    keyword = keyword.lower()
    for report in items:
        if keyword in report["name"].lower():
            results.append(report)
        elif keyword in report["description"].lower():
            results.append(report)
        elif keyword in report["location"].lower():
            results.append(report)
    return results


def resolve_item(items, number):
    if number < 1 or number > len(items):
        return False
    items[number - 1]["resolved"] = True
    return True


def remove_item(items, number):
    if number < 1 or number > len(items):
        return False
    items.pop(number - 1)
    return True


def number_of_items(items):
    return len(items)


def lost_count(items):
    count = 0
    for report in items:
        if report["type"] == "Lost":
            count += 1
    return count


def found_count(items):
    count = 0
    for report in items:
        if report["type"] == "Found":
            count += 1
    return count


def open_count(items):
    count = 0
    for report in items:
        if report["resolved"] == False:
            count += 1
    return count


def resolved_count(items):
    count = 0
    for report in items:
        if report["resolved"]:
            count += 1
    return count
