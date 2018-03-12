import os
import csv

employee_path1 = os.path.join('employee_data1.csv')
employee_path2 = os.path.join('employee_data2.csv')

#create lists to store original data
emp_id = []
dob = []
ssn = []
state = []

#lists to take edited data
first_name = []
last_name = []
hidden_ssn = []
formatted_dob = []
state_abbrev = []

#drop in the state abbreviations dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#read the data in and make lists from the data from the first csv
with open(employee_path1, newline='') as employee_csv1:
    employee_reader1 = csv.reader(employee_csv1, delimiter=",")
    next(employee_reader1)

    for row in employee_reader1:
        
        #grab the employee id
        emp_id.append(row[0])

        #create the hidden ssn list
        ssn = row[3].split('-')
        hidden_ssn.append('***-**-' + ssn[2])

        #split the name into two lists
        f_name = row[1].split(" ")
        first_name.append(f_name[0])

        l_name = row[1].split(" ")
        last_name.append(l_name[1])

        #grab the DOB and reformat it
        dob = row[2].split('-')
        formatted_dob.append(dob[1] + '/' + dob[2] + '/' + dob[0])        

        #change state names to abbreviations
        state = row[4]
        state_abbrev.append(us_state_abbrev[state])

#do everything agin for the second employee list
with open(employee_path2, newline='') as employee_csv2:
    employee_reader2 = csv.reader(employee_csv2, delimiter=",")
    next(employee_reader2)

    for row in employee_reader2:
        
        #grab the employee id
        emp_id.append(row[0])

        #create the hidden ssn list
        ssn = row[3].split('-')
        hidden_ssn.append('***-**-' + ssn[2])

        #split the name into two lists
        f_name = row[1].split(" ")
        first_name.append(f_name[0])

        l_name = row[1].split(" ")
        last_name.append(l_name[1])

        #grab the DOB and reformat it
        dob = row[2].split('-')
        formatted_dob.append(dob[1] + '/' + dob[2] + '/' + dob[0])        

        #change state names to abbreviations
        state = row[4]
        state_abbrev.append(us_state_abbrev[state])

#zip the lists together
#Emp ID,First Name,Last Name,DOB,SSN,State
employee_list = zip(emp_id, first_name, last_name, formatted_dob, hidden_ssn, state_abbrev)

#create an output file
output_file = os.path.join('Employee_list.csv') 

#write stuff to the output file (including writing a header row!)
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(['Employee ID', 'First Name', 'Last Name', 'Date of Birth', 'SSN', 'State'])

    writer.writerows(employee_list)