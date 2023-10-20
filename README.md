# Nier:Automata - Chip Fusion Script
Simple python script that will help plan a chip fusion path with the chips in your inventory.

## Prerequisites
Have the following installed:
- Python 3

## Usage
Clone the repo or download the three .py files.
Create or modify the chips.json matching the example format, keeping all files in the same folder.

Run in terminal or command prompt:
```bash
python3 fuse.py
```

## Limitations
- Chip names have to match a specific format so see [chipNames](chipNames.md) to make sure you use the correct name in the json file.
- This script looks for exact matches of chips and doesn't use the formula to calculate all potential matches

## Future Improvements
- Add formula to calculate the resulting cost after fusion
- Add functionality to target specific levels and costs
- Add functionality to try to fuse several of the same level + cost


## References
- [maki's guide on steam](https://steamcommunity.com/sharedfiles/filedetails/?id=2486382617)
- [strawbry_jam's guide on steam](https://steamcommunity.com/sharedfiles/filedetails/?id=2918340521)
