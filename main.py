import sys
import getopt
import csv

def start_import():
    print "I'm importing"

    with open('data/init.csv', 'rU') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row]
        header = rows[0]

        print header
        for row in rows[1:]:
            print row


# Main Functions
if __name__ == "__main__":
    start_import()