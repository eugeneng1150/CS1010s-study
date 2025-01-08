import csv
def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

###
### Question 1
###
def monthly_avg(fname, currency, year, component):
    pass

###
### Question 2
###
def highest_gain(fname, year, component):
    pass

# Tests
def test_q1():
    print(monthly_avg('crypto.csv', 'ETH', 2017, 'Close') == \
        {'Nov': 296.4443, 'Oct': 306.2474, 'Sep': 293.0473, 
         'Aug': 301.6094, 'Jul': 224.1239, 'Jun': 313.7343, 
         'May': 125.7494, 'Apr': 50.3367, 'Mar': 34.7916, 
         'Feb': 12.3711, 'Jan': 10.2013})

    print(monthly_avg('crypto.csv', 'BTC', 2013, 'High') == \
        {'Dec': 856.4419, 'Nov': 569.307, 'Oct': 161.9442, 
         'Sep': 134.164, 'Aug': 116.0023, 'Jul': 93.869, 
         'Jun': 111.3007, 'May': 123.949, 'Apr': 143.4667})


def test_q2():
    print(highest_gain('crypto.csv', 2017, "Volume") == \
        {'Nov': ('XPR', 695.17), 'Oct': ('XPR', 3485.19), 
         'Sep': ('LTC', 1792.14), 'Aug': ('XPR', 5524.07), 
         'Jul': ('LTC', 1354.52), 'Jun': ('XPR', 1071.13), 
         'May': ('ETH', 2302.35), 'Apr': ('XPR', 4537.85), 
         'Mar': ('XPR', 7003.02), 'Feb': ('ETH', 1049.67), 
         'Jan': ('XPR', 1975.93)})
 
    print(highest_gain('crypto.csv', 2013, "Market Cap") == \
        {'Dec': ('XPR', 272.37), 'Nov': ('LTC', 1862.94), 
         'Oct': ('BTC', 88.94), 'Sep': ('XPR', 171.23), 
         'Aug': ('XPR', 109.9), 'Jul': ('BTC', 59.08), 
         'Jun': ('LTC', 52.22), 'May': ('LTC', 48.27), 
         'Apr': ('BTC', 7.15)})

#test_q1()
#test_q2()
