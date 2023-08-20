try:
    # Prompt the user to input their ID number
    input = str(input("Enter your ID number, ex (3020_____): ")).strip()

    # Check if the input length is valid (14 characters)
    if len(input) == 14:
        print("Valid ID number") 
        id_num = input # Store the valid ID number

    # Function to map Governorate Codes to Governorate Names
    def country_code_filter(Governorate_Code):
        Governorate = {
            '01': 'القاهرة',
            '02': 'الإسكندرية',
            '03': 'بورسعيد',
            '04': 'السويس',
            '11': 'دمياط',
            '12': 'الدقهلية',
            '13': 'الشرقية',
            '14': 'القليوبية',
            '15': 'كفر الشيخ',
            '16': 'الغربية',
            '17': 'المنوفية',
            '18': 'البحيرة',
            '19': 'الإسماعيلية',
            '21': 'الجيزة',
            '22': 'بني سويف',
            '23': 'الفيوم',
            '24': 'المنيا',
            '25': 'أسيوط',
            '26': 'سوهاج',
            '27': 'قنا',
            '28': 'أسوان',
            '29': 'الأقصر',
            '31': 'البحر الأحمر',
            '32': 'الوادي الجديد',
            '33': 'مطروح',
            '34': 'شمال سيناء',
            '35': 'جنوب سيناء',
            '88': 'خارج جمهوري'
        }
        return Governorate.get(Governorate_Code, 'لم يتم التعرف على المحافظة')
    
     # Extract the Governorate Code from the ID number and get the Governorate Name
    country_name = country_code_filter(id_num[7:9])
    print("Governorate:", country_name)

    # Function to determine the century based on the first character
    def century(c):
        if c[0] == '2':
            return '19'
        elif c[0] == '3':
            return '20'
        else:
            return 'Invalid century'
    # Determine the century of birth using the first character of the ID number    
    print(f'century:{century(id_num)}')

    # Function to extract the birth year from the ID number
    def date_of_birth(date):
         Y = date[1:3]
         M = date[3:5]   
         D = date[5:7]
         if date[0] == '2':
             year  =  f'Year: 19{Y}'
             month =   f'Month: {M}'  
             day =   f'Day: {D}'  
             return  year , month  ,day
         
         elif date[0] == '3':
             year  =  f'Year: 20{Y} '
             month =   f'Month: {M}'  
             day =   f'Day: {D}'  
             return  year , month  ,day      
         else:
             return 'Invalid date of birth' 
    # Extract and print the full birth year using the appropriate century
    print(date_of_birth(id_num)) 
    def gender(g):
        if g[-2] in ('1', '3', '5', '7', '9'):
            return 'ذكر'  # Male
        elif g[-2] in ('2', '4', '6', '8'):
            return 'أنثى'  # Female
        # Uncomment the following lines if you want to handle an "Invalid Gender" case
        else:
            return 'جنس غير صحيح'
    print(gender(id_num))  


except:
        # Handle the case of an invalid ID number
        print("Invalid ID number")
        input= str(input("Enter your ID number: ")).strip()