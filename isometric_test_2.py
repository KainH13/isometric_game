"""
Simple program to show basic sprite usage.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_angle
"""
import arcade
import os
import math
import time

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move Sprite by Angle Example"

MOVEMENT_SPEED = 5
ANGLE_SPEED = 5


class Player(arcade.Sprite):
    """ Player class """

    def __init__(self, image, scale):
        """ Set up the player """

        # Call the parent init
        super().__init__(image, scale)

        # Create a variable to hold our speed. 'angle' is created by the parent
        self.speed = 0

    def update(self):
        # Convert angle in degrees to radians.
        angle_rad = math.radians(self.angle)

        # Rotate the ship
        self.angle += self.change_angle

        # Use math to find our change based on our speed and angle
        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)
        # print("sprite_x: {0:5f}".format(self.center_x))


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None

        # Set up the player info
        self.player_sprite = None

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Player(":resources:images/space_shooter/playerShip1_orange.png", SPRITE_SCALING)
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_list.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # Forward/back
        if key == arcade.key.UP:
            self.player_sprite.speed = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.speed = -MOVEMENT_SPEED

        # Rotate left/right
        elif key == arcade.key.LEFT:
            self.player_sprite.change_angle = ANGLE_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_angle = -ANGLE_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.speed = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_angle = 0

    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        if button == 1:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y
            # Find mouse angle and turn ship to face mouse
            delta_x = x - self.player_sprite.center_x
            delta_y = y - self.player_sprite.center_y
            angle = math.atan2(delta_x, delta_y)
            print("radian angle: {:.2f}".format(angle))
            degreeAngle = math.degrees(angle)*-1
            print("degree angle: {:.2f}".format(degreeAngle))
            self.player_sprite.angle = degreeAngle
            print("x: {0:5d}, sprite_x.position: {0:5d}".format(x, self.player_sprite.position))
            self.player_sprite.speed = MOVEMENT_SPEED
            
    def on_mouse_release(self, x, y, dx, dy):
        # Find mouse angle and turn ship to face mouse
        delta_x = x - self.player_sprite.center_x
        delta_y = y - self.player_sprite.center_y
        angle = math.atan2(delta_x, delta_y)
        print("radian angle: {:.2f}".format(angle))
        degreeAngle = math.degrees(angle)*-1
        print("degree angle: {:.2f}".format(degreeAngle))
        self.player_sprite.angle = degreeAngle
        print("x: {0:5d}, sprite_x.position: {0:5d}".format(x, self.player_sprite.position))
        self.player_sprite.speed = MOVEMENT_SPEED
       
        # self.player_sprite.center_x = x
        # self.player_sprite.center_y = y

        # Move ship
        # self.player_sprite.change_x = math.cos(angle) * -MOVEMENT_SPEED
        # self.player_sprite.change_y = math.sin(angle) * MOVEMENT_SPEED
        # while (self.player_sprite.center_x < x):
        #     self.player_sprite.speed = MOVEMENT_SPEED
        #     print("x: {0:5d}, sprite_x: {0:5d}".format(x, self.player_sprite.center_x))
        #     time.sleep(3)
        # self.player_sprite.change_y = math.sin(angle) * MOVEMENT_SPEED
        # length_delta = math.sqrt((delta_x**2) + (delta_y**2))
        # angle_delta = math.asin(delta_x / length_delta)
        # self.player_sprite.speed = 0




        # while angle_delta != 0:
        #     if angle_delta > 0:
        #         self.player_sprite.change_angle = ANGLE_SPEED
        #     elif angle_delta < 0:
        #         self.player_sprite.change_angle = -ANGLE_SPEED
        #     delta_x = x - self.player_sprite.center_x
        #     delta_y = y - self.player_sprite.center_y
        #     length_delta = math.sqrt((delta_x**2) + (delta_y**2))
        #     angle_delta = math.asin(delta_x / length_delta)
        #     print(angle_delta)

        # self.player_sprite.change_angle = 0



        # if angle_delta > 0.2:
        #     self.player_sprite.change_angle = ANGLE_SPEED
        # elif angle_delta < -0.2:
        #     self.player_sprite.change_angle = -ANGLE_SPEED
        # else:
        #     self.player_sprite.change_angle = 0

            
        # self.player_sprite.center_y = y
        # self.player_sprite.center_x = x

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()