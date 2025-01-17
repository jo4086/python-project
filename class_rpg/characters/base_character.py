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

    def status(self):
        return "\n".join(f"{attr}: {value}" for attr, value in self.__dict__.items())

# 사용 예제
hero = Character("Hero", 120, 60, 15, 12, 20, 25, 7)
enemy = Character(name="Enemy", hp=90, matk=30)

print(hero.status())
print(enemy.status())