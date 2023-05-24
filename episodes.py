import re

episodes_titles =input("Enter Blacklist episode") or '''
Blacklist S01E01:Pilot
Blacklist S01E02:The Freelancer
Blacklist S01E03:Wujing
Blacklist S01E04:The Stewmaker
Blacklist S01E05:The Courier
Blacklist S01E06:Gina Zanetakos
Blacklist S01E07:Frederick Barnes
Blacklist S01E08:General Ludd
Blacklist S01E09:Anslo Garrick
Blacklist S01E10:Anslo Garrick Conclusion
Blacklist S01E11:The Good samaritan
Blacklist S01E12:The Alchemist
Blacklist S01E13:The Cyprus Agency
Blacklist S01E14:Madeline Pratt
Blacklist S01E15:The Judge
Blacklist S01E16:Mako Tanida
Blacklist S01E17:Ivan
Blacklist S01E18:Milton Bobbit
Blacklist S01E19:The Pavlovich Brothers
Blacklist S01E20:The Kingmaker
Blacklist S02E21:Berlin
Blacklist S02E22:Berlin Conclusion
Blacklist S02E01:Lord Baltimore
Blacklist S02E02:Monarch Douglas Bank
Blacklist S02E03:Dr james Convigton
Blacklist S02E04:Dr Linus
Blacklist S02E05:The Front
Blacklist S02E06:The Mombasa Cartel 
Blacklist S02E07:The Scimitar
Blacklist S02E08:The Decembrist
Blacklist S02E09:Luther Braxton
Blacklist S02E10:Luther Braxton Conclusion
Blacklist S02E11:Ruslan Denisov
Blacklist S02E12:The Kenyon Family
Blacklist S02E13:The Deer Hunter
Blacklist S02E14:T Earl King VI
Blacklist S02E15:The Major
Blacklist S02E16:Tom Keen
Blacklist S02E17:The Longevity Iniative
Blacklist S02E18:Vanessa Cruz
Blacklist S02E19:Leonard Caul
legacy
Blacklist S02E20:Quon Zhang
Blacklist S02E21:Karakurt
Blacklist S02E22:Tom Connoly
Blacklist S03E01:The Troll Farmer
Blacklist S03E02:Marvin Gerard
Blacklist S03E03:Eli Matchett
Blacklist S03E04:The Djinn
Blacklist S03E05:Arioch Cain
Blacklist S03E06:Sir Crispin Crandall
Blacklist S03E07:Zal Bin Hasaan
Blacklist S03E08:Kings of the Highway
Blacklist S03E09:The Director
the 100
Blacklist S03E10:The Director Conclusion
Blacklist S03E11:Mr Gregory Devry
Blacklist S03E12:The Vehm
Blacklist S03E13:Alistair Pitt
Blacklist S03E14:Lady Ambrosia
/the grim
Blacklist S03E15:The Dexel
Blacklist S03E16:The Caretaker
Blacklist S03E17:Mr Caretaker
Blacklist S03E18:Mr Solomon
Blacklist S03E19:Mr Solomon Conclusion
Blacklist S03E20:Cape May
Blacklist S03E21:The Artax Network
goodgirls
Blacklist S03E22:Susan Hargave
Blacklist S03E23:Alexander Kirk
Blacklist S03E24:Alexander Kirk Conclusion '''

regular_expression = r'(.*?)\s(S\d{2}E\d{2}):(.*)'
title_data = re.findall(regular_expression, episodes_titles)
for x in title_data:
 print(x)
