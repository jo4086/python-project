def auto_init(cls):
    def __init__(self, *args, **kwargs):
        attributes = cls.__annotations__
        for i, (key, default) in enumerate(attributes.items()):
            setattr(self, key, args[i] if i < len(args) else kwargs.get(key, default))
    cls.__init__ = __init__
    return cls

@auto_init
class Character:
    name: str = "Unnamed"
    hp: int = 100
    mp: int = 50
    df: int = 10
    mdf: int = 10
    atk: int = 15
    matk: int = 15
    action_speed: int = 5
    Attack_range: int = 2

    def status(self):
        return "\n".join(f"{attr}: {value}" for attr, value in self.__dict__.items())

# 사용 예제
# 변수 = Character("이름", HP, MP, DF, mDF, atk, matk, speed)
warrior = Character("Hero", 160, 50, 15, 12, 13, 12, 6, 2)
mage = Character("Mage", 80, 120, 8, 15, 8, 20, 3, 4)
ranger = Character("Ranger", 120, 70, 5)
log = Character("Log", 110, 80, 10, 10, 15, 12, )

enemy = Character(name="Enemy", hp=90, matk=30)

print(warrior.status(), "\n")
print(mage.status(), "\n")
print(ranger.status(), "\n")
print(log.status(), "\n")
