def calc_future_eps(eps, growth):
  return eps * (growth/100+1)**10

def calc_sticker(price_in_10, minimum_return):
  return price_in_10 / (minimum_return ** 10)

eps = float(input("EPS (TTM): "))
pe = float(input("PE (TTM): ")) # min(5yr average, twice the growth)
growth = float(input("Growth rate: ")) # Example: 15% = 15

minimum_return = 1.15

future_eps = calc_future_eps(eps, growth)
price_in_10 = future_eps * pe

sticker = calc_sticker(price_in_10, minimum_return)

print("sticker is " + str(sticker))