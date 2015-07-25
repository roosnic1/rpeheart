import dateutil.parser
import math

#Lilian Calc funcs
def calcHRCorrected(hrs):
    """correction of HR in each HR (Raendertrimmung und Intervallpausen loeschen),
    all following calculations are based on the corrected HRvalues"""

    duration = dateutil.parser.parse(hrs[len(hrs)-1][0]) - dateutil.parser.parse(hrs[0][0])
    hypothek = 0
    hrsOverHundert = []
    hrsTimes = []
    for idx,hr in enumerate(hrs):
        if(idx == len(hrs)-1):
            break
        delta = dateutil.parser.parse(hrs[idx+1][0]) - dateutil.parser.parse(hr[0])
        if(int(hr[1]) < 100):
            hypothek += delta.total_seconds()
        else:
            hrsOverHundert.append(int(hr[1]))
            hrsTimes.append(delta.total_seconds())


    return { 'correctedDuration': (duration.total_seconds() - hypothek),'hrsNew':hrsOverHundert,'hrsTimes':hrsTimes,'hypothek':hypothek}
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

def calcDurationHRzones(correctedHRs,correctedHRsTimes,maxHR):
    """calculate duration in minutes per HRzone:
    z0 = <50% HRmax
    z1 = 50% - 60% HRmax
    z2 = 60% - 70% HRmax
    z3 = 70% - 80% HRmax
    z4 = 80% - 90% HRmax
    z5 = 90% - 100% HRmax
    6 new variables will be added"""
    z0 = 0.0
    z1 = 0.0
    z2 = 0.0
    z3 = 0.0
    z4 = 0.0
    z5 = 0.0

    maxHR = int(maxHR)

    for idx,hr in enumerate(correctedHRs):
        if(hr < maxHR * 0.5):
            z0 += correctedHRsTimes[idx]
        elif(hr < maxHR * 0.6):
            z1 += correctedHRsTimes[idx]
        elif(hr < maxHR * 0.7):
            z2 += correctedHRsTimes[idx]
        elif(hr < maxHR * 0.8):
            z3 += correctedHRsTimes[idx]
        elif(hr < maxHR * 0.9):
            z4 += correctedHRsTimes[idx]
        else:
            z5 += correctedHRsTimes[idx]

    return {'z0':z0,'z1':z1,'z2':z2,'z3':z3,'z4':z4,'z5':z5}

def calcTRIMP(ratioHR,gender,correctedDuration):
    """calculate TRIMP with the following gender specific formulas:
    for male athletes (geschlecht = 1): correctedDuration * ratioHR * 0.64 * e^(1.92 * ratioHR)
    for female athletes (geschlecht = 2): correctedDuration * ratioHR * 0.86 * e^(1.67 * ratioHR)"""
    trimp = 0
    if int(gender) == 1:
        trimp = (correctedDuration / 60) * ratioHR * 0.64 * math.exp(1.92 * ratioHR)
    else:
        trimp = (correctedDuration / 60)* ratioHR * 0.86 * math.exp(1.67 * ratioHR)
    return trimp

def calcEdwards(durationHRz1,durationHRz2,durationHRz3,durationHRz4,durationHRz5,factor):
    """calculate Edwards = durationHRz1 * 1 + durationHRz2 * 2 + durationHRz3 * 3 + durationHRz4 * 4 + durationHRz5* 5"""
    return edwards

def calcsRPE(rpe,correctedDuration):
    """calculate sRPE = RPE  * correctedDuration"""
    sRPE = int(rpe) * (correctedDuration / 60)
    return sRPE
