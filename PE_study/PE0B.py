###############
# Question 1  #
###############

"""
A tram packing is a packing following the two simple rules.
"""


###############
# Task 1A     #
###############

"""
Implement the function tram_packing_iter(config)
that returns the final seating arrangement given
the initial seating configuration.

The function must be implemented using iteration
and without any recursion.  Make sure any helper
function is non-recursive (or built-in).
"""

def tram_packing_iter(config):
  return config



### Uncomment to Test
##print(tram_packing_iter("XOX"))
##print(tram_packing_iter("XOOX"))
##print(tram_packing_iter("XOOOX"))
##print(tram_packing_iter("XOOOOX"))
##print(tram_packing_iter("XOOOOOX"))
##print(tram_packing_iter("XOOOOOOX"))
##print(tram_packing_iter("XOOOOOOOX"))
##print(tram_packing_iter("XOOOOOOOOX"))
##print(tram_packing_iter("XOOOOOOOOOX"))


###############
# Task 1B     #
###############

"""
Implement the function tram_packing_rec(config)
that returns the final seating arrangement given
the initial seating configuration.

The function must be implemented using recursion
and without any iteration.  Make sure any helper
function is non-iterative (or built-in).
"""


def tram_packing_rec(config):
  if config == "XOX":
    return "XOX"
  if config == "XOOX":
    return "XOOX"
  else:
    mid  = len(config) // 2
    new_config = config[:mid] + "X" + config[mid+1:]
    #print(new_config)
    right_input_rec = new_config[mid:]
    left_input_rec = new_config[:mid+1]
    #print(right_input_rec)
    #print(new_input_rec)
    
  return tram_packing_rec(left_input_rec)[:-1] + tram_packing_rec(right_input_rec)
    






### Uncomment to Test
##print(tram_packing_rec("XOX"))
##print(tram_packing_rec("XOOX"))hm
#print(tram_packing_rec("XOOOX"))
print(tram_packing_rec("XOOOOX"))
print(tram_packing_rec("XOOOOOX"))
print(tram_packing_rec("XOOOOOOX"))
#print(tram_packing_rec("XOOOOOOOX"))
##print(tram_packing_rec("XOOOOOOOOX"))
#print(tram_packing_rec("XOOOOOOOOOX"))
