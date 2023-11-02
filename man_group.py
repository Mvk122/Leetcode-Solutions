def price():
    years_until = [0,1,2,3,4,5]
    discount_factor = [1, 0.95, 0.91, 0.87, 0.83, 0.8]
    coupon_schedule = [0.5, 1, 1.5, 2, 2.5, 3, 3,5, 4, 4.5]
    coupon_amount = [250 for i in range(len(coupon_schedule))]
    bond_price = 10000

    coupon_amount_final = 0
    for index, coupon_schd in enumerate(coupon_schedule): 
        for discount_index, discount in enumerate(years_until):
            if coupon_schd > discount:
                coupon_amount_final += discount_factor[discount_index] * coupon_amount[index]
        else:
            coupon_amount_final += discount_factor[-1] * coupon_amount[index]
    return coupon_amount_final + bond_price

print(price())