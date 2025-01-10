from m3_testcase import felix
import m3_graphics

m3_graphics.display(felix)
m3_graphics.get_height(felix)
def flip_vertical(image):
    m3_graphics.display(image)

flip_vertical(felix)