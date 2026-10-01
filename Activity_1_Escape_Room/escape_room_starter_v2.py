# Escape Room Starter Code Version 2

from random import choice


def room_one(inventory):
    """Room 1: the player arrives here first."""

    
    # TODO 1: 
    print("You wake up in an room in an abandoned building. There is a door to the LEFT and a bag in front of you.")

    while True:
        choice = input("What do you do? ").lower()

        # TODO 3: Write if/elif/else branches for this room's choices.
        if choice == "go left":
            print("You step through the door into the main hallway.")
            return "room_two"
        elif choice == "search bag":
            if has_item(inventory, "key badge"):
                print("You already have the key badge.")
            else:
                print("You find a key badge!")
                inventory.append("key badge")
        else:
            print("Hmm, try 'go left' or 'search bag'.")
    

    # TODO 4: replace this placeholder return once your branches are written
    return "room_one"
    
def room_two(inventory):
    """Room 2: reached after leaving room one."""

    # TODO 5: Copy the room_one pattern here. Give this room its own
    # description and its own choices. One choice should require an item
    # from `inventory` (use a for loop, see TODO 6) to "escape".

    print("You are in room two. (You see two doors, one to the left that requires a key badge and one to the right that is sealed shut.)")
    while True:
        choice = input("What do you do? ").lower()
        if choice == "go left":
            if has_item(inventory, "key badge"):
                print("You scan the key badge and the door unlocks. Congratulations, you escape!")
                return "escaped"
            else:
                print("The scanner flashes red. It looks like you need some kind of key badge.")
                return "room_one"
        elif choice == "go right":
            print("The door is sealed shut. Try 'go left' to try the exit.")
        else:
            print("That isn't an option. Try 'go left' or 'go right'.")


def has_item(inventory, item_name):
    """Return True if item_name is in the player's inventory."""

    # TODO 6: Use a for loop to check each item in `inventory`.
    # If it matches item_name, return True. If the loop finishes without
    # finding it, return False.
    for item in inventory:
        if item == item_name:
            return True

    return False

def main():
    print("=== Escape Room ===")
    print("Type 'quit' at any time to give up.\n")

    inventory = []
    current_room = "room_one"
    # TODO 2: Set the loop condition so the game keeps running until the
    # player escapes or quits. Hint: use a `playing` boolean flag.
    playing = True
    while playing:
        if current_room == "room_one":
            current_room = room_one(inventory)
        elif current_room == "room_two":
            current_room = room_two(inventory)
        elif current_room == "escaped":
            print("\nYou escaped! Congratulations!")
            playing = False
        elif current_room == "quit":
            print("\nMaybe next time!")
            playing = False

if __name__ == "__main__":
    main()