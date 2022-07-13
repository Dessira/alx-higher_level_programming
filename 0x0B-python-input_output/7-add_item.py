#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    chicken = load_from_json_file("add_item.json")
except FileNotFoundError:
    chicken = []

for i in range(1, len(sys.argv)):
    chicken.append(sys.argv[i])
save_to_json_file(chicken, "add_item.json")
