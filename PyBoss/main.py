#Import the os module to create file paths
import os

#Import module to read and write CVS files
import csv

#use state abreviations dictionary
abbrev_dict = {
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


# Specify the location of the files to read and write --> employee_data1.csv is the Source and formated_employee_data1.csv the new one
input_file = os.path.join('raw_data','employee_data1.csv')
output_file = os.path.join('formated_employee_data1.csv')

#Create lists to store the data to be used for modifying the file
emp_id = []
full_name = []
dob = []
formated_dob = []
ssn = []
formated_ssn = []
state = []

# Use this lists to be able to separate the Name into First Name and Last Name
first_name = []
last_name = []

# Use below lists to modify the original Date to the MM/DD/YYYY format.
dob_year = []
dob_month = []
dob_day = []

# Use these lists to look for the abbreviation of the State based on the dictionary
name_to_abbr = []
abbrev = []

with open(input_file, newline='') as csvfile:

    # csvreader is used to store the contents of the original CSV file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Loop through csv reader and store data into the different lists
    for row in csvreader:
        emp_id.append(row[0])
        full_name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])   

# Discard the Header
full_name.pop(0)
dob.pop(0)
ssn.pop(0)
state.pop(0)
emp_id.pop(0)

# Use below loop to : 1. Separate the last name from Name 2. Format the Date according to the request 
# 3. Replace the last 6 digits of the S/N with "*" 4. Change the state from full name to only two letters
for i in range(len(full_name)):
    first_name.append(full_name[i].split(" ")[0])
    last_name.append(full_name[i].split(" ")[1])

    dob_year.append(dob[i].split("-")[0])
    dob_month.append(dob[i].split("-")[1])
    dob_day.append(dob[i].split("-")[2])
    formated_dob.append(f"{dob_month[i]}/{dob_day[i]}/{dob_year[i]}")
    ssn[i]= ssn[i].replace(ssn[i][0:6],"***-**")
        
    for key in abbrev_dict.keys():
        if state[i] == key:
            state[i] = abbrev_dict[key]


# Use below code to write the new file with the information based on the request
with open(output_file, 'w', newline='') as csvfile:

# Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

# Write column headers on the first row
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])

# Use this loop to write the new file with the new formatted information
    for i in range(len(emp_id)):
        csvwriter.writerow([emp_id[i],first_name[i],last_name[i],formated_dob[i],ssn[i],state[i]])