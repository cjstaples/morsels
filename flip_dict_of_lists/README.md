--
write a function that takes a dictionary of lists and returns a "flipped" dictionary of lists. What I mean by "flipped" is this:

 
>>> d = {'a': [1, 2], 'b': [3, 1], 'c': [2]}
>>> flip_dict_of_lists(d)
{1:  ['a', 'b'], 2: ['a', 'c'], 3: ['b']}

Your function should accept any dictionary type and the output lists should maintain the order of given keys (for ordered dictionaries).

--

As a bonus, allow your function to accept a dict_type argument that will return a new dictionary-like object when called ✔️:

>>> toppings = OrderedDict([('Trey', ['anchovies', 'olives']), ('Guido', ['olives', 'pineapple'])])
>>> flip_dict_of_lists(toppings, dict_type=OrderedDict)
OrderedDict([('anchovies', ['Trey']), ('olives', ['Trey', 'Guido']), ('pineapple', ['Guido'])])

As a second bonus, allow your function to accept a key_func argument that will be called to normalize the keys in the new dictionary  ✔️:

>>> toppings = {'Trey': ['anchovies', 'olives'], 'Guido': ['Olives', 'Pineapple']}
>>> def lowercase(string): return string.lower()
...
>>> flip_dict_of_lists(toppings, key_func=lowercase)
{'anchovies': ['Trey'], 'olives': ['Trey', 'Guido'], 'pineapple': ['Guido']}

--

Automated tests for this week's exercise can be found here. 
You'll need to write your function in a module named flip.py next to the test file. 
To run the tests you'll run "python test_flip.py" and check the output for "OK". You'll see that there are some "expected failures" (or "unexpected successes" maybe). 
If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly. 

===
original content from python morsels:
Trey Hunner trey@truthful.technology via dripemail2.com
