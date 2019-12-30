import pygame
import os
if not os.path.isfile("joindata.txt"):
	file = open('joindata.txt','w')
	file.close

font1 = 'THE_Oegyeinseolmyeongseo.ttf'
WHITE = (255,255,255)
BLACK = (0,0,0)

pad_width = 1024
pad_height = 512

def showObject(x,y,object):
	""" 
	screen에 띄울 이미지를 불러오는 함수이다. 
	"""
	global screen
	screen.blit(object,(x,y))

def exitGame():	
	""" 
	게임을 종료하는 함수이다.
	아이디가 입력된 파일에, 쓴 돈과 월급을 입력한 후 file을 닫으며 마무리한다.
	"""
	file = open(ID +'.txt','w')
	file.write(daymoney + '\n')
	file.write(salaryday + '\n')
	file.write(money + '\n')
	if charactor == man1:
		file.write('man1\n')
	elif charactor == man2:
		file.write('man2\n')
	elif charactor == woman1:
		file.write('woman1\n')
	elif charactor == woman2:
		file.write('woman2\n')
	file.close
	pygame.quit()
	
def addIDPW(ID,PW):
	"""
	id를 만드는 함수로 joindata.txt파일에 id를 저장한다.
	"""
	IDPW=[]
	with open('joindata.txt', 'r') as file:
		for lineContent in file:
			IDPW.append(lineContent.strip('\n').split(','))
	test = False
	for list in IDPW:
		if list[0] == ID:
			test = True
			join()
		
	if test == False:
		file = open('joindata.txt','a')
		file.write(ID + ',' + PW + '\n')
		file.close
		file2 = open(ID + '.txt','w')
		file2.close
		file3 = open(ID + '_moneylist.txt','w')
		file3.close

def logintest(ID,PW):
	"""
	login을 위한 함수로 앞서 id를 만들 때 만들었던 joindata.txt파일을 연 뒤, 
	사용자가 입력하는 id와 txt파일에 입력된 id가 같은지 확인하는 함수이다.
	"""
	IDPW=[]
	with open('joindata.txt', 'r') as file:
		for lineContent in file:
			IDPW.append(lineContent.strip('\n').split(','))
		for list in IDPW:	
			if list[0]!=ID:
				continue
			elif list[0]==ID:
				if list[1]==PW:
					return True
	return False

def writesentence(font,fontsize,sentence,color,x,y):
	"""
	문장을 입력하는 함수로서 font, fontsize, 문장, 색, 위치를 입력받는다.
	"""
	fontObj = pygame.font.Font(font, fontsize)
	textSurfaceObj = fontObj.render(sentence, True, color)
	textRectObj= (x, y)
	screen.blit(textSurfaceObj, textRectObj)
	
def writecenter(font,fontsize,sentence,color,x,y):
	"""
	텍스트를 가운데 정렬하여 출력하는 함수이다.
	입력된 변수x와 y는 텍스트의 가운데 점의 위치에 해당한다.
	"""
	fontObj = pygame.font.Font(font, fontsize)
	textSurfaceObj = fontObj.render(sentence, True, color)
	textRectObj = textSurfaceObj.get_rect();
	textRectObj.center = (x, y)
	screen.blit(textSurfaceObj, textRectObj)

import calendar
from datetime import datetime
import math

def Calc_Calendar(salaryday):
	"""
	월급날로부터 다음월급날이 될 때까지의 남은 일수를 계산해주는 함수로서
	calendar 모듈과 datetime 모듈을 이용한다.
	"""
	today = datetime.today().day
    
	if int(salaryday) < today:
		day_1 = calendar.monthrange(datetime.today().year,datetime.today().month)
		day_11 = int(day_1[1])
		return day_11 - today + int(salaryday)
	elif int(salaryday) > today:
		return abs(today - int(salaryday))
	elif int(salaryday) == today:
		return 1
	
def runGame():
	'''
	게임이 실행되는 메인 화면으로서 이 게임에서 할 수 있는 모든 기능이 담긴 버튼이 위치한다.\
	runGame()함수에서 보여주는 버튼은 먹으러가기, 놀러가기, 공부하기, 잔고관리, 종료, 메뉴시트버튼이다.
	'''
	global screen, clock
	
	listnumber = 0
	crashed = False
	moneylist = []
	file = open(ID + '_moneylist.txt','r')
	for lineContent in file:
		moneylist.append(lineContent.strip('\n').split(','))
	file.close
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if eat_button.get_rect(x=35,y=80).collidepoint(pygame.mouse.get_pos()):
					eat()
				elif play_button.get_rect(x=35,y=155).collidepoint(pygame.mouse.get_pos()):
					play()
				elif study_button.get_rect(x=35,y=230).collidepoint(pygame.mouse.get_pos()):
					study()
				elif endprogram_button.get_rect(x=770,y=425).collidepoint(pygame.mouse.get_pos()):
					crashed = True
				elif money_manage_button.get_rect(x=770,y=350).collidepoint(pygame.mouse.get_pos()):
					usemoney()
				elif right_button.get_rect(x=950,y=50).collidepoint(pygame.mouse.get_pos()):
					if 5 * listnumber <= len(moneylist)-1:
						listnumber += 1
				elif left_button.get_rect(x=750,y=50).collidepoint(pygame.mouse.get_pos()):
					if listnumber != 0:
						listnumber -= 1
			elif event.type == pygame.QUIT:
				exitGame()
		screen.fill(WHITE)
		showObject(0,0,background)		
		showObject(35,80,eat_button)
		showObject(35,155,play_button)
		showObject(35,230,study_button)
		showObject(770,425,endprogram_button)
		showObject(770,350,money_manage_button)
		showObject(400,100,charactor)
		showObject(950,50,right_button)
		showObject(750,50,left_button)
		writecenter(font1,30,ID,BLACK,135,46)
		writesentence(font1,50,'오늘은 뭘 할까??',BLACK,350,30)
		writesentence(font1,40,money,BLACK,30,355)
		writesentence(font1,40,daymoney,BLACK,30,440)
		if moneylist != []:
			if 5 * listnumber < len(moneylist):
				writecenter(font1,30,moneylist[5*listnumber][0]+' : '+moneylist[5*listnumber][1],BLACK,870,115)
			if 5 * listnumber + 1 < len(moneylist):
				writecenter(font1,30,moneylist[5*listnumber+1][0]+' : '+moneylist[5*listnumber+1][1],BLACK,870,155)
			if 5 * listnumber + 2 < len(moneylist):
				writecenter(font1,30,moneylist[5*listnumber+2][0]+' : '+moneylist[5*listnumber+2][1],BLACK,870,195)
			if 5 * listnumber + 3 < len(moneylist):
				writecenter(font1,30,moneylist[5*listnumber+3][0]+' : '+moneylist[5*listnumber+3][1],BLACK,870,235)
			if 5 * listnumber + 4 < len(moneylist):
				writecenter(font1,30,moneylist[5*listnumber+4][0]+' : '+moneylist[5*listnumber+4][1],BLACK,870,275)
		pygame.display.update()
		clock.tick(60)
	exitGame()

def usemoney():
	'''
	잔고관리에 이용되는 함수로서 어디에, 얼마를 사용했는지를 입력받고 id가 저장되어있는 파일에 입력한다.
	'''

	global screen, clock, usewhere, usedmoney, money, daymoney
	
	usedmoney = ""
	usewhere = ""
	typed = False
	while not typed:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					typed = True
				elif event.unicode.isdigit() or event.unicode.isalpha():
					usewhere += event.unicode
				elif event.key == pygame.K_BACKSPACE:
					usewhere = usewhere[:-1]
			elif event.type == pygame.QUIT:
				exitGame()
		screen.fill(WHITE)
		writecenter(font1,50,'어디에 돈 썼지??',BLACK,700,150)
		writecenter(font1,50,usewhere+'에 썼어',BLACK,700,250)
		showObject(200,80,charactor)
		pygame.display.update()
		clock.tick(60)
	typed2 = False
	while not typed2:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					typed2 = True
				elif event.unicode.isdigit():
					usedmoney += event.unicode
				elif event.key == pygame.K_BACKSPACE:
					usedmoney = usedmoney[:-1]
			elif event.type == pygame.QUIT:
				exitGame()
		screen.fill(WHITE)
		writecenter(font1,50,usewhere+ '에 돈 얼마나 썼지??',BLACK,700,150)
		writecenter(font1,50,usedmoney+'원 썼어',BLACK,700,250)
		showObject(200,80,charactor)
		pygame.display.update()
		clock.tick(60)
	file = open(ID + '_moneylist.txt','a')
	file.write(usewhere+','+usedmoney+'\n')
	file.close
	money = str(int(money) - int(usedmoney))
	daymoney = str(int(daymoney) - int(usedmoney))
	runGame()
	

def studyuntil():
	'''
	공부하기 기능에서는 공부할 시간에 따라 적합한 카페 또는 도서관을 추천해주므로 몇시까지 공부할지 시간을 입력받는 함수이다.
	'''
	
	global screen, clock, studyuntiltime
	
	studyuntiltime = ''
	typed = False
	while not typed:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					typed = True
				elif event.unicode.isdigit():
					studyuntiltime += event.unicode
				elif event.key == pygame.K_BACKSPACE:
					studyuntiltime = studyuntiltime[:-1]
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.get_rect(x=900,y=20).collidepoint(pygame.mouse.get_pos()):
					study()
			elif event.type == pygame.QUIT:
				exitGame()
		screen.fill(WHITE)
		writesentence(font1,50,'몇 시까지 공부할까??',BLACK,490,125)
		writesentence(font1,50,studyuntiltime,BLACK,700,300)
		showObject(200,80,charactor)
		showObject(900,20,back_button)
		pygame.display.update()
		clock.tick(60)
		
def foodchoice(country,money):
	'''
	먹으러가기 기능에서 타입(한식,일식 등)을 선택하면 사용자의 잔고상황에 알맞은 메뉴를 csv로 부터 추출한 후 랜덤으로 추천해주는 함수이다.
	'''
	
	fileMatrix = []
	newfood=[]
	newchoicelist=[]
	import random
	with open('hackathon_menu.csv', 'r') as file:
		for lineContent in file: # Point.1
			fileMatrix.append(lineContent.strip('\n').split(',')) # Point.2
	for i in range(1,len(fileMatrix)):
		if fileMatrix[i][0]==country:
			newfood.append(fileMatrix[i])
		else:
			continue
	for i in range(1,len(newfood)):
		if int(newfood[i][3])<int(money):
			newchoicelist.append(newfood[i])
		else:
			continue
	return random.sample(newchoicelist,5)
	
def speak(picture,x,y,line):
	'''
	추천해주는 화면에서 글자 제외 나머지 이미지 모두를 띄우는 함수이다.
	'''
	
	global screen, clock
	
	pressed = False
	while not pressed:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if enter_button.get_rect(x=800,y=400).collidepoint(pygame.mouse.get_pos()):
					pressed = True
			elif event.type == pygame.QUIT:
				exitGame()
		screen.fill(WHITE)
		showObject(x,y,picture)
		showObject(800,400,enter_button)
		showObject(510,100,charactor)	
		writesentence(font1,26,line,BLACK,680,80)
		writesentence(font1,25,money,BLACK,230,740)
		writesentence(font1,25,daymoney,BLACK,730,740)
		pygame.display.update()
		clock.tick(60)

def speakreverse(picture,x,y,line):
	'''
	추천해주는 화면에서 글자 제외 나머지 이미지 모두를 띄우는 함수이다.
	'''
	
	global screen, clock
	
	pressed = False
	while not pressed:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if enter_button.get_rect(x=800,y=400).collidepoint(pygame.mouse.get_pos()):
					pressed = True
			elif event.type == pygame.QUIT:
				exitGame()
		screen.fill(WHITE)
		showObject(x,y,picture)
		showObject(800,400,enter_button)
		showObject(600,100,charactor)
		writesentence(font1,45,line,BLACK,170,100)		
		writesentence(font1,40,money,BLACK,230,740)
		writesentence(font1,40,daymoney,BLACK,730,740)
		pygame.display.update()
		clock.tick(60)
	
def studytime(time):
	'''
	사용자가 입력한 공부 시간에 알맞은 카페를 추천해주는 함수이다.
	카페별 마감시간을 dic으로 준 후, 공부 시간 이후에 마감하는 카페를 추천한다.
	'''
	answer=[] 
	line=""
	values2=[]
	study_place = {'우정원일카':20,'khucafe':21.5,'엔젤리너스':23,'스타벅스':23,'이디야':23,'sweetedu':23,'비엔나':1,'할리스':2,'탐탐':24}
	values = list(study_place.values())
	default = '탐탐'
	recommend_place = []
	answer = []
	for i in range(len(values)):
		if time == 1:
			answer = '할리스,탐탐'
			return answer
		elif 1< time < 8:
			answer = '탐탐'
			return answer
	if 7<time<25:
		a=0
		while values[a]<time:
			a+=1
		values2=values[a:]
    
	for item in study_place:
		if study_place[item] in values2:
			answer.append(item)
	for i in range(len(answer)):
		line+=answer[i]
		line+=','
	return line

def eat():
	'''
	메뉴 타입 선택 후, 랜덤메뉴를 추천해주는 함수이다.
	버튼을 이용해 메뉴타입을 선택한 후, 타입에 알맞은 메뉴를 텍스트형식으로 보일 수 있도록 추천한다.
	메뉴타입 버튼은 한식, 중식, 일식, 양식 총 4가지이다
	'''
	global screen, clock, country
	pressed = False
	country = 0
	while not pressed:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if korea_button.get_rect(x=80,y=150).collidepoint(pygame.mouse.get_pos()):
					country = '한식'
					pressed = True
				elif china_button.get_rect(x=80,y=270).collidepoint(pygame.mouse.get_pos()):
					country = '중식'
					pressed = True
				elif japan_button.get_rect(x=300,y=150).collidepoint(pygame.mouse.get_pos()):
					country = '일식'
					pressed = True
				elif western_button.get_rect(x=300,y=270).collidepoint(pygame.mouse.get_pos()):
					country = '양식'
					pressed = True
				elif back_button.get_rect(x=900,y=20).collidepoint(pygame.mouse.get_pos()):
					runGame()
			elif event.type == pygame.QUIT:
				exitGame()
		screen.fill(WHITE)	
		showObject(80,150,korea_button)
		showObject(80,270,china_button)
		showObject(300,150,japan_button)
		showObject(300,270,western_button)
		showObject(620,100,charactor)	
		showObject(900,20,back_button)
		writesentence(font1,50,'무엇을 먹을까??',BLACK,550,30)
		writesentence(font1,50,money,BLACK,230,740)
		writesentence(font1,50,daymoney,BLACK,730,740)
		pygame.display.update()
		clock.tick(60)
	recommend = foodchoice(country,daymoney)
	line1 = '뭘 먹을지 추천해줄게요'
	line2 = '{}/{}/{}원'.format(recommend[0][1],recommend[0][2],recommend[0][3])
	line3 = '{}/{}/{}원'.format(recommend[1][1],recommend[1][2],recommend[1][3])
	line4 = '{}/{}/{}원'.format(recommend[2][1],recommend[2][2],recommend[2][3])
	line5 = '{}/{}/{}원'.format(recommend[3][1],recommend[3][2],recommend[3][3])
	line6 = '{}/{}/{}원'.format(recommend[4][1],recommend[4][2],recommend[4][3])
	pressed = False
	while not pressed:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if enter_button.get_rect(x=800,y=400).collidepoint(pygame.mouse.get_pos()):
					pressed = True
				elif back_button.get_rect(x=900,y=20).collidepoint(pygame.mouse.get_pos()):
					eat()
			elif event.type == pygame.QUIT:
				exitGame()
		screen.fill(WHITE)
		showObject(800,400,enter_button)
		showObject(10,20,balloon_reverse)
		showObject(600,100,charactor)	
		showObject(900,20,back_button)
		writesentence(font1,24,line1,BLACK,100,55)
		writesentence(font1,24,line2,BLACK,100,105)
		writesentence(font1,24,line3,BLACK,100,155)
		writesentence(font1,24,line4,BLACK,100,205)
		writesentence(font1,24,line5,BLACK,100,255)
		writesentence(font1,24,line6,BLACK,100,305)
		pygame.display.update()
		clock.tick(60)
	runGame()


	
def etccafe():
	'''
	이색카페를 선택하면, 이용시간과 요금 등의 정보를 제공해주는 함수이다.
	이색카페 버튼의 종류에는 룸카페, 만화카페, 보드게임카페, 양궁카페 총 4가지이다.
	각 이색카페에 대한 정보는 이미지로 제공한다.
	'''
	global screen, clock

	pressed = False
	while not pressed:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if roomcafe_button.get_rect(x=80,y=150).collidepoint(pygame.mouse.get_pos()):
					pressed = True
					speak(roomcafe_list,75,20, "룸카페에 가서 놀자!")
				elif comicbook_button.get_rect(x=80,y=270).collidepoint(pygame.mouse.get_pos()):
					pressed = True
					speak(comicbook_list,75,30, "만화카페에 가서 놀자!")
				elif boardgame_button.get_rect(x=300,y=150).collidepoint(pygame.mouse.get_pos()):
					pressed = True
					speak(boardgame_list,50,100, "보드게임카페에 가서 놀자!")
				elif bowcafe_button.get_rect(x=300,y=270).collidepoint(pygame.mouse.get_pos()):
					pressed = True
					speak(bowcafe_list,50,100, "양궁카페에 가서 놀자!")
				elif back_button.get_rect(x=900,y=20).collidepoint(pygame.mouse.get_pos()):
					play()
			elif event.type == pygame.QUIT:
				exitGame()
			
		screen.fill(WHITE)	
		showObject(80,150,roomcafe_button)
		showObject(80,270,comicbook_button)
		showObject(300,150,boardgame_button)
		showObject(300,270,bowcafe_button)
		showObject(900,20,back_button)
		showObject(620,100,charactor)	
		writesentence(font1,50,'무슨 카페 갈까??',BLACK,550,30)
		writesentence(font1,50,money,BLACK,230,740)
		writesentence(font1,50,daymoney,BLACK,730,740)
		pygame.display.update()
		clock.tick(60)
	
def play():
	'''
	기본 화면(runGame 함수의 실행 화면)에서 놀러가기를 클릭하였을 때 4개의 버튼을 보여주고 버튼마다 추천하는 장소에 관한 정보를 제공한다.
	play() 함수에서 보여주는 4개의 버튼은 pc방, 노래방, 당구장, 이색카페에 해당한다.
	'''
   
	global screen, clock
	pressed = False
	while not pressed:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if pcroom_button.get_rect(x=80,y=150).collidepoint(pygame.mouse.get_pos()):
					pressed = True
					speak(pcroom_list,50,100, "pc방에 가서 놀자!")
				elif singroom_button.get_rect(x=80,y=270).collidepoint(pygame.mouse.get_pos()):
					pressed = True
					speak(singroom_list,50,100, "노래방에 가서 놀자!")
				elif danggu_button.get_rect(x=300,y=150).collidepoint(pygame.mouse.get_pos()):
					pressed = True
					speak(danggu_list,130,30, "당구장에 가서 놀자!")
				elif etccafe_button.get_rect(x=300,y=270).collidepoint(pygame.mouse.get_pos()):
					etccafe()
					pressed = True
				elif back_button.get_rect(x=900,y=20).collidepoint(pygame.mouse.get_pos()):
					runGame()
			elif event.type == pygame.QUIT:
				exitGame()
				
		screen.fill(WHITE)	
		showObject(80,150,pcroom_button)
		showObject(80,270,singroom_button)
		showObject(300,150,danggu_button)
		showObject(300,270,etccafe_button)
		showObject(620,100,charactor)	
		showObject(900,20,back_button)
		writesentence(font1,50,'뭐하고 놀까??',BLACK,550,30)
		writesentence(font1,50,money,BLACK,230,740)
		writesentence(font1,50,daymoney,BLACK,730,740)
		pygame.display.update()
		clock.tick(60)
	runGame()
	

def study():
	'''
	공부할 곳을 선택하는 함수이다.
	공부할 장소는 도서관, 카페 두가지의 버튼이 해당된다.
	도서관을 선택했을 시, 열람실 별 이용시간 정보가 제공된다.
	카페를 선택했을 경우, studycafe()함수를 실행한다.
	'''
	global screen, clock
	pressed = False
	while not pressed:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if library_button.get_rect(x=50,y=210).collidepoint(pygame.mouse.get_pos()):
					pressed = True
					speak(library_list,50,100, "도서관에 가면 아껴쓸 수 있어!")
				elif cafe_button.get_rect(x=270,y=210).collidepoint(pygame.mouse.get_pos()):
					studycafe()
					pressed = True
				elif back_button.get_rect(x=900,y=20).collidepoint(pygame.mouse.get_pos()):
					runGame()
			elif event.type == pygame.QUIT:
				exitGame()
			
		screen.fill(WHITE)	
		showObject(50,210,library_button)
		showObject(270,210,cafe_button)
		showObject(580,100,charactor)
		showObject(900,20,back_button)
		writesentence(font1,50,"어디서 공부할까?",BLACK,510,30)
		writesentence(font1,50,money,BLACK,230,740)
		writesentence(font1,50,daymoney,BLACK,730,740)
		pygame.display.update()
		clock.tick(60)
	runGame()
	
def studycafe():
	'''
	카페를 선택한 이용자에게 studytime에 따른 함수를 추천하기 위한 화면을 띄우는 함수이다.
	'''
	studyuntil()
	line = studytime(int(studyuntiltime))
	pressed = False
	while not pressed:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if enter_button.get_rect(x=800,y=400).collidepoint(pygame.mouse.get_pos()):
					pressed = True
			elif event.type == pygame.QUIT:
				exitGame()
		screen.fill(WHITE)
		showObject(800,400,enter_button)
		showObject(430,100,charactor)	
		writecenter(font1,26,line,BLACK,512,40)
		pygame.display.update()
		clock.tick(60)
	runGame()	
	
def getInformationSalaryday():
	'''
	월급/용돈날을 입력받는 함수이다.
	입력받은 내용은 ID가 입력되어있는 파일에 입력된다.
	'''
	global screen, clock, salaryday, daymoney
	
	file = open(ID + '.txt','a')
	salaryday = ""
	typed = False
	while not typed:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					typed = True
				elif event.unicode.isdigit():
					salaryday += event.unicode
				elif event.key == pygame.K_BACKSPACE:
					salaryday = salaryday[:-1]
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.get_rect(x=900,y=20).collidepoint(pygame.mouse.get_pos()):
					getInformationMoney()
			elif event.type == pygame.QUIT:
				exitGame()
		screen.fill(WHITE)
		writecenter(font1,50,'월급/용돈날을 입력하고 enter하세요',BLACK,512,100)
		writesentence(font1,50,money + '원',BLACK,500,200)
		writesentence(font1,50,salaryday + '일',BLACK,500,300)
		showObject(200,200,charactor_circle)
		showObject(900,20,back_button)
		pygame.display.update()
		clock.tick(60)
	daymoney = str(int(int(money)/Calc_Calendar(salaryday)))
	file.write(daymoney + '\n')
	file.write(salaryday + '\n')
	file.close
	runGame()

def getInformationMoney():
	'''
	월급/용돈을 입력받는 함수이다.
	정보는 id가 입력된 파일에 저장된다.
	'''
	
	global screen, clock, money
	
	file = open(ID + '.txt','a')
	money = ""
	typed = False
	while not typed:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					file.write(money + '\n')
					typed = True
				elif event.unicode.isdigit():
					money += event.unicode
				elif event.key == pygame.K_BACKSPACE:
					money = money[:-1]
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.get_rect(x=900,y=20).collidepoint(pygame.mouse.get_pos()):
					selectCharactor()
			elif event.type == pygame.QUIT:
				exitGame()
		screen.fill(WHITE)
		writecenter(font1,50,'현재 가진 잔액을 입력하고 enter하세요',BLACK,512,100)
		writesentence(font1,50,money + '원',BLACK,500,200)
		showObject(200,200,charactor_circle)
		showObject(900,20,back_button)
		pygame.display.update()
		clock.tick(60)
	file.close
	getInformationSalaryday()
	
def selectCharactor():
	'''
	게임에서 사용할 캐릭터를 선택하는 함수이다.
	캐릭터는 총 네가지로 남성캐릭터 2종, 여성캐릭터 2종으로 이루어져있다.
	캐릭터 선택 화면에서는 외모만 보이는 이미지를 보여주며, 메인 runGame()함수에서는 전신이미지를 사용한다.
	'''
	global screen, clock, charactor, charactor_circle
	
	file = open(ID + '.txt','a')
	selected = False
	while not selected:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if man1_circle.get_rect(x=100,y=200).collidepoint(pygame.mouse.get_pos()):
					charactor = man1
					charactor_circle = man1_circle
					file.write('man1\n')
					selected = True
				elif man2_circle.get_rect(x=305,y=200).collidepoint(pygame.mouse.get_pos()):
					charactor = man2
					charactor_circle = man2_circle
					file.write('man2\n')
					selected = True
				elif woman1_circle.get_rect(x=510,y=200).collidepoint(pygame.mouse.get_pos()):
					charactor = woman1
					charactor_circle = woman1_circle
					file.write('woman1\n')
					selected = True
				elif woman2_circle.get_rect(x=715,y=200).collidepoint(pygame.mouse.get_pos()):
					charactor = woman2
					charactor_circle = woman2_circle
					file.write('woman2\n')
					selected = True
				elif back_button.get_rect(x=900,y=20).collidepoint(pygame.mouse.get_pos()):
					startGame()
			elif event.type == pygame.QUIT:
				exitGame()
		screen.fill(WHITE)
		writecenter(font1,50,'캐릭터 선택',BLACK,500,120)
		showObject(100,200,man1_circle)
		showObject(305,200,man2_circle)
		showObject(510,200,woman1_circle)
		showObject(715,200,woman2_circle)
		showObject(900,20,back_button)
		pygame.display.update()
		clock.tick(60)
	file.close
	getInformationMoney()
	
def login():
	global screen, clock, ID, PW, money, salaryday, charactor, daymoney
	cursortime = 0
	ID = ""
	PW = ""
	typedID = False
	while not typedID:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					typedID = True
				elif event.unicode.isalpha():
					ID += event.unicode
				elif event.key == pygame.K_BACKSPACE:
					ID = ID[:-1]
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.get_rect(x=900,y=20).collidepoint(pygame.mouse.get_pos()):
					startGame()
			elif event.type == pygame.QUIT:
				exitGame()
		screen.fill(WHITE)
		showObject(0,0,login_screen)
		showObject(900,20,back_button)
		if 0 <= cursortime and cursortime <= 20:
			cursortime += 1
			cursor = "|"
		elif cursortime == 40:
			cursortime = 0
		else:
			cursortime += 1
			cursor = ""
		writesentence(font1,40,'ID : '+ ID + cursor,BLACK,335,175)
		pygame.display.update()
		clock.tick(60)
	typedPW = False
	while not typedPW:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					typedPW = True
				elif event.unicode.isdigit():
					PW += event.unicode
				elif event.key == pygame.K_BACKSPACE:
					PW = PW[:-1]
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.get_rect(x=900,y=20).collidepoint(pygame.mouse.get_pos()):
					startGame()
			elif event.type == pygame.QUIT:
				exitGame()
		screen.fill(WHITE)
		showObject(0,0,login_screen)
		showObject(900,20,back_button)
		if 0 <= cursortime and cursortime <= 20:
			cursortime += 1
			cursor = "|"
		elif cursortime == 40:
			cursortime = 0
		else:
			cursortime += 1
			cursor = ""
		writesentence(font1,40,'ID : '+ ID,BLACK,335,175)
		writesentence(font1,40,'PW : '+PW+cursor,BLACK,335,253)
		pygame.display.update()
		clock.tick(60)
	if logintest(ID,PW) == True:
		DSMC = []
		file = open(ID+'.txt','r')
		for lineContent in file:
			DSMC.append(lineContent.strip('\n').split(','))
		file.close
		if str(DSMC[3][0]) == 'man1':
			charactor = man1
		elif str(DSMC[3][0]) == 'man2':
			charactor = man2
		elif str(DSMC[3][0]) == 'woman1':
			charactor = woman1
		elif str(DSMC[3][0]) == 'woman2':
			charactor = woman2
		money = str(DSMC[2][0])
		salaryday = str(DSMC[1][0])
		if DSMC[0][0] == '':
			daymoney = str(int(int(money)/Calc_Calendar(salaryday)))
		else:
			daymoney = DSMC[0][0]
		runGame()
	elif logintest(ID,PW) == False:
		login()

def join():
	global screen, clock, ID, PW
	cursortime = 0
	ID = ""
	PW = ""
	typedID = False
	while not typedID:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					typedID = True
				elif event.unicode.isalpha():
					ID += event.unicode
				elif event.key == pygame.K_BACKSPACE:
					ID = ID[:-1]
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.get_rect(x=900,y=20).collidepoint(pygame.mouse.get_pos()):
					startGame()
			elif event.type == pygame.QUIT:
				exitGame()
		screen.fill(WHITE)
		showObject(0,0,join_screen)
		showObject(900,20,back_button)
		if 0 <= cursortime and cursortime <= 20:
			cursortime += 1
			cursor = "|"
		elif cursortime == 40:
			cursortime = 0
		else:
			cursortime += 1
			cursor = ""
		writesentence(font1,40,'ID : ' + ID + cursor,BLACK,335,160)
		pygame.display.update()
		clock.tick(60)
	typedPW = False
	while not typedPW:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					typedPW = True
				elif event.unicode.isdigit():
					PW += event.unicode
				elif event.key == pygame.K_BACKSPACE:
					PW = PW[:-1]
			elif event.type == pygame.QUIT:
				exitGame()
		screen.fill(WHITE)
		showObject(0,0,join_screen)
		writesentence(font1,40,'ID : ' + ID,BLACK,335,160)
		if 0 <= cursortime and cursortime <= 20:
			cursortime += 1
			cursor = "|"
		elif cursortime == 40:
			cursortime = 0
		else:
			cursortime += 1
			cursor = ""
		writesentence(font1,40,'PW : '+PW+cursor,BLACK,335,245)
		pygame.display.update()
		clock.tick(60)
	addIDPW(ID,PW)
	selectCharactor()
	

	
def startGame():
	global screen, clock
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if login_button.get_rect(x=800,y=380).collidepoint(pygame.mouse.get_pos()):
					login()
					break
				elif join_button.get_rect(x=800,y=300).collidepoint(pygame.mouse.get_pos()):
					join()
					break
			elif event.type == pygame.QUIT:
				exitGame()

		screen.fill(WHITE)
		showObject(0,0,start_screen)
		showObject(800,380,login_button)
		showObject(800,300,join_button)
		pygame.display.update()
		clock.tick(60)
	
def initGame():
	'''
	프로그램에서 사용하고자 하는 이미지들을 모두 불러온다.
	'''
	global screen, clock, start_screen, background, join_screen, login_screen
	global eat_button, play_button, study_button, endprogram_button, enter_button
	global korea_button, china_button, western_button, japan_button
	global pcroom_button, singroom_button, danggu_button, etccafe_button
	global roomcafe_button, comicbook_button, boardgame_button, bowcafe_button
	global library_button, cafe_button, balloon, balloon_reverse
	global pcroom_list, singroom_list, danggu_list, library_list
	global roomcafe_list,comicbook_list, boardgame_list, bowcafe_list
	global back_button, join_button, login_button
	global man1, man2, woman1, woman2,right_button,left_button,money_manage_button
	global man1_circle, man2_circle, woman1_circle, woman2_circle
	
	pygame.init()
	screen = pygame.display.set_mode((pad_width,pad_height))
	pygame.display.set_caption('small_but_sure_happiness')
	start_screen = pygame.image.load('start_screen.png')
	background = pygame.image.load('background.png')
	join_screen = pygame.image.load('join_screen.png')
	login_screen = pygame.image.load('login_screen.png')
	eat_button = pygame.image.load('eat_button.png')
	play_button = pygame.image.load('play_button.png')
	study_button = pygame.image.load('study_button.png')
	endprogram_button = pygame.image.load('endprogram_button.png')
	enter_button = pygame.image.load('enter_button.png')
	korea_button = pygame.image.load('korea_button.png')
	china_button = pygame.image.load('china_button.png')
	western_button = pygame.image.load('western_button.png')
	japan_button = pygame.image.load('japan_button.png')
	pcroom_button = pygame.image.load('pcroom_button.png')
	singroom_button = pygame.image.load('singroom_button.png')
	danggu_button = pygame.image.load('danggu_button.png')
	etccafe_button = pygame.image.load('etccafe_button.png')
	roomcafe_button = pygame.image.load('roomcafe_button.png')
	comicbook_button = pygame.image.load('comicbook_button.png')
	boardgame_button = pygame.image.load('boardgame_button.png')
	bowcafe_button = pygame.image.load('bowcafe_button.png')
	library_button = pygame.image.load('library_button.png')
	cafe_button = pygame.image.load('cafe_button.png')
	balloon = pygame.image.load('balloon.png')
	balloon_reverse = pygame.image.load('balloon_reverse.png')
	pcroom_list = pygame.transform.scale(pygame.image.load('pcroom_list.png'),(400,300))
	singroom_list = pygame.transform.scale(pygame.image.load('singroom_list.png'),(400,300))
	danggu_list = pygame.image.load('danggu_list.png')
	library_list = pygame.image.load('library_list.png')
	roomcafe_list = pygame.image.load('roomcafe_list.png')
	comicbook_list = pygame.image.load('comicbook_list.png')
	boardgame_list = pygame.image.load('boardgame_list.png')
	bowcafe_list = pygame.image.load('bowcafe_list.png')
	back_button = pygame.image.load('back_button.png')
	join_button= pygame.image.load('join_button.png')
	login_button = pygame.image.load('login_button.png')
	man1 = pygame.image.load('char_man_stand1.png')
	man2 = pygame.image.load('char_man_stand2.png')
	woman1 = pygame.image.load('char_woman_stand1.png')
	woman2 = pygame.image.load('char_woman_stand2.png')
	man1_circle = pygame.image.load('char_man_circle1.png')
	man2_circle = pygame.image.load('char_man_circle2.png')
	woman1_circle = pygame.image.load('char_woman_circle1.png')
	woman2_circle = pygame.image.load('char_woman_circle2.png')
	right_button=pygame.image.load('right_button.png')
	left_button=pygame.image.load('left_button.png')
	money_manage_button=pygame.image.load('money_manage_button.png')
	
	clock = pygame.time.Clock()
	startGame()

initGame()