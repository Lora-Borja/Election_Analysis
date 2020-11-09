# Election_Analysis

## Project Overview
In this project I assisted a Colorado Board of Elections employee, Tom, in reporting the total number of votes cast, the total number of votes for each candidate, the percentage of votes for each candidate, and the winner of the election based on the popular votes. Using Python, I was tasked to analyze the election data tabulated in a CSV file in order to generate a vote count report to certify the election results.

## Election-Audit Results
![Election_Results_Snapshot](https://github.com/Lora-Borja/Election_Analysis/blob/main/analysis/Election_Results_Snapshot.PNG)

* A total of 369,711 votes were cast in this congressional election
* In the above snapshot of the Election Results, the number of votes and the percentage of total votes for each county are as follows:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

* The Denver county had the highest turnout with the largest number of votes
* In the above snapshot of the Election Results, the number of votes and the percentage of total votes for each candidate are as follows:
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)

* Diana DeGette won the election with a significant total vote count of 272,892 being the highest percentage of total votes at 73.8%


## Election-Audit Summary
Now that we have automated the tasks to analyze this election's data using Python, this is a great opportunity to use the same method in analysing data for any election results throughout the country. Python was fairly easy to write given that the syntax seem much simplier to understand compared to VBA. It also performed any calculations fairly quickly as well when compared to Excel or VBA. The runtime in this tool was also fast considering there was a large amount of data in the CSV file. The existing script can simply be revised to implement different sets of counties and candidates. The process could also be revised to explore writing the summary of the results back into an excel file, instead of a text file, just in case there would be a preference in creating charts or graphs.

## Challenge Summary
* Below is a snapshot of the Election Results Printed to the Command Line
![Election_Results_onCommandline](https://github.com/Lora-Borja/Election_Analysis/blob/main/analysis/Election_Results_onCommandline.PNG)

* Here is a link to the analysis folder where you will find the Elections Results Saved to a Text file

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.51.0
