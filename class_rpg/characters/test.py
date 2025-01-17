class Character:
    def __init__(self, name, hp, mp, df, mdf, atk, matk, action_speed):
        for key, value in locals().items():
            if key != "self":
                setattr(self, key, value)

    def status(self):
        return "\n".join(f"{attr}: {value}" for attr, value in self.__dict__.items())

# example
hero = Character(name="hero", hp="150", mp="50", df="18", mdf="8", atk="17", matk="0", 
action_speed="5")
print(hero.status())