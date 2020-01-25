import arcade

#set constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#Open the window, set the title and dimentions (width aand height )
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,"Drawing example")

#set background color to white
#(r,g,b,a)
#or direct naming 
arcade.set_background_color(arcade.color.WHITE)

#start the render process. this must be done before any drawing command 
arcade.start_render()

#draw the face
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x,y,radius,arcade.color.YELLOW)

#draw the right eye
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

#draw the left eye 
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

#draw the smile 
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

#finish the drawing and show the result 
arcade.finish_render()

arcade.run()
