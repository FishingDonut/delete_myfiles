import os

melon = input("■■■■🍖 :") + '/'

os.chdir(melon)

homer = os.listdir()

mw = []
mwd = []

for home in homer:
    mw.append(home)


for egg in mw:
    if os.path.isdir(egg):
        mwd.append(egg)

for vinte in mwd:
    os.rmdir(vinte)

print(os.listdir())

#fishingdonut
