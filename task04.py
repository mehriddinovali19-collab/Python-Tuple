orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]
ordered = []
for order_id, name in orders:
    if order_id % 2 == 0:
        ordered.append((order_id, name))
for order_id, name in ordered:
    print(f"order_id: {order_id}, name: {name}")
    print(ordered)