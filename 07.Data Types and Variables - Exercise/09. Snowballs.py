import sys
snowballs = int(input())
max_result = -sys.maxsize - 1
while snowballs:
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    result = (snowball_snow / snowball_time) ** snowball_quality
    if max_result < result:
        max_snowball_snow = snowball_snow
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality
        max_result = result
    snowballs -= 1
print(f"{max_snowball_snow} : {max_snowball_time} = {max_result:.0f} ({max_snowball_quality})")
