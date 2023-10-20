import json

MIN_LEVEL, MAX_LEVEL = 0, 8

CHIP_COST_MINIMUMS = {
    0: 4,
    1: 5,
    2: 6,
    3: 7,
    4: 9,
    5: 11,
    6: 14,
    7: 17,
    8: 21
}

IDEAL_FUSION_COSTS = {
    8: {
        21: [17, 18]
    },
    7: {
        17: [14, 14],
        18: [15, 15]
    },
    6: {
        14: [11, 12],
        15: [12, 13]
    },
    5: {
        11: [9, 9],
        12: [10, 10],
        13: [11, 11]
    },
    4: {
        9: [7, 8],
        10: [8, 9],
        11: [9, 10]
    },
    3: {
        7: [6, 6],
        8: [7, 7],
        9: [8, 8],
        10: [9, 9]
    },
    2: {
        6: [5, 6],
        7: [6, 7],
        8: [7, 8],
        9: [8, 9]
    },
    1: {
        5: [4, 5],
        6: [5, 6],
        7: [6, 7],
        8: [7, 8],
        9: [8, 9]
    }
}

VALID_CHIP_NAMES = set([
    "Charge-Attack",
    "Counter",
    "Critical-Up",
    "Down-Attack-Up",
    "Last-Stand",
    "Ranged-Attack-Up",
    "Shockwave",
    "Weapon-Attack-Up",
    "Anti-Chain-Damage",
    "Auto-Heal",
    "Damage-Absorb",
    "Deadly-Heal",
    "Max-HP-Up",
    "Melee-Defense-Up",
    "Offensive-Heal",
    "Ranged-Defense",
    "Reset",
    "Resilience",
    "Auto-Use-Item",
    "Drop-Rate-Up",
    "EXP-Gain-Up",
    "Evade-Range-Up",
    "Fast-Cooldown",
    "Moving-Speed-Up",
    "Overclock",
    "Taunt-Up",
    "Vengeance",
    "Combust",
    "Heal-Drops-Up",
    "Hijack-Boost",
    "Stun"
])


def ExtractChipInfo(filename):
    try:
        with open(filename, 'r') as file:
            # content = file.read()
            # print(content)
            data = json.load(file)
            # print(data)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filename} could not be found.")
    except PermissionError:
        raise PermissionError(
            f"You do not have permission to read {filename}.")
    except Exception as e:
        raise SystemError(f"An error occurred: {e}")

    return data
