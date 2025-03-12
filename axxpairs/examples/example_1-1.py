from axxpairs.combo import mypairs
from axxpairs.combo.combinatorics import combine_all

pair_sets = mypairs.MyPairs

"""
 basic functional demo
"""


parameters = [ [ "HomeDepot", "Lowes", "WalMart" ]
             , [ "Desktop-Windows", "Desktop-MacOS", "Desktop-Unix", "Mobile-Android", "Mobile-iOS"]
             , [ "Chrome", "Firefox", "Edge" ]
             ]

# report non-optimized test matrix
test_matrix = combine_all(parameters)

print("NON OPTIMIZED MATRIX ::")
for i, v in enumerate(test_matrix):
    print("%i:\t%s" % (i, str(v)))

# ---
# get optimized pair sets from supplied parameters
optimized_matrix = pair_sets(parameters)

print("DEMO_PAIRWISE_1 ::")
for i, v in enumerate(optimized_matrix):
    print("%i:\t%s" % (i, str(v)))


    