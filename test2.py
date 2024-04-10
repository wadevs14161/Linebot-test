product_list = [{'serial': '450314', 'serial_alt': '460909', 'id': '07001272', 'color': 'White', 'size': 'XS', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07001273', 'color': 'White', 'size': 'S', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07001274', 'color': 'White', 'size': 'M', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07001275', 'color': 'White', 'size': 'L', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07001276', 'color': 'White', 'size': 'XL', 'stock': 'STOCK_OUT', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07001277', 'color': 'White', 'size': 'XXL', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07001278', 'color': 'White', 'size': '3XL', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07001296', 'color': 'Black', 'size': 'XS', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07001297', 'color': 'Black', 'size': 'S', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07001298', 'color': 'Black', 'size': 'M', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07001299', 'color': 'Black', 'size': 'L', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07001300', 'color': 'Black', 'size': 'XL', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07001301', 'color': 'Black', 'size': 'XXL', 'stock': 'LOW_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07001302', 'color': 'Black', 'size': '3XL', 'stock': 'LOW_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07606829', 'color': 'Brown', 'size': 'XS', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07606830', 'color': 'Brown', 'size': 'S', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07606831', 'color': 'Brown', 'size': 'M', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07606832', 'color': 'Brown', 'size': 'L', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07606833', 'color': 'Brown', 'size': 'XL', 'stock': 'STOCK_OUT', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07606834', 'color': 'Brown', 'size': 'XXL', 'stock': 'STOCK_OUT', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07606835', 'color': 'Brown', 'size': '3XL', 'stock': 'STOCK_OUT', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07606845', 'color': 'Green', 'size': 'XS', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07606846', 'color': 'Green', 'size': 'S', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07606847', 'color': 'Green', 'size': 'M', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07606848', 'color': 'Green', 'size': 'L', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07606849', 'color': 'Green', 'size': 'XL', 'stock': 'IN_STOCK', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07606850', 'color': 'Green', 'size': 'XXL', 'stock': 'STOCK_OUT', 'price': 4990}, {'serial': '450314', 'serial_alt': '460909', 'id': '07606851', 'color': 'Green', 'size': '3XL', 'stock': 'STOCK_OUT', 'price': 4990}]

available_dict = {}

for item in product_list:
    if item['stock'] != 'STOCK_OUT' and item['color'] not in available_dict:
        available_dict[item['color']] = []

    if item['stock'] != 'STOCK_OUT' and item['color'] in available_dict:
        available_dict[item['color']].append(item['size'])


reply = "商品庫存\n{}".format(available_dict)

print(available_dict)
print(reply)