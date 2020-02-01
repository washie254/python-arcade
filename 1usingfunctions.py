import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "::Raven's Pine Game::")

def draw_pine_tree(x, y):
    """this function draws pine tree at a specific location"""

    #draw the triangle on top of the trunk
    #we need three x, y  points for the triangle

    arcade.draw_triangle_filled(x + 40, y,
                                x, y - 100,
                                x + 80, y - 100, 
                                arcade.color.DARK_GREEN)
    #draw the trunk 
    arcade.draw_lrtb_rectangle_filled(x+30, x+50,y-100, y-140, arcade.color.DARK_BROWN)