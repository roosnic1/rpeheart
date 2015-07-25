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
                person[header[i].strip()] = row[i]

            #print person
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

            heartrates = getHeartrate(trainingunit,person)


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

            #print tup
            hrs.append(tup)

        calc1 = lp.calcHRCorrected(hrs)

        duration = calc1['correctedDuration']
        hrsNew = calc1['hrsNew']

        maxHRtraining = lp.calcHRmaxTraining(hrsNew)
        minHRtraining = lp.calcHRminTraining(hrsNew)
        averageHRtraining = lp.calcHRaverageTraining(hrsNew)

        lp.calcHRratio(hrsNew,person['minHR'],person['maxHR'])
        #print hrs,duration

        #return heartrates






# Main Functions
if __name__ == "__main__":
    start_import()
