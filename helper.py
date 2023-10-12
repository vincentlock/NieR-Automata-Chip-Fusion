import json

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


def extractChipInfo(filename):
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
