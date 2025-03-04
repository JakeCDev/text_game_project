#======================================================================
#Entryway Room: 4 - (First Room Inside the House)
#room_4_entryway.py
#======================================================================

#Internal imports
import game_states
from game_mechanics import visit_room, check_front_door, check_entryway_for_door, check_inventory, check_fuse_box, universal_wait
from text_effects import type_text
from ascii_art import ascii_art
from debug_mode import debug_menu

#======================================================================

#External imports
import random

#======================================================================
#Entryway function room: 4

def room_4_entryway():
    #Room tracker
    room_name = "room_4_entryway"
    visit_count = game_states.room_visits.get(room_name, 0)

    #Check if the front door has disappeared
    check_entryway_for_door()

    #Room state changes
    if visit_count == 0:  #Present
        type_text("\nYou step into the room. The house creaks all around you.")
        type_text("The entryway is dimly lit. Dust flows through the air.")

    elif visit_count == 1:  #Past
        type_text("\nThe wallpaper is clean, the air carries the faint scent of coffee.")
        type_text("Shoes are neatly placed by the door, as if someone was just here...")

    elif visit_count == 2:  #Future
        type_text("\nThe walls have been repainted... A new table and coat rack stands where the old one was...")
        type_text("It feels like someone else lives here now...")

    elif visit_count == 3:  #Eerie
        type_text("\nYour footsteps echo strangely, as if someone else is walking right behind you...")
        type_text("The temperature drops almost instantly...")

    else:  #Altered Reality
        type_text("\nYou are inside. But the house is... wrong...")
        type_text("The room is filled with stairs and doors leading nowhere...")

#======================================================================

    #Entryway art
    print(ascii_art["entryway"])

#======================================================================
#Entryway choices
    while True:
        print("\nWhat do you want to do?")
        print("1. Look around")
        print("2. Wait in the entryway")
        print("3. Check the front door")
        print("4. Go west to the Office")
        print("5. Go east to the Living Room")
        print("6. Check Inventory")
        if not game_states.power_restored:  #If fuse puzzle not done
            print("7. Check the fuse box")

        choice = input("> ").strip()

        if choice == "1":
            look_around_entryway()

        elif choice == "2":
            universal_wait()
            input("\nPress Enter to continue.")

        elif choice == "3":
            check_front_door()

        elif choice == "4":
            game_states.room_visits[room_name] += 1
            visit_room("room_5_office")  #Move west
            break

        elif choice == "5":
            game_states.room_visits[room_name] += 1
            visit_room("room_8_living_room")  #Move east
            break

        elif choice == "6":
            check_inventory(room_4_entryway)

        elif choice == "7" and not game_states.power_restored:
            check_fuse_box()

        elif choice == "debug":
            debug_menu()  #Calls the debug menu

        else:
            print("\nInvalid choice. Try again.")

#======================================================================
#Look around entryway

def look_around_entryway():
    while True:
        type_text("\nYou scan the dim entryway. What do you want to examine?")
        print("1. The mirror on the wall")
        print("2. The coat rack")
        print("3. The closet")
        print("4. Nevermind")

        choice = input("> ").strip()

        if choice == "1":
            type_text("\nYou step up to the mirror. The reflection is hard to make out.")
            print(ascii_art["mirror"])

        elif choice == "2":  #Red fuse
            if "red fuse" not in game_states.inventory and "red fuse" not in game_states.fuse_box:
                type_text("\nAn old coat rack stands by the door. A single coat hangs there.")
                type_text("Its pocket has a single Red Fuse.")
                print(ascii_art["red_fuse"])
                game_states.inventory.append("red fuse")
                type_text("This may be useful... you decide to take it for now.")
            else:
                type_text("The coat's pockets are empty now.")

        elif choice == "3":
            type_text("\nThe closet is bare.")
            type_text("For a moment, you think you hear something shuffling behind you...")
            print(ascii_art["door"])

        elif choice == "4":
            return  #Exit back to entryway menu

        else:
            print("\nInvalid choice. Try again.")
#======================================================================

