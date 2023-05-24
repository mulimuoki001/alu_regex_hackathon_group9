import re

date = input("Enter date (dd-MMM-yyyy): ") or """
24-MAY-2023
25-DEC-2022
11-DEC-2021
23-SEP-2004
06-MAR-1957
05-JAN-2023
19-Feb-2023
07-Nov-2021
23-Aug-2020
06-Jan-2023
30-Jul-2021
12-May-2019
25-Dec-2022
04-Sep-2018
18-Jun-2020
01-Mar-2021
14-Nov-2019
29-Apr-2022
09-Feb-2018
26-Sep-2021
01-JAN-2024
30-Dec-2021
10-MAY-1988
13-APR-1906

"""

date_regex = r'\d{2}[-]\w+[-]\d{4}'

date_match = re.findall(date_regex, date)
for m in date_match:
    print(m)