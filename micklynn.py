
#Sales Tracking Solution.

def record_sale(sku, quantity):
  
    #Update stock levels based on sold quantity

    #variable sku: string, the Stock Keeping Unit of the product
    #variable quantity: integer, the quantity sold
 
    product = get_product_by_sku(sku)
    product.stock_level -= quantity
    update_product(product)


#Re-order Point Calculation Solution:
def calculate_re-order_point(sku)

    #Calculate re-order point based on historical sales data, lead time, and safety stock level

    #variable sku: string, the Stock Keeping Unit of the product
    #return: integer, the re-order point

    product = get_product_by_sku(sku)
    reorder_point = product.average_sales_per_day * product.lead_time + product.safety_stock
    return reorder_point


#Re-ordering Process Solution:

def generate_purchase_order(products_below_re-order)
    
    #Generate a purchase order for products that need restocking

    #variable products_below_re-order: list of products that need to be restocked
    #return: dictionary, the purchase order information
    
    purchase_order = {}
    for product in products_below_re-order:
        re-order_quantity = calculate_re-order_quantity(product.sku)
        purchase_order[product.sku] = re-order_quantity
    return purchase_order



