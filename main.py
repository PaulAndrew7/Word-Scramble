import pygame
import pygame_gui
import random

pygame.init()

# Set up display
WINDOW_SIZE = (600, 400)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Word Scramble Game")

# Set up the clock
clock = pygame.time.Clock()
fps = 60

# Load custom theme
manager = pygame_gui.UIManager(WINDOW_SIZE, theme_path="theme.json")

show_time = pygame.time.get_ticks()

# Create GUI elements
text_input = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((200, 150), (200, 50)),  # Position and size
    manager=manager
)

submit_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((250, 220), (100, 40)),  # Position and size
    text="Submit",
    manager=manager
)

popup_panel = pygame_gui.elements.UIPanel(
    relative_rect=pygame.Rect((200, 150), (200, 100)),
    manager=manager,
    visible=False
)

# Create a label within the popup:
popup_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((0, 25), (200, 50)),
    text="You Win!",
    manager=manager,
    container=popup_panel
)

try_again_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((250, 270), (100, 30)),  # Position and size
        text="Try again!",
        manager=manager,  # Anchor to the submit button
        visible=False  # Initially hidden
    )


words = ['python', 'pygame', 'scrambled', 'game']
guessed = False
word_to_guess = random.choice(words)
word = [x for x in word_to_guess]
print(word)
random.shuffle(word)
print(word)
jumbled_word = ' '.join(word).rstrip()
word = ''.join(word)

label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((150, 75), (300, 50)),  # Position and size
    text=jumbled_word,
    manager=manager
)



# Run the game loop
running = True
while running:
    time_delta = clock.tick(fps) / 1000.0  # Time between frames in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Pass events to the GUI manager
        manager.process_events(event)

        # Handle button click
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == submit_button:
                user_text = text_input.get_text()
                if user_text.lstrip().rstrip() == word_to_guess:
                    print("You Win!")
                    popup_panel.show()
                    text_input.hide()
                    submit_button.hide()
                    label.hide()
                else:
                    print("Try again!")
                    try_again_label.show()
                    show_time = pygame.time.get_ticks()

    if pygame.time.get_ticks() - show_time >= 2000:  # 1000 ms = 1 second
        try_again_label.hide()



    
    # Update the GUI manager
    manager.update(time_delta)

    # Clear the screen
    screen.fill((30, 30, 30))

    # Draw the GUI
    manager.draw_ui(screen)

    # Update the display
    pygame.display.flip()

pygame.quit()
