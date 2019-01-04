import random
import time
import math
import sys

races = {
    "terran":   ["hellion", "scv", "factory", "supply depot", "command center", "reaper", "stargate", "ghost", "battlecruiser", "techlab"],
    "zerg":     ["hatchery", "zergling", "baneling", "drone", "evolution chamber", "hive", "lurkers den", "hydralisk", "mutalisk", "roach warren"],
    "protoss":  ["pylon", "nexus", "zealot", "stalker", "probe", "gateway", "forge", "stargate", "archon", "tempest"]
}

def getRandomPositionFromRaceArray(race):
    rand = random.randint(0,len(race)-1)
    return race[rand]

races_pool = ["terran", "zerg", "protoss"]
selected_race = []
max_game_time = 5;
max_game_time_str = str(max_game_time)
curr_game_time = 0;
selected_race_input = input("Please select one of three races: terran, zerg, protoss.\n").lower()
is_race_ok = selected_race_input.lower() in races_pool


while not is_race_ok:
    selected_race_input = input("Please provide proper race: terran, zerg, protoss.\n")
    is_race_ok = selected_race_input in races_pool

print("You have selected " + selected_race_input + ".\n")

timespan = input("Now please provide time (in minutes) for how long game build order should be prepared. Maximum value is " + max_game_time_str + " minutes.\n")
is_timespan_ok = timespan.isdigit() and int(timespan) <= max_game_time

while not is_timespan_ok:
    timespan = input("Invalid time value, please provide valid time value. Maximum value is " + max_game_time_str + " minutes.\n")
    is_timespan_ok = timespan.isdigit() and int(timespan) <= max_game_time

print("All set!\n")
print("Selected race: " + selected_race_input + ".\nSelected time: " + timespan + ".\n")

timespan = int(timespan) * 60
selected_race = races.get(selected_race_input)

print("Please wait a moment as our OMEGALUL advanced AI is preparing build order for you...")
time.sleep(3)
print("Ready. Here is your build:\n\n")

while(curr_game_time <= timespan):
    outcome_str = ""
    minute = math.floor(curr_game_time / 60)
    seconds = curr_game_time % 60
    
    if seconds < 10:
        seconds = "0" + str(seconds)
        
    outcome_str = "[0" + str(minute) + ":" + str(seconds) + "] - "
    unit = getRandomPositionFromRaceArray(selected_race)
    outcome_str += unit
    print(outcome_str)
    curr_game_time += 5

print("Done. Good luck and have fun!")

sys.exit(0)

