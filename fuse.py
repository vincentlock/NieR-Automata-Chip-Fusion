from collections import defaultdict, Counter
import json
from helper import ExtractChipInfo, VALID_CHIP_NAMES, CHIP_COST_MINIMUMS, MIN_LEVEL, MAX_LEVEL

filename = "chips.json"

data = ExtractChipInfo(filename)["chips"]

# parse data into some data structure (defaultdict?)
chips = defaultdict(lambda: defaultdict(Counter))
for item in data:
    if item["name"] not in VALID_CHIP_NAMES:
        raise Exception("Invalid chip name")
    if item["count"] > 99:
        raise Exception("Chip count is too high")
    if not MIN_LEVEL <= item["level"] <= MAX_LEVEL:
        raise Exception("Chip level isn't valid")
    if CHIP_COST_MINIMUMS[item["level"]] > item["cost"]:
        raise Exception("Chip cost isn't valid")

    chips[item["name"]][item["level"]][item["cost"]] += item["count"]


# iterate over each chip name
    # brute force/greedily iterate over every level from top to botton to try to find pairings
