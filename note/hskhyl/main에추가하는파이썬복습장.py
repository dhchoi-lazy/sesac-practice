# def create_following_dict(users: list, following: list) -> dict:
#     result = {
#         user: follower for user, follower in zip(users, following) if follower >= 5
#     }
#     print(result)
#     return result


# create_following_dict(["Alice", "Bob", "Charlie"], [3, 7, 5])


# def create_following_dict(users: list, following: list) -> dict:
#     length_users = len(users)
#     result = {}
#     for i in range(length_users):
#         if following[i] >= 5:
#             result[users[i]] = following[i]
#     print(result)
#     return result


# create_following_dict(["Alice", "Bob", "Charlie"], [3, 7, 5])


# def solution(n, k):
#     answer = 12000 * n + 2000 * k
#     print(answer)
#     return answer


# def add(a, b):
#     return a + b


# def subtract(a, b):
#     return a - b


# calc = {"add": add, "subtract": subtract}

# num1 = calc["add"](10, 5)
# num2 = calc["subtract"](10, 5)

# print(num1)
# print(num2)

# numbers = [1, 2, 3, 4, 5]
# squared = map(lambda x: x**2, numbers)
# print(list(squared))


# def power(x):
#     return x**2


# numbers = [1, 2, 3, 4, 5]
# squared = map(power, numbers)
# print(list(squared))


# str_numbers = ["1", "2", "3", "4", "5"]
# int_numbers = map(int, str_numbers)
# print(list(int_numbers))


# def is_even(number):
#     return number % 2 == 0


# numbers = [1, 2, 3, 4, 5]

# even_numbers = filter(is_even, numbers)

# print(list(even_numbers))


# map 이든 filter든 약간 분배법칙 하는 느낌은 비슷한데
# map은 map객체로 다 반환해주고 (연산하는 함수에 좋다)
# filter은 True이면 filter 객체로 반환해준다 (Boolean에 좋다)False이면 따로 안 담음.


# data = [
#     {"date": "2024-01-01", "value": 10},
#     {"date": "2024-01-02", "value": 15},
#     {"date": "2024-01-03", "value": 20},
# ]

# jan_first_data = filter(lambda x: x["date"] == "2024-01-01", data)
# print(list(jan_first_data))

# # 람다 함수는 그냥 작명하기 싫을때 간단하게 처리하는 함수이다


# def drink_alcohol(pid):  # personal id
#     birth_year = int(pid.split("-")[0][:2])
#     millenial = int(pid.split("-")[1][0]) >= 3  # 2000년 이후 출생자들 민증 뒷자리로 첫번째로 구분 가능 3 !
#     if millenial:
#         birth_year = 2000 + birth_year
#     else:
#         birth_year = 1900 + birth_year
#     return 2024 - birth_year >= 20


# students = ["050123-3234567", "850505-1345678", "060404-3456789", "971212-1567890"]
# alcoholer = filter(drink_alcohol, students)
# print(list(alcoholer))


# add = lambda x, y: x + y
# print(add(5, 3))


# strings = [
#     "똘기",
#     "떵이",
#     "호치",
#     "새초미",
#     "드라고",
#     "요롱이",
#     "마초",
#     "미미",
#     "몽치",
#     "키키",
#     "당다리",
#     "찡찡이",
#     "오로라공주",]


# strings.sort(key=lambda s: len(s))
# print("sorted by length:", strings)

# longest_string = max(strings, key=lambda s: len(s))
# print("Longest string:", longest_string)

# shortest_string = min(strings, key=lambda s: len(s))
# print("Shortest string:", shortest_string)


# def fibonacci(n: int) -> int:
#     list = [0, 1]
#     for i in range(2, n + 1):
#         list.append(list[i - 1] + list[i - 2])

#     result = list[n]
#     return result

#     print(list)


# fibonacci(5)
# fibonacci(6)
# fibonacci(0)


# def pokemon_battle(pokemon_a_hp: int = 100, pokemon_b_hp: int = 100) -> str:
#     if pokemon_a_hp - pokemon_b_hp > 0:
#         result = "포켓몬 A 승리"

#     elif pokemon_a_hp - pokemon_b_hp < 0:
#         result = "포켓몬 B 승리"

#     else:
#         result = "무승부"

#     print(result)
#     return result


# pokemon_battle()
# pokemon_battle(pokemon_a_hp=120)


# def plan_trip(*countries) -> str:
#     result = [*countries]
#     RESULT = " -> ".join(result)
#     print(RESULT)
#     return RESULT


# plan_trip("USA", "Korea", "Japan")


# monthly_sales = 2000


# def manage_coffee_shop() -> int:
#     daily_sales = 100
#     result = monthly_sales + daily_sales
#     return result

"""lambda 공부해야할 코드"""
# 내가 삽질한 코드
# def sort_by_last
# _letter(names):
#         names.sort(key= lambda x : names[i][len(x)] for i in range(len(names)))

#     names.sort(reverse=True)
#     return names


# gpt가 알려준 코드 진짜 깔끔하다 !
# def sort_by_last_letter(names):
#     names.sort(key=lambda x: x[-1])
#     return names

# sort_by_last_letter(["Jessie", "Paul", "John"])


# def get_lengths(words):
#     result = list(map(len, words))
#     print(result)
#     return result


# get_lengths(["hello", "world", "python"])


# def filter_air_quality(data, threshold):
#     result = filter(lambda x: x > threshold, data)
#     RESULT = list(result)
#     print(RESULT)
#     return RESULT


# filter_air_quality([50, 40, 60, 90, 30], 50)

"""
def count_up_to(max_number):
    count = 1
    while count <= max_number:
        yield count
        count += 1


counter = count_up_to(5)
for number in counter:
    print(number)
"""


"""
def ticket_generator():
    ticket_number = 1
    while True:
        yield ticket_number
        ticket_number += 1


kiosk = ticket_generator()

print("First ticket:", next(kiosk))

print("second ticket:", next(kiosk))

print("third ticket:", next(kiosk))
"""


# def add_lists(list1, list2):
#     plus = lambda x, y: x + y
#     result = []
#     for i in range(len(list1)):
#         result.append(plus(list1[i], list2[i]))

#     print(result)
#     return result


# add_lists([1, 2, 3], [4, 5, 6])


# def add_lists(list1, list2):
#     result = list(map(lambda x, y: x + y, list1, list2))


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)


# map(), filter,() sorted() 이런애들이랑 lambda가 잘쓰인다.. 왜냐면 그 iterable에 들어가는 요소들을 lambda랑 같이 쓰면
# 한번에 대입하는 등 굉장히 편리해지기 때문이다. 거의 함수정의해서 그 인자값 바로 받는 매개변수 역할을 하는 듯?


# def create_omakase_menu(*ingredients):
#     menu = list(ingredients)
#     result = f"오늘의 오마카세 메뉴: {', '.join(menu)}"
#     print(result)
#     return result


# create_omakase_menu("참치", "연어", "우니")


# my_list = ["apple", "banana", "orange"]
# result = ", ".join(my_list)

# print(result)


# def solution(num_list, n):
#     result = []
#     for i in range(0, len(num_list), n):
#         result.append(num_list[i])
#     print(result)
#     return result


# def solution(num_list, n):
#     print(num_list[::n])
#     return num_list[::n]


# solution(
#     [
#         1,
#         5,
#         94,
#         5,
#         1,
#         949,
#         89,
#         1,
#         89,
#     ],
#     2,
# )
# def solution(n):
#     result = 1 + n // 7
#     if n % 7 == 0:
#         result -= 1

#     return result
