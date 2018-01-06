from main import main
import csv
import requests
import argparse
import datetime


price = []
day = []

mylist = []
today = datetime.date.today()
mylist.append(today)

p = argparse.ArgumentParser()
p.add_argument('-f', help='absolute location of .csv file', dest="file")
p.add_argument('-u', help='url of the .csv file')
args = p.parse_args()

if not (args.file or args.u):
    parser.error('Add -f or -u option')

elif args.file:
    with open(args.file, newline='') as f:
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            price.append(row[1])

            day.append(row[0])
else:
    with requests.Session() as s:
        download = s.get(args.u)
        decoded_content = download.content.decode('utf-8')
        reader = csv.reader(decoded_content.splitlines(), delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            day.append(row[0])
            price.append(row[1])

dataset = list(zip(day, price))

request = main()
print("Percentage of maximum increase :", request.max_rise(dataset))
print("Percentage of maximum fall ", request.max_fall(dataset))
print("Maximum Price:", request.max_price(dataset))
print ("Today's date : ", mylist[0])



            
