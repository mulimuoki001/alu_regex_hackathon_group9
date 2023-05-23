import re

ISBN_numbers = '''
ISBN 123-4-567-89012-3
ISBN 987-6-543-21098-7
ISBN 456-7-890-12345-6
ISBN 321-0-987-65432-1
ISBN 789-1-234-56789-0
ISBN 234-5-678-90123-4
ISBN 876-5-432-10987-6
ISBN 543-2-109-87654-3
ISBN 210-9-876-54321-0
ISBN 678-0-123-45678-9
ISBN 123987321
ISBN 8299283HHD 
08846562
'''
regular_expressions = r'ISBN\s\d{3}[-]\d[-]\d{3}[-]\d{5}[-]\d'

regex = re.findall(regular_expressions, ISBN_numbers)
for x in regex:
    print(x)

