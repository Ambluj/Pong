import random

def impossibleAI(paddle2YPos, ballYPos, paddleHeight, ballHeight):

	if paddle2YPos + paddleHeight/2 < ballYPos + ballHeight/2:
		action = "DIRECTION_DOWN"

	if paddle2YPos + paddleHeight/2 > ballYPos + ballHeight/2:
		action = "DIRECTION_UP"

	return action

def normalAI(paddle2YPos, ballYPos, paddleHeight, ballHeight, previousAction):

	choose = random.randint(1, 25)
	choice = random.randint(1, 8)
	if choose <= 18: #Will only make choice ~70% of the time
		
		if choice <= 7: #Choice will be correct 7/8 of the time

			if paddle2YPos + paddleHeight/2 < ballYPos + ballHeight/2:
				action = "DIRECTION_DOWN"

			if paddle2YPos + paddleHeight/2 > ballYPos + ballHeight/2:
				action = "DIRECTION_UP"
		else: #Incorrect choice
			if paddle2YPos + paddleHeight/2 < ballYPos + ballHeight/2:
				action = "DIRECTION_UP"

			if paddle2YPos + paddleHeight/2 > ballYPos + ballHeight/2:
				action = "DIRECTION_DOWN"

	else:
		action = previousAction

	return action

def easyAI(paddle2YPos, ballYPos, paddleHeight, ballHeight, previousAction):

	choose = random.randint(1, 25)
	choice = random.randint(1, 10)
	if choose > 13: #Will only make choice 1/2 of the time
		
		if choice <= 4: #Choice will be correct 40% of the time

			if paddle2YPos + paddleHeight/2 < ballYPos + ballHeight/2:
				action = "DIRECTION_DOWN"

			if paddle2YPos + paddleHeight/2 > ballYPos + ballHeight/2:
				action = "DIRECTION_UP"
		else: #Incorrect choice
			if paddle2YPos + paddleHeight/2 < ballYPos + ballHeight/2:
				action = "DIRECTION_UP"

			if paddle2YPos + paddleHeight/2 > ballYPos + ballHeight/2:
				action = "DIRECTION_DOWN"

	else:
		action = previousAction

	return action
