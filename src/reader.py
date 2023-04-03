# pip install pyserial 
import serial
import re
import pygame
import random

inside = 0

def trapped(r_pos, r_dim, p_pos):
	global inside
	x = p_pos[0]
	y = p_pos[1]
	left = r_pos[0]
	right = r_pos[0]+r_dim[0]
	top = r_pos[1]
	bottom = r_pos[1] + r_dim[1]
	if ((x > left and x < right and y > top and y < bottom) or inside):
		if x < left: #to the left
			x = left
		if y < top: #above
			y = top
		if x > right: #to the right
			x = right
		if y > bottom: #below
			y = bottom
		inside = 1
	
	return (x,y)

def main():
	
	global inside

	#set serial input port
	ser = serial.Serial('/dev/cu.usbserial-546F1153241', 115200)
		
	# initialize the game
	pygame.init()
	pygame.display.set_caption("Steal the Color")
	screen = pygame.display.set_mode((800,600))
	clock = pygame.time.Clock()
		
	#initialize the color and rectangle
	color = "green"
	rect_pos = (100,100)
	rect_dim = (200,150)
	rect_color = "black"

	running = True

	while(running):


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		#retrieve serial input	
		ser_str = str(ser.readline().strip(), 'ascii')
		ser_vals = list(map(int, re.findall('\d+', ser_str)))
		
		#player position determined by joystick:
		player_pos = pygame.Vector2(ser_vals[0]*10/50,ser_vals[1]*7.5/50)
		screen.fill("black")

		#if joystick is not being pressed and inside_rect, trapped
		#if button is being pressed, not trapped
		if(ser_vals[2]==1 and ser_vals[3]==1):
			player_pos = trapped(rect_pos, rect_dim, player_pos)


		#if joystick pressed when inside square, change color and break out
		#if button being pressed, can change color anytime
		if ((ser_vals[2] == 0 and inside) or ser_vals[3]==0):
			color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
			rect_pos = (random.randint(0,800), random.randint(0,600))
			inside = 0

		rect = (rect_pos, rect_dim)
		pygame.draw.rect(screen, rect_color, rect)
		pygame.draw.circle(screen, color, player_pos, 40)

		pygame.display.flip()

		clock.tick(60)

if __name__ == "__main__":
	main()