import gameclass as gameclass
import mainmenu as mainmenu


f = open('level.txt', 'w')
f.write('0')
f.close()
f = open('difficulty.txt', 'w')
f.write("easy")
f.close()
mainmenu.MainMenu()

