# Python-Module-pygame

## First check out the flowing

[Game flow](flow.md) and [pygame rect](rect_pygame.md)

## Road map

- Creating frame for the game

  - [Colors Module](colors.py)

  - [Config Module](config.py)

  - [Initialize Module](init.py)

  - [Player (sprite) Module](Player.py)

  - [The main Module](main.py)

- Replacing the player sprite (rectangular shape) with an image

## The game divided into different modules for ease of use and debugging

- [Colors Module](colors.py)
  - defining some `RGB colors` to use in the game (we can add more colors here)

- [Config Module](config.py)
  - defining screen width and height and also the `FPS`

- [Initialize Module](init.py)
  - initializing the `pygame module`, `pygame mixer` (used for sounds), `the screen` (width and height imported from config module), `screen label` and the `clock` (used to control the time of the game flow) See: [Game flow](flow.md)

- [Player (sprite) Module](Player.py)
  - contains `player` (sprite) class and for now it is a rectangular shape (pygame.Surfaces())

- [The main Module](main.py)
  - the main loop of the game and contains the all the steps of the `game flow` See: [Game flow](flow.md)
