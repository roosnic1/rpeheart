import dateutil.parser

#Lilian Calc funcs
def calcHRCorrected(hrs):
    """correction of HR in each HR (Raendertrimmung und Intervallpausen loeschen),
    all following calculations are based on the corrected HRvalues"""

    duration = dateutil.parser.parse(hrs[len(hrs)-1][0]) - dateutil.parser.parse(hrs[0][0])
    hypothek = 0
    hrsOverHundert = []
    for idx,hr in enumerate(hrs):
        if(int(hr[1]) < 100):
            delta = dateutil.parser.parse(hrs[idx+1][0]) - dateutil.parser.parse(hr[0])
            hypothek += delta.total_seconds()
        else:
            hrsOverHundert.append(int(hr[1]))

    return { 'correctedDuration': (duration.total_seconds() - hypothek),'hrsNew':hrsOverHundert}
    #print (duration.total_seconds() - hypothek) / 60
    #print hrsOverHundert, hypothek, duration

def calcHRmaxTraining(correctedHRs):
    """calculate HRmax per TU"""
    return max(correctedHRs)

def calcHRminTraining(correctedHRs):
    """calculate HRmin per TU"""
    return min(correctedHRs)

def calcHRaverageTraining(correctedHRs):
    """calculate HRaverage per TU"""
    return sum(correctedHRs) / len(correctedHRs)

def calcHRratio(averageHRtraining,minHR,maxHR):
    """calculate HRratio per TU as ((averageHRtraining - minHR) / (maxHR - minHR));
    minHR and maxHR values are to be taken from the init (person) file"""
    return (averageHRtraining - float(minHR)) / (int(maxHR) - int(minHR))

def calcDurationHRzones(hrs):
    """calculate duration in minutes per HRzone:
    z0 = <50% HRmax
    z1 = 50% - 60% HRmax
    z2 = 60% - 70% HRmax
    z3 = 70% - 80% HRmax
    z4 = 80% - 90% HRmax
    z5 = 90% - 100% HRmax
    6 new variables will be added"""
    return durationHRz0, durationHRz1, durationHRz2, durationHRz3, durationHRz4, durationHRz5

def calcTRIMP(hrs,geschlecht,correctedDuration):
    """calculate TRIMP with the following gender specific formulas:
    for male athletes (geschlecht = 1): correctedDuration * ratioHR * 0.64 * e^(1.92 * ratioHR)
    for female athletes (geschlecht = 2): correctedDuration * ratioHR * 0.86 * e^(1.67* ratioHR)"""
    return TRIMP

def calcEdwards(durationHRz1,durationHRz2,durationHRz3,durationHRz4,durationHRz5,factor):
    """calculate Edwards = durationHRz1 * 1 + durationHRz2 * 2 + durationHRz3 * 3 + durationHRz4 * 4 + durationHRz5* 5"""
    return edwards

def calcsRPE(rpe,correctedDuration):
    """calculate sRPE = RPE  * correctedDuration"""
    return sRPE
