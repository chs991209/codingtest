import timeit


def namedatagather(name_list, errorcheck=None):  # errorcheck = True or False
    """
    이름의 firstname, lastname을 각각 key, value로 서로 갖는 두 dict를 return
    :param errorcheck:
    :param name_list:
    :return: (firstnamedict, lastnamedict)
    """

    lastnamedict = {}
    firstnamedict = {}  # 신고 userid 기록 dict

    namepairlist_lastname = (j.split() for j in name_list)
    # lastname: [firstname]
    for firstname, lastname in namepairlist_lastname:
        lastnamedict.setdefault(lastname, []).append(firstname)

    namepairlist_first = (j.split() for j in name_list)
    # firstname: [lastname]
    for firstname, lastname in namepairlist_first:
        firstnamedict.setdefault(firstname, []).append(lastname)

    if errorcheck is True:
        for name in name_list:
            if len(name.split()) != 2:
                raise Exception("Input the name as diveded to First Name and Last name")

    return firstnamedict, lastnamedict


namelist = [
    "Brody Hahn",
    "Augustus Ochoa",
    "Francisco Lucero",
    "Nathan Farley",
    "Memphis Lambert",
    "Brisa Trujillo",
    "Gregory Villa",
    "Ian Huynh",
    "Marie Salinas",
    "Rylee Dalton",
    "Allisson Horn",
    "Brynlee Freeman",
    "Mya Walters",
    "Laci Santana",
    "Aurora Fitzpatrick",
    "Bentley Rivera",
    "Arjun Gonzalez",
    "Reid Goodwin",
    "Annie Andersen",
    "Eva Fry",
    "Messiah Roberts",
    "Jadiel Stewart",
    "Cora Church",
    "Anastasia Rich",
    "Jordyn Mcconnell",
    "Branden Spencer",
    "Carlee Ross",
]

print(timeit.timeit("namedatagather(namelist)", number=1000, globals=globals()))


print(namedatagather(namelist))

# 여러 pyfile에서 같은 소스의 데이터를 처리해야 하는 경우
# namedict data를 불러오는 과정을 subclass에 넣고,
# data를 특정 url이나 class나 func로 보내주는 과정을 decorator로 생성한다.
# data를 보내주는 과정을 abs method로 생성해 반드시 포함하게 하고,
# data를 불러오는 과정 또한 abs method로 생성해 반드시 포함하게 한다.
# 이후 해당 pyfile에서 data를 후처리하는 과정은 자율적으로 한다.
