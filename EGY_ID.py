import datetime # Import the datetime module to work with dates and times
# Print a header with the current date
print(F'-------------------------------- TODAY: {datetime.datetime.now().day} {datetime.datetime.now().strftime("%B")} {datetime.datetime.now().year} --------------------------------', end='\n\n')

# Prompt the user to input their ID number
input = str(input("Enter Your ID Number, Such As (3020_____): ")).strip()
id_num = input # Store the valid ID number'

# Extract birthdate information from the ID number
if id_num[0] == '2':
    year  =  (int(f'19{id_num[1:3]}')) 
    month =  (int(f'{id_num[3:5]}'))  
    day =    (int(f'{id_num[5:7]}')) 
    Weekday = datetime.datetime(year,month,day).strftime('%A')  
    print(F'Born on: {Weekday} {day}-{month}-{year}')
elif id_num[0] == '3':
    year  =  (int(f'20{id_num[1:3]}')) 
    month =  (int(f'{id_num[3:5]}'))  
    day =    (int(f'{id_num[5:7]}')) 
    Weekday = datetime.datetime(year,month,day).strftime('%A')
    print(F'Born on: {Weekday} {day}-{month}-{year}')


# Check if the input length is valid (14 characters)
if len(input) == 14 and type(input) == str:
    id_num = input # Store the valid ID number

# Function to determine the century based on the first character
def century(c):
    if c[0] == '2':
        return '19'
    elif c[0] == '3':
        return '20'
    else:
        return 'Invalid century'
# print(f'century: {century(id_num)}th')

# Define a function to map Governorate Codes to Governorate Names
def country_code_filter(Governorate_Code):
# Dictionary to map Governorate Codes to Names
    Governorate = {
        '01': 'Cairo',
         '02': 'Alexandria',
         '03': 'Port Said',
         '04': 'Suez',
         '11': 'Damietta',
         '12': 'Dakahlia',
         '13': 'Eastern',
         '14': 'Qalyubia',
         '15': 'Kafr El-Sheikh',
         '16': 'Western',
         '17': 'Monofia',
         '18': 'The Lake',
         '19': 'Ismailia',
         '21': 'Giza',
         '22': 'Bani Suef',
         '23': 'Fayoum',
         '24': 'Minya',
         '25': 'Assiut',
         '26': 'Sohag',
         '27': 'Qena',
         '28': 'Aswan',
         '29': 'Luxor',
         '31': 'The Red Sea',
         '32': 'The New Valley',
         '33': 'Matrouh',
         '34': 'North Sinai',
         '35': 'South Sinai',
         '88': 'outside the republic'
    }
    return Governorate.get(Governorate_Code, 'Governorate Is Invalid')
# Define a function to determine gender based on the ID number   
def gender(g):
        if g[-2] in ('1', '3', '5', '7', '9'):
            return 'Gender: Male'  
        elif g[-2] in ('2', '4', '6', '8'):
            return 'Gender: Female'  
        # Uncomment the following lines if you want to handle an "Invalid Gender" case
        else:
            return 'Incorrect Gender'
print(gender(id_num))  


# Extract the Governorate Code from the ID number and get the Governorate Name
country_name = country_code_filter(id_num[7:9])
print("Governorate:", country_name)
    
# Get the current date and time

# Define a function to calculate and print age and various time intervals
current_datetime = datetime.datetime.now()
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day
def calculate_age(id_num): 

         if id_num[0] == '2':
             year  =  int(f'19{id_num[1:3]}') 
             month =   int(f'{id_num[3:5]}')  
             day =    int(f'{id_num[5:7]}')  

             birth_date = datetime.datetime(year, month, day)
             current_date = datetime.datetime(current_year, current_month, current_day)
             year_diff = current_date.year - birth_date.year
             month_diff = current_date.month - birth_date.month
             day_diff = current_date.day - birth_date.day

             if day_diff < 0:
               month_diff -= 1
               day_diff += 30  # Assuming an average month length
    
             if month_diff < 0:
               year_diff -= 1
               month_diff += 12

             leap_years = sum(1 for year in range(birth_date.year, current_date.year + 1) if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
             days_in_leap_years = leap_years
             age_years = year_diff
             age_months = month_diff
             age_days = day_diff + days_in_leap_years
             TOTAL_DAYS = (current_datetime - birth_date).days

             Weekday = birth_date.strftime('%A') 
             OHTER_FORMAT = day.strftime('%D')
             age = current_year - birth_date.year
             print('-------------- Age Calculator  ----------')  
             print(F'Born on: {Weekday} {OHTER_FORMAT}-{month}-{year}')
            #  print(F'Age  on: {current_day} {current_datetime.strftime("%B")} {current_year}')
             print('------------ age in different units: ----------')
             print(F'Your Age Is: {age_years} YEARS {age_months} MONTHS {age_days} DAYS')
             print(F'Your Age Is: {age_years * 12 + age_months} MONTHS {age_days} DAYS')
             print(F'TOTAL_DAYS: {TOTAL_DAYS:,} DAYS')
             print(F'TOTAL_HOURS: {TOTAL_DAYS * 24:,} HOURS')
             print(F'TOTAL_MINUTES: {TOTAL_DAYS * 24 * 60:,} MINUTES')
             print(F'TOTAL_SECOND: {TOTAL_DAYS * 24 * 60 *60:,} SECONDS')
             print('---------------- Success project -----------------')

         elif id_num[0] == '3':
             year  =  int(f'20{id_num[1:3]}') 
             month =   int(f'{id_num[3:5]}')  
             day =    int(f'{id_num[5:7]}')  

             birth_date = datetime.datetime(year, month, day)
             current_date = datetime.datetime(current_year, current_month, current_day)
             year_diff = current_date.year - birth_date.year
             month_diff = current_date.month - birth_date.month
             day_diff = current_date.day - birth_date.day

             if day_diff < 0:
               month_diff -= 1
               day_diff += 30  # Assuming an average month length
    
             if month_diff < 0:
               year_diff -= 1
               month_diff += 12

             leap_years = sum(1 for year in range(birth_date.year, current_date.year + 1) if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
             days_in_leap_years = leap_years

             age_years = year_diff
             age_months = month_diff
             age_days = day_diff + days_in_leap_years
            
    
             TOTAL_DAYS = (current_datetime - birth_date).days
             OHTER_FORMAT = birth_date.strftime('%b')
             Weekday = birth_date.strftime('%A') 
             print('-------------- Age Calculator  ----------')  
             print(F'Born on: {Weekday} {day}-{OHTER_FORMAT}-{year}')
            #  print(F'Age  on: {current_day} {current_datetime.strftime("%B")} {current_year}')
             print('------------ age in different units: ----------')
             print(F'Your Age Is: {age_years} YEARS {age_months} MONTHS {age_days} DAYS')
             print(F'Your Age Is: {age_years * 12 + age_months} MONTHS {age_days} DAYS')
             print(F'TOTAL_DAYS: {TOTAL_DAYS:,} DAYS')
             print(F'TOTAL_HOURS: {TOTAL_DAYS * 24:,} HOURS')
             print(F'TOTAL_MINUTES: {TOTAL_DAYS * 24 * 60:,} MINUTES')
             print(F'TOTAL_SECOND: {TOTAL_DAYS * 24 * 60 *60:,} SECONDS')
             print('---------------- Success project -----------------')
         else:
             return 'Invalid Date' 
# Call the date_of_birth function to calculate and print results
calculate_age(id_num)
       

