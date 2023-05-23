import re

date =  input("Enter date (dd-MMM-yyyy): ") or """22-MAY-2023
05-JAN-2022
25-DEC-2001
06-MAR-1957
01-JUL-2004
23-OCT-1990
21-SEP-1909
08-NOV-2019
23-JUN-2026
12-FEB-2011
26-APR-1998
29-AUG-2013
14-FEB-2024
18-SEP-2020
15-JUN-2005
01-JAN-2006
02-NOV-2000
26-DEC-2001
15-MAY-2022
23-SEP-2021
14-JUN-2022
31-OCT-1966
29-FEB-2024
20-MAR-2025
25-DEC-2023
"""
date_regex = r'\d{2}[-]\w+[-]\d{4}'


date_match= re.findall(date_regex,date)
for m in date_match:
    print(m)
          
