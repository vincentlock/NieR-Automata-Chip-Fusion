from helper import IDEAL_FUSION_COSTS

def formatFuseString(chipName, level, cost1, cost2):

    result =  "Fuse " + chipName + "+" + str(level) + "[" + str(cost1) + "] with " \
        + chipName + "+" + str(level) + "[" + str(cost2) + "]"
    return result

def targetLevel8Ideal(chipName, chipCounter):
    fusionInstructions = []
    buildRecurse(chipName, 8, 21, chipCounter, fusionInstructions)
    return fusionInstructions

def buildRecurse(chipName, level, cost, chipCounter, fusionInstructions):
    reqLevel = level - 1
    chip1cost, chip2cost = IDEAL_FUSION_COSTS[level][cost]

    if reqLevel > 0:
        if not chipCounter[chipName][reqLevel][chip1cost] >= 1:
            buildRecurse(chipName, reqLevel, chip1cost, chipCounter, fusionInstructions)
        
        if not chipCounter[chipName][reqLevel][chip2cost] >= 1:
            buildRecurse(chipName, reqLevel, chip2cost, chipCounter, fusionInstructions)
    
    if chipCounter[chipName][reqLevel][chip1cost] >= 1 \
        and chipCounter[chipName][reqLevel][chip2cost] >= 1:
        fusionInstructions.append(formatFuseString(chipName, reqLevel, chip1cost, chip2cost))
        chipCounter[chipName][reqLevel][chip1cost] -= 1
        chipCounter[chipName][reqLevel][chip2cost] -= 1
        chipCounter[chipName][level][cost] += 1
    return

