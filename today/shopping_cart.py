# from IPython.display import clear_output

class RemoveError(Exception):
    pass

class Cart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        for obj in self.items:
            if obj.name == item:
                self.items.remove(obj)
                break

    def is_in_cart(self, item_name):
        for item_obj in self.items:
            if item_obj.name == item_name:
                return True
        return False

    def show_cart(self):
        if not self.items:
            print('You currently have no items in your cart.')
        else:
            display_cart = []
            # want to add dictionary objects into the display cart
            for obj in self.items:
                if obj.name not in [i['name'] for i in display_cart]:
                    display_cart.append({
                        'name': obj.name,
                        'price': obj.price
                    })
                else:
                    for i in display_cart:
                        if i['name'] == obj.name:
                            i['price'] += obj.price
            for idx, item in enumerate(display_cart):
#                 ["return statement" for loop]
                print(f"{idx+1}) {item['name']} @ ${item['price']} [{[obj.name for obj in self.items].count(item['name'])}]")
        print("=" * 60)

    def clear_cart(self):
        self.items.clear()

class CartItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shop:
    def display_message(self):
        return input('Your input was invalid. Please try again. ')

    def show_instructions(self):
        print("""Type 'add' to add an item to your cart.
Type 'remove' to remove an item from your cart.
Type 'clear' to remove all items from your cart.
Type 'quit' to quit the program.""")
        print("=" * 60)
    
    def run(self):
        # customer starts shopping session by taking out a new cart
        shopping_cart = Cart()
    
        while True:
            decision = input("Would you like to continue? Y/N? ").lower()

            if decision == 'n':
                break
            elif decision == 'y':
                # always clear the output before rendering anything else
                # clear_output()

                # display some instructions
                self.show_instructions()

                # show the shopping_cart
                shopping_cart.show_cart()

                decision = input("What would you like to do? ").lower()

                if decision == 'quit':
                    break
                elif decision == 'add':
                    done_adding = False
                    while not done_adding:
                        # get name
                        item_name = input('What item would you like to add? ').lower()
                        try:
                            # get price
                            item_price = float(input("How much does this item cost? "))
                            # create new item
                            cart_item = CartItem(item_name, item_price)
                            shopping_cart.add_item(cart_item)
                            
                            done_adding = True
                        except Exception:
                            input('You have entered an invalid price. Please try again.')
                            # clear_output()
                elif decision == 'remove':
                    try:
                        item_to_remove = input('What item would you like to remove? ').lower()

                        if len(shopping_cart.items) == 0:
                            raise RemoveError('[Error removing item from cart] Your cart is empty. ')
                        if not shopping_cart.is_in_cart(item_to_remove):
                            raise RemoveError(f'{item_to_remove} is not in the cart')

                        shopping_cart.remove_item(item_to_remove)
                    except RemoveError as err:
                        print(err)
                elif decision == 'clear':
                    confirm = input('Are you sure? This will remove all items from your cart. Y/N? ').lower()
                    if confirm == 'y':
                        shopping_cart.clear_cart()
                    elif confirm == 'n':
                        continue
                    else:
                        self.display_message()
                else:
                    self.display_message()
            else:
                self.display_message()