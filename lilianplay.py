#Lilian Calc funcs
def calHRCorrected(hrs):
    """correction of HR in each HR (Rändertrimmung und Intervallpausen löschen),
    all following calculations are based on the corrected HRvalues"""
    return correctedHR

def calcCorrectedDuration(hrs):
    #calculate duration after correction of HR files
    return correctedDuration

def calcHRmax(hrs):
    #calculate HRmax per TU
    return maxHR

def calcHRmin(hrs):
    #calculate HRmin per TU
    return minHR

def calcHRaverage(hrs):
    #calculate HR average per TU
    return averageHR

def calcDurationHRzones(hrs):
    """calculate duration in minutes per HRzone:
    z0 = <50% HRmax
    z1 = 50% - 60% HRmax
    z2 = 60% - 70% HRmax
    z3 = 70% - 80% HRmax
    z4 = 80% - 90% HRmax
    z5 = 90% - 100% HRmax
    6 new variables will be added"""
    return durationHRzones

def calcTRIMP(hrs,geschlecht,constant):
    #
    return TRIMP

def calcEdwards(durationHRzones,zoneNr):
    #calculate Edwards = minutes in z1 * 1 + minutes in z2 * 2 + minutes in z3 * 3 + minutes in z4 * 4 + minutes in z5 * 5
    return edwards

def calcsRPE(rpe,duration):
    #calculate sRPE = RPE value * training duration in minutes
    return sRPE
