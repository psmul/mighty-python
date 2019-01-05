import random
import time
import math
import sys

races = {
    "terran":   ["hellion", "scv", "factory", "supply depot", "command center", "reaper", "stargate", "ghost", "battlecruiser", "techlab"],
    "zerg":     ["hatchery", "zergling", "baneling", "drone", "evolution chamber", "hive", "lurkers den", "hydralisk", "mutalisk", "roach warren"],
    "protoss":  ["pylon", "nexus", "zealot", "stalker", "probe", "gateway", "forge", "stargate", "archon", "tempest"]
}

races_pool = ["terran", "zerg", "protoss"]
selected_race = []
selected_race_input = ""
max_game_time = 5
curr_game_time = 0
is_race_ok = False
timespan = ""
is_timespan_ok = False

def get_random_position_from_race_dictionary(race):
    rand = random.randint(0,len(race)-1)
    return race[rand]

while not is_race_ok:
    selected_race_input = input("Please select one of three races: terran, zerg, protoss.\n").lower()
    is_race_ok = selected_race_input in races_pool

while not is_timespan_ok:
    timespan = input("Please provide time (in minutes) for how long game build order should be prepared. Maximum value is " + str(max_game_time) + " minutes.\n")
    is_timespan_ok = timespan.isdigit() and int(timespan) <= max_game_time

print("All set!\n")
print("Selected race: " + selected_race_input + ".\nSelected time: " + timespan + ".\n")
print("Please wait a moment as our OMEGALUL advanced AI is preparing build order for you...")
time.sleep(3)
print("Ready. Here is your build:\n\n")

timespan = int(timespan) * 60
selected_race = races.get(selected_race_input)

while(curr_game_time <= timespan):
    outcome_str = ""
    minute = math.floor(curr_game_time / 60)
    seconds = curr_game_time % 60
    
    if seconds < 10:
        seconds = "0" + str(seconds)
        
    outcome_str = "[0" + str(minute) + ":" + str(seconds) + "] - "
    unit = get_random_position_from_race_dictionary(selected_race)
    outcome_str += unit
    print(outcome_str)
    curr_game_time += 5

print("Done. Good luck and have fun!")

sys.exit(0)

