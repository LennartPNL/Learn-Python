# Local and Global Scope

def localExample():
    var = 12 # Assigning value in local scope
    print(str(var+var))

localExample() # Print out var + var

# print(var) -> This will result in an error because var is only defined within localExample's scope

# Reuse variable names in different local scopes

def dog():
    cat = 1
    fish()
    print('Dog: ' + str(cat)) # The value of cat in this scope (1) wil be printed

def fish():
    poodle = 2
    cat = 2 # This value exists in the fish's scope
    print('Fish: ' + str(cat))

dog()


# Global variables in a local scope

def globVar():
    print(someGlobVar)

# This variable is not defined within a local scope, it is global
someGlobVar = 'Mr. worldwide'

# someGlobVar can be reached from a local scope
globVar()

# It also can be read globally 
print(someGlobVar)

# Global Statement

def modGlob():
    global bird
    bird = 'Cool' # Redifining a global variable from within a function

bird = 11
modGlob() # Here, the value of global variable bird is being modified
print(bird)




