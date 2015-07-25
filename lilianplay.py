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
            #print delta.total_seconds()
            hypothek += delta.total_seconds()
        else:
            hrsOverHundert.append(hr[1])

    return { 'correctedDuration': (duration.total_seconds() - hypothek),'hrs':hrsOverHundert}
    #print (duration.total_seconds() - hypothek) / 60
    #print hrsOverHundert, hypothek, duration



    #return correctedHR

def calcCorrectedDuration(hrs):
    """calculate duration after correction of HR files"""
    return correctedDuration

def calcHRmaxTraining(hrs):
    """calculate HRmax per TU"""
    return maxHRtraining

def calcHRminTraining(hrs):
    """calculate HRmin per TU"""
    return minHRtraining

def calcHRaverageTraining(hrs):
    """calculate HRaverage per TU"""
    return averageHRtraining

def calcHRratio(hrs,minHR,maxHR):
    """calculate HRratio as ((averageHRtraining - minHR) / (maxHR - minHR));
    minHR and maxHR values are to be taken from the init (person) file"""
    return ratioHR

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

def calcTRIMP(hrs,geschlecht,correctedDuration):
    """calculate TRIMP with the following gender specific formula:
    for male athletes (geschlecht = 1): correctedDuration * ratioHR * 0.64 * e^(1.92 * ratioHR)
    for female athletes (geschlecht = 2): correctedDuration * ratioHR * 0.86 * e^(1.67* ratioHR)"""
    return TRIMP

def calcEdwards(durationHRzones,factor):
    """calculate Edwards = minutes in z1 * 1 + minutes in z2 * 2 + minutes in z3 * 3 + minutes in z4 * 4 + minutes in z5 * 5"""
    return edwards

def calcsRPE(rpe,correctedDuration):
    """calculate sRPE = RPE value * training duration in minutes"""
    return sRPE
