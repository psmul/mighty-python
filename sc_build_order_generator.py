import random
import time
import os

terran_pool = ['hellion', 'scv', 'factory', 'supply depot', 'command center', 'reaper', 'stargate', 'ghost', 'battlecruiser', 'techlab']
zerg_pool = ['hatchery', 'zergling', 'baneling', 'drone', 'evolution chamber', 'hive', 'lurkers den', 'hydralisk', 'mutalisk', 'roach warren']
protoss_pool = ['pylon', 'nexus', 'zealot', 'stalker', 'probe', 'gateway', 'forge', 'stargate', 'archon', 'tempest']
races_pool = ['terran', 'zerg', 'protoss']
max_game_time = 5;
max_game_time_str = str(max_game_time)

selected_race = input("Please select one of three races: terran, zerg, protoss.\n").lower()
is_race_ok = selected_race in races_pool

while not is_race_ok:
    selected_race = input("Please provide proper race: terran, zerg, protoss.\n")
    is_race_ok = selected_race in races_pool

print("You have selected " + selected_race + ".\n")

timespan = input("Now please provide time (in minutes) for how long game build order should be prepared. Maximum value is " + max_game_time_str + " minutes.\n")
is_timespan_ok = timespan.isdigit() and int(timespan) <= max_game_time

while not is_timespan_ok:
    timespan = input("Invalid time value, please provide valid time value. Maximum value is " + max_game_time_str + " minutes.\n")
    is_timespan_ok = timespan.isdigit() and int(timespan) <= max_game_time

print("All set!\n")
print("Selected race: " + selected_race + ".\nSelected time: " + timespan + ".\n")

print("Please wait a moment as our OMEGALUL advanced AI is preparing build order for you...")
time.sleep(3)
print("Ready.")

