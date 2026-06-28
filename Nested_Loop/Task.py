tables = ['Customers', 'orders', 'product','prices']
Columns = ['id', 'create_date']

for t in tables:
    for c in Columns:
        print(f"select count(*) from {t} where {c} Is Null;")