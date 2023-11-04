# TODO Напишите функцию find_common_participants
def find_common_participants(first_group: str, second_group: str, split=",") -> list:
    first_group_set = set(first_group.split(split))
    second_group_set = set(second_group.split(split))
    common = list(first_group_set.intersection(second_group_set))
    common.sort()
    return common


# Тест № 1
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))

# Тест № 2
participants_first_group = "Шемякин,Петров,Молодяков"
participants_second_group = "Касилов,Шемякин,Жарко"
print(find_common_participants(participants_first_group, participants_second_group))

# Тест № 3
participants_first_group = "Шемякин%Петров%Фёдоров%Молодяков%Червинский%Жарко"
participants_second_group = "Жарко%Жарко%Касилов%Фёдоров"
print(find_common_participants(participants_first_group, participants_second_group, "%"))
