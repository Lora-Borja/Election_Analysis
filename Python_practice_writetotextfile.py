#Add our dependencies.
import os

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    #Write three counties to the file.
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

#Close the file
txt_file.close()