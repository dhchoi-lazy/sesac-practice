# def drink_alcohol(pid):
#     birth_year=int(pid.split('-')[0][:2])
#     millennial=False if int(pid.split('-')[1][0]) >=3 else False
#     if millennial:
#         birth_year=2000 + birth_year
#     else:
#         birth_year=1900 + birth_year
    
#     return 2024- birth_year >=20

# students=['050123-3234567','850505-4345678',
#           '060404-3456789','971212-4567890']

# alcoholer=filter(drink_alcohol, students)
# print(list(alcoholer))

# def extract_sensor_data(sensor_data: list) -> list:
#     # YOUR CODE HERE
#     result=[]
#     tmp=sensor_data
#     for i in range(len(sensor_data)):
#         if len(tmp[i])%2==0:
#             del_idx=(len(sensor_data)//2)-1
#             t1= tmp[i][del_idx]
#             del tmp[i][del_idx]
#             t2= tmp[i][del_idx]
#             del tmp[i][del_idx]
#             tmp[i][del_idx]=(t1+t2)/2
#     return result

# print(extract_sensor_data([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))


# add=lambda x, y : x + y
# print(add(3, 5))

#문자열 길이에 따라 정렬
strings=['가','나리','다','라','마','바','사','아','자','차','카','타','파','하']
strings.sort(key=lambda s: len(s), reversed=True)
print('Sorted by length:', strings)

#가장 긴 문자열 찾기
longest_string=max(strings, key=lambda s: len(s))
print('Longest string:', longest_string)

#가장 짧은 문자열 찾기
shortest_string=min(strings, key=lambda s: len(s))
print('Shortest string:', shortest_string)