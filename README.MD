Python CourseWork Fall 2017 
Farhan Islam

Requirements:
Python3
UnitTest module

What this program should do:
"Write a script that takes the following CSV (https://blockchain.info/charts/market-price) and can tell the user the following information:

What was the greatest percent increase over the previous day, and what day was it?
What was the greatest percent decrease over the previous day, and what day was it?
What is the highest price in the the data, and what day was it?"


Usage:
1.either git clone or download the repository
2.use terminal or cmd and navigate into the downloaded repository folder
3.to run the program with the given csv file type in
"python3 get_request.py -f market-price.csv" or for the latest csv file from the url type in "python3 get_request -u https://api.blockchain.info/charts/market-price?format=csv"
4. to run the unittest type in "python3 testrunner.py"
or "python3 -m unittest test.py"
