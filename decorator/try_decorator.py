def checking_decorator(some_weirdo_function):
    def wrapper():
        really = True
        if really:
            print("Yes, really true")
        else:
            print("No")
        some_weirdo_function()
        print("we are after the called function")

    return wrapper


@checking_decorator
def ima_function():
    print("this is the decorated function")


ima_function()

# before  ima_function is run, we apply the decorator @checking_decorator
# @checking_decorator runs wrapper()
# wrapper sets arbitrary variable really
# wrapper checks arbitrary variable really, it's True, result is print 'Yes really true'
# some_weirdo_function() now applies the called function ima_function()
# ima_function() does its thing now, prints 'this is the decorated function'
# after some_weirdo_function() in the decorator, print 'we are after...'
