f = open('level.txt', 'r')
a = f.read()
level_now = int(a) + 1
f.close()

f = open('level.txt', 'w')
f.write(str(level_now))
print(level_now)
f.close()
