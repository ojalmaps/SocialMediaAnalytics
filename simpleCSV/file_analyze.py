import csv

def average_data():
    iq = 0
    height = 0
    brain = 0
    weight = 0
    n = 0

    with open("braindata.csv") as brain_data:
        file = csv.reader(brain_data)
        next(file) # skipping header row
        for row in file:
            iq += float(row[0])
            brain += float(row[1])
            height += float(row[2])
            weight += float(row[3])
            n += 1
    print( " Some facts about the brain" )
    print( " Average height "+ str(height / n))
    print(" Average weight "+ str(weight / n))
    print(" Average brain size "+ str(brain / n))
    print(" Average iq "+ str(iq / n))
    print(" Average height/weight ratio " + str(height/ weight))

average_data()
