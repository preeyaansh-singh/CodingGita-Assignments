# real_life_arithmetic.py
# Answers for Questions 36 — 44 (real-life arithmetic problems)

def q36_simple_interest():
    principal = 10000
    rate = 5     # percent
    time = 2     # years
    simple_interest = (principal * rate * time) / 100
    print("Q36 — Simple Interest:")
    print("Simple Interest:", simple_interest)
    print()

def q37_rectangle():
    length = 15  # cm
    width = 8    # cm
    area = length * width
    perimeter = 2 * (length + width)
    print("Q37 — Rectangle:")
    print("Area:", area)
    print("Perimeter:", perimeter)
    print()

def q38_circle():
    r = 7
    pi = 3.14
    area = pi * r * r
    print("Q38 — Circle:")
    print("Area:", area)
    print()

def q39_temperature_conversion():
    celsius = 35
    fahrenheit = (celsius * 9 / 5) + 32
    print("Q39 — Temperature Conversion:")
    print(f"{celsius}°C -> {fahrenheit}°F")
    print()

def q40_time_conversion():
    total_seconds = 367
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    print("Q40 — Time Conversion:")
    print("Minutes:", minutes)
    print("Seconds:", seconds)
    print()

def q41_hms_conversion():
    total_seconds = 7384
    hours = total_seconds // 3600
    rem = total_seconds % 3600
    minutes = rem // 60
    seconds = rem % 60
    print("Q41 — Hours, Minutes and Seconds:")
    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)
    print()

def q42_salary():
    basic = 25000
    hra = 5000
    travel_allowance = 2500
    tax_deduction = 3000
    gross = basic + hra + travel_allowance
    net = gross - tax_deduction
    print("Q42 — Salary Calculation:")
    print("Gross Salary:", gross)
    print("Net Salary:", net)
    print()

def q43_travel_cost():
    distance_km = 120
    km_per_litre = 20
    price_per_litre = 100
    fuel_required = distance_km / km_per_litre
    total_cost = fuel_required * price_per_litre
    print("Q43 — Travel Cost:")
    print("Fuel required (litres):", fuel_required)
    print("Total fuel cost:", total_cost)
    print()

def q44_shopping_discount():
    price = "2500"
    discount = "10"   # percent as string
    # convert to numeric
    price_num = float(price)
    discount_pct = float(discount)
    discount_amount = (price_num * discount_pct) / 100
    final_price = price_num - discount_amount
    print("Q44 — Shopping Discount:")
    print("Discount amount:", discount_amount)
    print("Final price:", final_price)
    print()

if __name__ == "__main__":
    q36_simple_interest()
    q37_rectangle()
    q38_circle()
    q39_temperature_conversion()
    q40_time_conversion()
    q41_hms_conversion()
    q42_salary()
    q43_travel_cost()
    q44_shopping_discount()