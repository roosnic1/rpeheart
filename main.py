import sys
import getopt
import csv


def start_import():
    with open('data/init.csv', 'rU') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row]
        header = rows[0]

        for row in rows[1:2]: #The number two only for testing. Without it would iterate over all persons
            person = {}
            for i in range(len(header)):
                person[header[i]] = row[i]

            getPersInit(person)


def getPersInit(person):
    #print person
    with open('data/' + person['ID'] + '/init.csv', 'rU') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row]
        header = rows[0]

        for row in rows [1:2]: #The number two only for testing. Without it would iterate over all persons
            trainingunit = {}
            for i in range(len(header)):
                trainingunit[header[i]] = row[i]

            getHeartrate(trainingunit,person['ID'])


def getHeartrate(trainingunit,personId):
    #print trainingunit
    with open('data/' + personId + '/' + trainingunit['TU'] + '.csv', 'rU') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row]
        header = rows[0]
        heartrates = []
        for row in rows [1:]: #The number two only for testing. Without it would iterate over all persons
            heartrate = {}
            tup = row[0], row[1]

            #print tup
            heartrates.extend(tup)

        print heartrates







# Main Functions
if __name__ == "__main__":
    start_import()