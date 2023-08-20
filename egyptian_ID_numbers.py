# from datetime import datetime
# import re
# def arabic_to_english(string):
#     string = string.replace(' ', '')
#     new_numbers = list(range(10))
#     persian_decimal = ['&#1776;', '&#1777;', '&#1778;', '&#1779;', '&#1780;', '&#1781;', '&#1782;', '&#1783;', '&#1784;', '&#1785;']
#     arabic_decimal = ['&#1632;', '&#1633;', '&#1634;', '&#1635;', '&#1636;', '&#1637;', '&#1638;', '&#1639;', '&#1640;', '&#1641;']
#     arabic = ['٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩']
#     persian = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']

#     string = string.replace(persian_decimal[0], str(new_numbers[0]))
#     string = string.replace(persian_decimal[1], str(new_numbers[1]))
#     # ... repeat for other elements in the arrays

#     id_number = int(string)
#     return id_number

# def country_code_filter(number):
#     switch = {
#         '01': 'القاهرة',
#         '02': 'الإسكندرية',
#         '03': 'بورسعيد',
#         # ... repeat for other cases
#         '88': 'خارج جمهورية مصر العربية'
#     }
#     return switch.get(number, 'لم يتم التعرف على المحافظة')

# def detect_egyptian_id(id_num):
#     matches = re.match(r'(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)', id_num)
#     if matches and len(matches.groups()) == 14:
#         name = "غير معروف"  # Temp Name
#         gender = matches.group(13)
#         gender = "انثي" if int(gender) % 2 == 0 else "ذكر"

#         born = matches.group(1)
#         born = 1900 if born == '2' else 2000
#         day = matches.group(6) + matches.group(7)
#         month = matches.group(4) + matches.group(5)
#         t = matches.group(1)  # century
#         year = 1700 + 100 * int(t) + int(id_num[1:3])

#         country_code = matches.group(8) + matches.group(9)
#         country_name = country_code_filter(country_code)

#         birthday = f"{year}{month}{day}"
#         current_date = datetime.now()
#         birthdate = datetime.strptime(birthday, "%Y%m%d")
#         age = (current_date - birthdate).days // 365

# # You can add further actions you'd like to take with the extracted information

# # Example usage
# id_num = "..."  # Replace with an actual ID number
# detect_egyptian_id(id_num)
# id_num ='30201010000000'
# def century(c):
#         if c == '2':
#             return '19'
#         elif c == '3':
#             return '20'
#         else:
#             return 'Invalid century'
# print(century(id_num[0]))



    #     return day, month, year















id_num ='30203011506812'
# def date_of_birth(date):
#          Y = date[1:3]
#          M = date[3:5]   
#          D = date[5:7]
#          if date[0] == '2':
#              year  =  f'Year: 19{Y}'
#              month =   f'Month: {M}'  
#              day =   f'Day: {D}'  
#              return  year , month  ,day
         
#          elif date[0] == '3':
#              year  =  f'Year: 20{Y} '
#              month =   f'Month: {M}'  
#              day =   f'Day: {D}'  
#              return  year , month  ,day      
#          else:
#              return 'Invalid date of birth' 
#     # Extract and print the full birth year using the appropriate century
# print(date_of_birth(id_num)) 


# print(id_num[-2])
# def gender(g):
#     if g[-2] in ('1', '3', '5', '7', '9'):
#         return 'ذكر'  # Male
#     elif g[-2] in ('2', '4', '6', '8'):
#         return 'أنثى'  # Female
#     # Uncomment the following lines if you want to handle an "Invalid Gender" case
#     # else:
#     #     return 'جنس غير صحيح'
# print(gender(id_num))  