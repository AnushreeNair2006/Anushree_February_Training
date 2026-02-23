customer_name=input("Enter customer name:")
product_price=float(input("Enter product price:"))
premium_member=input("Is the customer premium member(True/False)?").upper()=="TRUE"
coupen_code=input("Enter coupen code:").upper()
discount=0
if product_price>5000 and premium_member :discount=0.20
elif coupen_code=="SAVE10" or premium_member :discount=0.10
discount_price=product_price*discount
final_price=product_price-discount
print("Customer Bill")
print("Original price:", product_price)
print("Discount:",discount)
print("Final price:",final_price)
if premium_member:
    print("Premium benefits applied")