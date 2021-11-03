from enum import Enum, auto

# можно задавать самим
class WeekDays(Enum):
    MON = "понедельник"
    TUE = "вторник"
    WED = "среда"
    THU = "четверг"
    FRI = "пятница"
    SUT = "суббота"
    SUN = "воскресенье"


day = WeekDays.SUN
if day == WeekDays.MON:
    print("Это понедельник")
elif day == WeekDays.TUE:
    print("Это вторник")
elif day == WeekDays.WED:
    print("Это среда")
elif day == WeekDays.TUE:
    print("Это четверг")
else:
    print(f"Это {day.value}")

# можно задавать автоматически, если значение не важно
class BigMac(Enum):
    ORIGINAL = auto()
    SPICY = auto()
    WITH_BACON = auto()


bigmac = BigMac.ORIGINAL
print(bigmac, bigmac._value_, bigmac._name_)
