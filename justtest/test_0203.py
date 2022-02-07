import timeit

# Python 3.9.5

numbers = [k for k in range(1, 100)]


def whileloop(numlist):
    i = 0
    while i < len(numlist):
        if numlist[i] % 2:
            del numlist[i]
            continue
        i += 1
    return numlist


numbers_1 = [j for j in range(1, 100)]


def forloop(numlist):
    for n in numlist:
        if n % 2:
            numlist.remove(n)
    return numlist


print(timeit.timeit("whileloop(numbers)", number=1000, globals=globals()))
print()
print(timeit.timeit("forloop(numbers_1)", number=1000, globals=globals()))
lista = ["yourname", "myname"]
dicta = {"yourname": "Eric", "myname": "Nicko"}
tuplea = ("Holmes", "Shakespear", "Davinci", "Dicaprio")
seta = {"Seoul", "Tokyo", "NW", "Washington"}


def bycountry(func):
    list_api = []

    def packvalues(*args):
        # 함수를 인자로 받고, closure area에서 call
        api = func(*args)
        list_api.append(api)
        print("Dictionary Api gathered safely >>>")

        return list_api

    return packvalues


@bycountry
def dict_todata(country):
    country_data = {country.AsianCountry: country.cityname}
    return country_data


from collections import namedtuple

City_Asia = namedtuple("AsianCity", ["AsianCountry", "cityname"])

# usercountrydata = [("city", "Seoul"), ("continent", "Asia"), ("language", "Korea"), ("numofseasons", 4), ("ifOECD", True)]
# print(usercountrydata[0])
#
#
rok = City_Asia("South Korea", "Seoul")
usa = City_Asia("United States of America", "NY")

dict_todata(rok)
print(dict_todata(usa))
# print(rok.CityName)
# print(rok)
#
#
# class UserAPIConvert(object):
#     def __init__(self, usernamefull, city, continent, language, numofseasons, ifOECD, *args):
#         self._usernamefull = usernamefull
#         self._city = city
#         self._continent = continent
#         self._language = language
#         self._city = city
#         self._numofseasons = numofseasons
#         self._ifOECD = ifOECD
#         self._etc = args
#
#     # def values(self):
