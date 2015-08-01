import sys
import csv
import os.path

import lilianplay as lp


def start_import():
    with open('data/init.csv', 'rU') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row]
        header = rows[0]
        people = []

        for row in rows[1:]: #The number two only for testing. Without it would iterate over all persons
            p = {};
            person = {}
            for i in range(len(header)):
                person[header[i].strip()] = row[i].strip()

            #person['trainingunits'] = getPersInit(person)
            alluntis = []
            for tu in getPersInit(person):
                #print tu
                for i in range(len(header)):
                    tu[header[i].strip()] = row[i].strip()

                tu_sorted = {}
                tu_sorted['ID'] = tu['ID']
                tu_sorted['TU'] = tu['TU']

                #print tu
                alluntis.append(tu_sorted)

            people.append(alluntis)

        print len(people[0])
        #print people[0]
        outputToCSV(people)



def getPersInit(person):
    #print person
    with open('data/' + person['ID'] + '/init.csv', 'rU') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row]
        header = rows[0]
        trainingunits = []

        for row in rows [1:]: #The number two only for testing. Without it would iterate over all persons
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

            if lons['zonesHR'] == 'NAN':
                trainingunit['zonesHR_z0'] = 'NAN'
                trainingunit['zonesHR_z1'] = 'NAN'
                trainingunit['zonesHR_z2'] = 'NAN'
                trainingunit['zonesHR_z3'] = 'NAN'
                trainingunit['zonesHR_z4'] = 'NAN'
                trainingunit['zonesHR_z5'] = 'NAN'
            else:
                trainingunit['zonesHR_z0'] = lons['zonesHR']['z0'] / 60
                trainingunit['zonesHR_z1'] = lons['zonesHR']['z1'] / 60
                trainingunit['zonesHR_z2'] = lons['zonesHR']['z2'] / 60
                trainingunit['zonesHR_z3'] = lons['zonesHR']['z3'] / 60
                trainingunit['zonesHR_z4'] = lons['zonesHR']['z4'] / 60
                trainingunit['zonesHR_z5'] = lons['zonesHR']['z5'] / 60



            trainingunits.append(trainingunit)

        return trainingunits


def getHeartrate(trainingunit,person):
    #print trainingunit

    if not os.path.isfile('data/' + person['ID'] + '/' + trainingunit['TU'] + '.csv'):
        return {'cd':'NAN','maxHRtraining':'NAN','minHRtraining':'NAN','avgHRtraining':'NAN','zonesHR':'NAN','trimp':'NAN','edwards':'NAN','srpe':'NAN','hypothek':'NAN'}

    with open('data/' + person['ID'] + '/' + trainingunit['TU'] + '.csv', 'rU') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row]
        hrs = []
        for row in rows [1:]: #The number two only for testing. Without it would iterate over all persons
            #heartrate = {}
            tup = row[0], row[1]


            hrs.append(tup)

        calc1 = lp.calcHRCorrected(hrs)

        correctedDuration = calc1['correctedDuration'] / 60
        hrsNew = calc1['hrsNew']
        hrsTimes = calc1['hrsTimes']
        hypothek = calc1['hypothek'] / 60

        maxHRtraining = lp.calcHRmaxTraining(hrsNew)
        minHRtraining = lp.calcHRminTraining(hrsNew)
        averageHRtraining = lp.calcHRaverageTraining(hrsNew)

        zonesHR = lp.calcDurationHRzones(hrsNew,hrsTimes,person['maxHR'])
        ratioHR = lp.calcHRratio(averageHRtraining,person['minHR'],person['maxHR'])
        trimp = lp.calcTRIMP(ratioHR,person['gender'],correctedDuration)
        edwards = lp.calcEdwards(zonesHR)
        srpe = lp.calcsRPE(trainingunit['RPE'],correctedDuration)

        return {'cd':correctedDuration,'maxHRtraining':maxHRtraining,'minHRtraining':minHRtraining,'avgHRtraining':averageHRtraining,'zonesHR':zonesHR,'trimp':trimp,'edwards':edwards,'srpe':srpe,'hypothek':hypothek}




def outputToCSV(people):
    for peop in people:
        with open('out/' + peop[0]['ID'] + '.csv','wb') as f:
            writer = csv.DictWriter(f,peop[0].keys())
            writer.writeheader()
            for tu in peop:
                writer.writerow(tu)



# Main Functions
if __name__ == "__main__":
    start_import()
