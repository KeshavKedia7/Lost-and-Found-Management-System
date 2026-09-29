import lost_found_manager
import check

items = []
i=1

def report_item():
    print("\n--- Report an Item ---")
    item_type = input("Is the item Lost or Found? ")

    if check.valid_item_type(item_type) == False:
        print("Please enter Lost or Found.")
        return

    name = input("Enter item name: ")
    description = input("Enter description: ")
    location = input("Enter location: ")
    reporter = input("Enter your name: ")

    if check.valid_item_type(item_type) == False:
        print("Please enter Lost or Found.")
        return
    if check.valid_text(name) == False:
        print("Item name cannot be empty.")
        return
    if check.valid_text(description) == False:
        print("Description cannot be empty.")
        return
    if check.valid_text(location) == False:
        print("Location cannot be empty.")
        return
    if check.valid_text(reporter) == False:
        print("Name cannot be empty.")
        return

    lost_found_manager.add_item(items, item_type, name, description, location, reporter)
    print("Item reported successfully.")

def view_items():
    print("\n--- All Reports ---")
    if lost_found_manager.number_of_items(items) == 0:
        print("No reports available.")
        return
    lost_found_manager.display_items(items)

def search_items():
    print("\n--- Search ---")
    if lost_found_manager.number_of_items(items) == 0:
        print("No reports available.")
        return
    keyword = input("Enter item name, description or location: ")
    results = lost_found_manager.search_items(items, keyword)
    if len(results) == 0:
        print("No matching reports found.")
    else:
        lost_found_manager.display_items(results)

def resolve_item():
    print("\n--- Claim / Resolve Item ---")
    if lost_found_manager.number_of_items(items) == 0:
        print("No reports available.")
        return
    lost_found_manager.display_items(items)
    number = input("Enter report number: ")
    if check.valid_number(number):
        if lost_found_manager.resolve_item(items, int(number)):
            print("Item marked as claimed/resolved.")
        else:
            print("Invalid report number.")
    else:
        print("Please enter a valid number.")

def remove_item():
    print("\n--- Remove Report ---")
    if lost_found_manager.number_of_items(items) == 0:
        print("No reports available.")
        return
    lost_found_manager.display_items(items)
    number = input("Enter report number: ")
    if check.valid_number(number):
        if lost_found_manager.remove_item(items, int(number)):
            print("Report removed successfully.")
        else:
            print("Invalid report number.")
    else:
        print("Please enter a valid number.")
        


while i>=1:
    print("--------------------------------------")
    print("\n>>> SMART CAMPUS LOST-AND-FOUND SYSTEM <<<")
    print("--------------------------------------")
    print("Open reports:", lost_found_manager.open_count(items))
    print("Resolved reports:", lost_found_manager.resolved_count(items))
    print("")
    print("1. Report lost/found item")
    print("2. View all reports")
    print("3. Search for an item")
    print("4. Claim / resolve item")
    print("5. Remove a report")
    print("6. View report counts")
    print("7. Exit")

    choice = input("Enter your choice: ")   

    if choice == "1":
        report_item()
    elif choice == "2":
        view_items()
    elif choice == "3":
        search_items()
    elif choice == "4":
        resolve_item()
    elif choice == "5":
        remove_item()
    elif choice == "6":
        print("Total reports:", lost_found_manager.number_of_items(items))
        print("Lost items:", lost_found_manager.lost_count(items))
        print("Found items:", lost_found_manager.found_count(items))
    elif choice == "7":
        print("Thank you for using the Smart Campus Lost-and-Found System.")
        break
    else:
        print("Invalid choice.")