"""
Simple test of isometric sprite movement using the mouse. 'Diablo style'.
"""

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_ENEMY = 0.25
ENEMY_COUNT = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Isometric Movement Test"

PLAYER_MOVEMENT_SPEED = 10


class MyGame(arcade.Window):
    """
    Custom Window Class
    """

    def __init__(self):
        """Initializer"""
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None
        self.enemy_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # TODO - do I need to set moust visibility to True or is this the default?

        # Set background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the enemys
        for i in range(ENEMY_COUNT):
            
            # Create the enemy instance
            enemy = arcade.Sprite(":resources:images/enemies/frog.png",
                                 SPRITE_SCALING_ENEMY)

            # Position the enemy
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.enemy_list.append(enemy)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.enemy_list.draw()
        self.player_list.draw()

        # Put the text on the screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        """ Mouse Press """
         
        # Move the center of the player sprite towards the location of the mouse press
        if x > self.player_sprite.center_x and y > self.player_sprite.center_y:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        if x > self.player_sprite.center_x and y < self.player_sprite.center_y:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if x < self.player_sprite.center_x and y < self.player_sprite.center_y: 
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if x < self.player_sprite.center_x and y > self.player_sprite.center_y:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED

    def on_mouse_release(self, x, y, buttons, modifiers):
        """ Move player to mouse release position """

        # Move the player towards the point the mouse was released until they get there
        while x != self.player_sprite.center_x and y != self.player_sprite.center_y:
            if x > self.player_sprite.center_x and y > self.player_sprite.center_y:
                self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
                self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
            if x > self.player_sprite.center_x and y < self.player_sprite.center_y:
                self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
                self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
            if x < self.player_sprite.center_x and y < self.player_sprite.center_y: 
                self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
                self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
            if x < self.player_sprite.center_x and y > self.player_sprite.center_y:
                self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
                self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.enemy_list.update()

        # Generate a list of all sprites that collided with the player
        enemys_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)

        # Loop through each colliding sprite, remove it and add to the score
        for enemy in enemys_hit_list:
            enemy.remove_from_sprite_lists()
            self.score += 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()