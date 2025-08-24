def bottles_of_beer(bob):
    """Print song about 99 bottles of the beer
    :param bob: should be int number"""
    if bob < 1:
        print("No bottles of the beer on the wall. No bottles of the beer.")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of the beer on the wall. {} bottles of the beer.
          Take one, let it go around, {} bottles of the beer on the wall.
          """.format(tmp,
                     tmp,
                     bob))
    bottles_of_beer(bob)


bottles_of_beer(99)
