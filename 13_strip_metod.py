#  strip method

place = "      warangal    Nit    "
dots  = " .........................."

# print(place+dots)

# to remove left space we use .lstrip() method
print(place.lstrip()+dots)
print(place.rstrip()+dots)
print(place.strip()+dots)

#  .replace 
print(place.replace(" ","#"))