import re 

twitter_handles = input("enter teitter handles: ") or '''
@WhimsicalWanderer
@ElectricDreamer
@MidnightWhisper
@SunnySideUp
@PixelEnthusiast
@ChaosMagnet
@MoonlitMelody
charite.com
___twembi '''


regular_expression = r'@\w+'

regex = re.findall(regular_expression, twitter_handles)
for x in regex:
    print(x)
