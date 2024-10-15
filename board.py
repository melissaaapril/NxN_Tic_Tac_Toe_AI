import pygame

# initialize pygame
pygame.init()

# screen
screen = pygame.display.set_mode((1000, 900))
running = True
n = 3
white = (255,255,255)

# grid function
def grid(size, colors):
    color = colors
    gridSizeRange = size-1
    offset = size * 100
    
    if size == 3: 
        xStartV = 450
        yStartV = 450
        xStartH = 350
        yStartH = 550
        
        for i in range(gridSizeRange):
            pygame.draw.line(screen, color, (xStartV, yStartV), (xStartV, yStartV+offset), 3)
            pygame.draw.line(screen, color, (xStartH, yStartH), (xStartH+offset, yStartH), 3)
            xStartV += 100
            yStartH += 100
            
    elif size == 4: 
        xStartV = 400
        yStartV = 400
        xStartH = 300
        yStartH = 500
        
        for i in range(gridSizeRange):
            pygame.draw.line(screen, color, (xStartV, yStartV), (xStartV, yStartV+offset), 3)
            pygame.draw.line(screen, color, (xStartH, yStartH), (xStartH+offset, yStartH), 3)
            xStartV += 100
            yStartH += 100
            
    elif size == 5: 
        xStartV = 350
        yStartV = 350
        xStartH = 250
        yStartH = 450
        
        for i in range(gridSizeRange):
            pygame.draw.line(screen, color, (xStartV, yStartV), (xStartV, yStartV+offset), 3)
            pygame.draw.line(screen, color, (xStartH, yStartH), (xStartH+offset, yStartH), 3)
            xStartV += 100
            yStartH += 100
        
# text function
def generateText(text, colors, fontSize):
    font = pygame.font.Font(None, fontSize)
    global text_surface
    text_surface = font.render(text, True, colors)

# draw start button
def startButton(colors):
    color = (colors)
    
# Generates Select Opponent
    generateText("Select Opponent", white, 20)
    pygame.draw.rect(screen, color, (124, 45, 250, 100), width=3)
    screen.blit(text_surface, (195, 59))
    # You v Comp radio
    pygame.draw.circle(screen, color, (195, 89), 8, 3)
    generateText("You vs. Computer", white, 16)
    screen.blit(text_surface, (215, 84))
    # P v P radio
    pygame.draw.circle(screen, color, (195, 119), 8, 3)
    generateText("You vs. Person", white, 16)
    screen.blit(text_surface, (215, 115))
    
# Generate Select X or O
    generateText("Select X or O", white, 20)
    pygame.draw.rect(screen, color, (124, 166, 250, 100), width=3)
    screen.blit(text_surface, (205, 183))
    # Select X radio
    pygame.draw.circle(screen, color, (195, 213), 8, 3)
    generateText("Select X", white, 16)
    screen.blit(text_surface, (215, 208))
    # Select O radio
    pygame.draw.circle(screen, color, (195, 243), 8, 3)
    generateText("Select O", white, 16)
    screen.blit(text_surface, (215, 238))
    
# Generate Grid Size
    generateText("Select Grid Size", white, 20)
    pygame.draw.rect(screen, color, (625, 45, 250, 100), width=3)
    screen.blit(text_surface, (700, 59))
    # Select 3x3 radio
    pygame.draw.circle(screen, color, (700, 89), 8, 3)
    generateText("3 x 3", white, 16)
    screen.blit(text_surface, (720, 85))
    # Select 4x4 radio
    pygame.draw.circle(screen, color, (775, 89), 8, 3)
    generateText("4 x 4", white, 16)
    screen.blit(text_surface, (795, 85))
    # Select 5x5 radio
    pygame.draw.circle(screen, color, (700, 119), 8, 3)
    generateText("5 x 5", white, 16)
    screen.blit(text_surface, (720, 114))

# Generate START Button  
    generateText("START", white, 24)
    pygame.draw.rect(screen, color, (625, 166, 250, 100), width=3)
    screen.blit(text_surface,(725, 205))
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    startButton(white)
    grid(n, white)
    #makeGrid()
    pygame.display.update()