import re
movies = input("movie") or '''
Whispering Shadows (2019)
Midnight Mirage (2022)
Dancing in the Rain (2008)
The Secret Code (2015)
Lost in Time (2011)
Flickering Flames (2020)
The Enchanted Forest (2017)
Eternal Echoes (2023)
The Silent Witness (2014)
Beyond the Horizon (2016)
Moonlit Serenade (2009)
The Glass Heart (2021)
Shadows of Doubt (2013)
Whirlwind Romance (2018)
The Forgotten Land (2010)
Spiderman Far from Home (2019)
2012 (2009)
Red Notice (2021)
Bumblebee (2018)
Titanic (1997)
The Matrix (1999)
Jurassic Park (1993) '''

regular_expression = r'\b[A-Za-z\s]+\(\d{4}\)'
title_data = re.findall(regular_expression, movies)
for x in title_data:
 print(x)

