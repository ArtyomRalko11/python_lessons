phone = {
    "first_name": "Ben",
    "last_name": "Dover",
    "email": ["okpon@gmail.com", "ponnnnnnnn@okpon.com"],
    "phones": [
        {
            "number": "123",
            "type": "home"
        },
        {
            "number": "678",
            "type": "work"
        },
    ],
    "private": "22848691961",
    "work": "1481928919",
    "notes": {
        "birthday": "01/01/2011",
        "special": {
            "name": "aaaaaaaaa",
            "nickname": "OkPon22848"

        }
    }
}
#вывести имя:
print(phone["first_name"])
#вывести второй емэйл:
print(phone["email"][1])
#вывести никнейм:
print(phone["notes"]["special"]["nickname"])

