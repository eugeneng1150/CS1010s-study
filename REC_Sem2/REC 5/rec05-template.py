#
# CS1010S --- Programming Methodology
#
# Recitation 5

from r5_images import display, WHITE, BLACK, FELIX, LUNA


def make_pixel(r, g, b):
    pixel = (r, g, b)
    return pixel


def get_r(pixel):
    return pixel[0]


def get_g(pixel):
    return pixel[1]


def get_b(pixel):
    return pixel[2]


##############
# Question 1 #
##############
t0 = (2,)
t1 = (2,3,4)
t2 = (5,6,7)
t3 = (1,2,3)
t4 = (9,8,7)
print(t4[:10]) # note that no error shown
empty = ()
new = ((t1 , t2) , (t3 , t4))
print(new)
print(empty + (t1,) + (t2,) + (t3,))
(((0,0,0) , (0,0,0)) , ((0,0,0) , (0,0,0)))

def make_image(width, height):
    image = ()
    for _ in range(width): 
        row_tuple = ()
        for _ in range(height):
            row_tuple += (WHITE,)
        image += (row_tuple,)
    return image
    

def get_pixel(image, row, col):
    return image[row][col]


def get_width(image):
    return len(image[0])


def get_height(image):
    return len(image)


def set_pixel(image, row, col, pixel):
    pass


# Tests
checker = make_image(2, 2)
##print(get_width(checker))
##print(get_height(checker))
##checker = set_pixel(checker, 0, 1, BLACK)
##checker = set_pixel(checker, 1, 0, BLACK)
##pixel = get_pixel(checker, 0, 1)
##print(get_r(pixel))
display(checker)


##############
# Question 2 #
##############


def load_image_from_data(image, data):
    # Your code here
    pass


##felix_width = felix_height = 16
##luna_width = luna_height = 16
##felix = make_image(felix_width, felix_height)
##felix = load_image_from_data(felix, FELIX)
##luna = make_image(luna_width, luna_height)
##luna = load_image_from_data(luna, LUNA)
##display(felix) # See below
##display(luna) # See below


def crop(image, row_from, col_from, row_to, col_to):
    # Your code here
    pass


# Setup -- UNCOMMENT AFTER crop is defined
##felix_head = crop(felix, 0, 0, 10, 10)
##print(get_width(felix_head) == 11)
##display(felix_head)
##display(crop(luna, 0, 0, 10, 10))
