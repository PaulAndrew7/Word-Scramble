import pygame

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()  # Create a Clock object to manage FPS
fps = 60

test_rect = pygame.Rect((300, 250, 50, 50))
red_color = (255, 0, 0)

run = True
while run:

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, red_color, test_rect)


    key = pygame.key.get_pressed()
    speed = 5
    if key[pygame.K_a] == True:
        test_rect.move_ip(-speed, 0)
    if key[pygame.K_d] == True:
        test_rect.move_ip(speed, 0)
    if key[pygame.K_s] == True:
        test_rect.move_ip(0, speed)
    if key[pygame.K_w] == True:
        test_rect.move_ip(0, -speed)
    
    test_rect.move_ip(0, 2)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
    clock.tick(fps)
    
pygame.quit()