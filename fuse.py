import json
from helper import extractChipInfo

filename = "chips.json"

data = extractChipInfo(filename)

# parse data into some data structure (defaultdict?)
    # error check to make sure that the chip name is valid
    # make sure the count is valid (probably <= 99)
    # make sure that the minimum chip values is valid (max doesn't matter since the rec will be to sell anyway)


# iterate over each chip name
    # brute force/greedily iterate over every level from top to botton to try to find pairings
