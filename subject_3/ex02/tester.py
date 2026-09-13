from DiamondTrap import King


Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blues")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
print(King.__mro__)
