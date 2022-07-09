import random


def myfunc():
	secret = random.randint(1, 100)
	answer = 0
	while answer != secret:
		answer = int(input("Какое твое число? "))
		if answer == secret:
			print("Поздравляю ты победил!")
		elif answer > secret:
			print("Попробуй ввести число меньше")
		elif answer < secret:
			print("Попробуй ввести число больше")
	if input("Хочешь сыграть снова? y/n ") == "y":
		myfunc()

myfunc()
