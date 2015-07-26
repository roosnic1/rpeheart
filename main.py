import sys
import csv

import lilianplay as lp


def start_import():
    with open('data/init.csv', 'rU') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row]
        header = rows[0]
        people = []

        for row in rows[1:2]: #The number two only for testing. Without it would iterate over all persons
            person = {}
            for i in range(len(header)):
                person[header[i].strip()] = row[i].strip()

            person['trainingunits'] = getPersInit(person)
            #people.extend(person)
            #print person

        #print len(people)



def getPersInit(person):
    #print person
    with open('data/' + person['ID'] + '/init.csv', 'rU') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row]
        header = rows[0]
        trainingunits = []

        for row in rows [1:2]: #The number two only for testing. Without it would iterate over all persons
            trainingunit = {}
            for i in range(len(header)):
                trainingunit[header[i]] = row[i]

            lons = getHeartrate(trainingunit,person)
            trainingunit['correctedDuration'] = lons['cd']
            trainingunit['trimp'] = lons['trimp']
            trainingunit['edwards'] = lons['edwards']
            trainingunit['srpe'] = lons['srpe']
            trainingunit['hypothek'] = lons['hypothek']
            trainingunit['maxHRtraining'] = lons['maxHRtraining']
            trainingunit['minHRtraining'] = lons['minHRtraining']
            trainingunit['avgHRtraining'] = lons['avgHRtraining']
            trainingunit['zonesHR'] = lons['zonesHR']

            trainingunits.extend(trainingunit)

        #return trainingunits
        


def getHeartrate(trainingunit,person):
    #print trainingunit
    with open('data/' + person['ID'] + '/' + trainingunit['TU'] + '.csv', 'rU') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row]
        hrs = []
        for row in rows [1:]: #The number two only for testing. Without it would iterate over all persons
            #heartrate = {}
            tup = row[0], row[1]


            hrs.append(tup)

        calc1 = lp.calcHRCorrected(hrs)

        correctedDuration = calc1['correctedDuration']
        hrsNew = calc1['hrsNew']
        hrsTimes = calc1['hrsTimes']
        hypothek = calc1['hypothek']

        maxHRtraining = lp.calcHRmaxTraining(hrsNew)
        minHRtraining = lp.calcHRminTraining(hrsNew)
        averageHRtraining = lp.calcHRaverageTraining(hrsNew)

        zonesHR = lp.calcDurationHRzones(hrsNew,hrsTimes,person['maxHR'])
        ratioHR = lp.calcHRratio(averageHRtraining,person['minHR'],person['maxHR'])
        trimp = lp.calcTRIMP(ratioHR,person['gender'],correctedDuration)
        edwards = lp.calcEdwards(zonesHR)
        srpe = lp.calcsRPE(trainingunit['RPE'],correctedDuration)

        return {'cd':correctedDuration,'maxHRtraining':maxHRtraining,'minHRtraining':minHRtraining,'avgHRtraining':averageHRtraining,'zonesHR':zonesHR,'trimp':trimp,'edwards':edwards,'srpe':srpe,'hypothek':hypothek}






# Main Functions
if __name__ == "__main__":
    start_import()
