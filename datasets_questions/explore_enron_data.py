#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
lastname = "Skilling".upper()
firstname = "Jeffrey".upper()
print enron_data[lastname+" "+firstname+" K"]

salaryCount = 0
emailCount = 0
count = 0
for i in enron_data:
    if enron_data[i]['poi']==True:
        count+=1

print count

nanCount = 0
for i in enron_data:
    if enron_data[i]["total_payments"]=='NaN':
        nanCount+=1
print float(nanCount)/len(enron_data)




