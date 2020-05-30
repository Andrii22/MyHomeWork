def count_sheeps(sheep):
    count = 0
    for sheeps in sheep:
      if sheeps == True:
        count+=1
        sheep = sheep + 1
      elif sheeps == False:
        sheep = sheep + 1
    return count