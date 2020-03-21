from init import *

# -------------------- START ----- SPRITE ---------------------------------

# all sprites in one group (sprites_group)
sprites_group = pygame.sprite.Group()

# ==================== START ===== ADDING PLAYER SPRITE ===================

player = Player()
sprites_group.add(player)

# ==================== END === ADDING PLAYER SPRITE =======================

# -------------------- END --- SPRITE -------------------------------------

is_running = True
while is_running:

    # -------------------- Setting the FPS ---------------------------------

    clock.tick(FPS)

    # -------------------- Setting the FPS ---------------------------------

    # -------------------- START --- EVENTS --------------------------------

    # group all the events and check them
    for event in pygame.event.get():

        # event (closing the window by pressing the x button)
        if event.type == pygame.QUIT:
            is_running = False

    # -------------------- END ----- EVENTS --------------------------------

    # -------------------- START --- UPDATE --------------------------------

    # update sprites_group (all sprites)
    sprites_group.update()

    # -------------------- END ----- UPDATE --------------------------------

    # -------------------- START --- RENDER --------------------------------

    # init is the module and screen is a variable within
    screen.fill(BLACK)
    # draw sprites_group (all sprites)
    sprites_group.draw(screen)

    # double buffering: draw all then display
    # always AFTER the drawing
    pygame.display.flip()

    # -------------------- END ----- RENDER --------------------------------

pygame.quit()
