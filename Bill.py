def calculate_bill(items, tax_rate):
    total_before_tax = 0
    
    
    for item, (price, quantity) in items.items():
        total_before_tax += price * quantity
    
    
    tax_amount = total_before_tax * (tax_rate / 100)
    
    
    total_after_tax = total_before_tax + tax_amount
    
    return total_before_tax, tax_amount, total_after_tax

def main():
    print("Welcome to the Bill Calculator!")
    
  
    items = {}
    
    while True:
        
        item_name = input("Enter the item name (or type 'done' to finish): ").strip()
        if item_name.lower() == 'done':
            break
        
        try:
            item_price = float(input(f"Enter the price of {item_name}: "))
            item_quantity = int(input(f"Enter the quantity of {item_name}: "))
        except ValueError:
            print("Invalid input! Please enter numbers for price and quantity.")
            continue
        
       
        items[item_name] = (item_price, item_quantity)
    
   
    try:
        tax_rate = float(input("Enter the tax rate (in %): "))
    except ValueError:
        print("Invalid tax rate! Setting tax rate to 0%.")
        tax_rate = 0
    
    
    total_before_tax, tax_amount, total_after_tax = calculate_bill(items, tax_rate)
    
   
    print("\n--- BILL SUMMARY ---")
    for item, (price, quantity) in items.items():
        print(f"{item}: ₹{price} x {quantity} = ₹{price * quantity}")
    print(f"\nTotal before tax: ₹{total_before_tax:.2f}")
    print(f"Tax ({tax_rate}%): ₹{tax_amount:.2f}")
    print(f"Total after tax: ₹{total_after_tax:.2f}")

if __name__ == "__main__":
    main()
