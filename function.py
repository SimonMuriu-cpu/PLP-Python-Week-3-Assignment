def calculate_discount(price, discount_percent):
    
    discount = (price * (discount_percent)/100)
    if discount_percent >= 20:
        final_price = price - discount
        return final_price
    else:
        final_price = price
        return final_price
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))
final_price = calculate_discount(price, discount_percent)
print(f"The final price after discount is: {final_price}")