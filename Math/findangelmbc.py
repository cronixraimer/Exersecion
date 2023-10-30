import math

user_input_1 = int(input().strip())
user_input_2 = int(input().strip())

angle_rag = math.atan(user_input_1 / user_input_2)

angel_deg = math.degrees(angle_rag)

print(round(angel_deg),'\N{DEGREE SIGN}',sep='')
