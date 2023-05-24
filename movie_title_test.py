import re
movie_title = """
The title of the movie is Whispering Shadows (2019)
Midnight Mirage (2022)
Dancing in the Rain (2008)
The Secret Code (2015)
Titanic (1997)
The Matrix (1999)
Jurassic Park (1993)
"""

movie_title_regex = r'(.*) \((\d{4})\)'


patterns = re.findall(movie_title_regex, movie_title)
for pattern in patterns:
    print(pattern)