import pygame
import random
import sys

#swaps between two cells (a and b) in a list
def swap(a, b):
	temp = line_heights[a]
	line_heights[a] = line_heights[b]
	line_heights[b] = temp

#sets the window
screen_width = 1000
screen_height = 400
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bubble Sort")
fps = pygame.time.Clock()

#creating list with random lines height
line_heights = [random.randint(0, screen_height) for i in range(100)]
print line_heights

def gameOver():
	pygame.quit()
	sys.exit()

j = 0
k = 0

while True:

	if k == len(line_heights) - 1 - j:
		k = 0
		j += 1

	if line_heights[k] > line_heights[k+1]:
		swap(k, k+1)

	if j == len(line_heights) - 1:
		break


	#waiting for the exit button to be pressed
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOver()

	#sets the screen background color
	window.fill(pygame.Color(255, 255, 255))

	#draw the lines
	for i in range(0, len(line_heights)):
		if i == k:		
			pygame.draw.rect(window, pygame.Color(255, 0, 0), pygame.Rect(i * 10, screen_height - line_heights[i], 10, line_heights[i]))
		else:
			pygame.draw.rect(window, pygame.Color(0, 0, 0), pygame.Rect(i*10, screen_height - line_heights[i], 10, line_heights[i]))
	
	k+= 1

	pygame.display.set_caption("Bubble Sort | Round: " + str(j) + " | Sort: " + str(k))
	pygame.display.flip()
	fps.tick(24)

