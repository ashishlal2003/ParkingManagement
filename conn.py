import sqlite3

conn = sqlite3.connect('customer.db')
c = conn.cursor()
c.execute('''CREATE TABLE customer
             (ID INT PRIMARY KEY NOT NULL,
             Name TEXT NOT NULL,
             Address TEXT NOT NULL,
             PostalCode INT NOT NULL,
             Country TEXT NOT NULL);''')

c.execute("INSERT INTO customer (ID, Name, Address, PostalCode, Country) VALUES (1, 'John Smith', '123 Main St', 12345, 'USA')")
c.execute("INSERT INTO customer (ID, Name, Address, PostalCode, Country) VALUES (2, 'Jane Doe', '456 Elm St', 67890, 'Canada')")
c.execute("INSERT INTO customer (ID, Name, Address, PostalCode, Country) VALUES (3, 'Mohammed Ahmed', '789 Park St', 23456, 'Egypt')")
c.execute("INSERT INTO customer (ID, Name, Address, PostalCode, Country) VALUES (4, 'Hans Schmidt', '1010 Wien St', 1010, 'Austria')")
c.execute("INSERT INTO customer (ID, Name, Address, PostalCode, Country) VALUES (5, 'Sita Singh', '567 Green St', 110011, 'India')")

print("Customer details in ascending order:")
for row in c.execute("SELECT * FROM customer ORDER BY Name ASC"):
    print(row)

c.execute("CREATE VIEW indian_customers AS SELECT * FROM customer WHERE Country='India'")

print("\nDetails of Indian customers:")
for row in c.execute("SELECT * FROM indian_customers"):
    print(row)
conn.commit()
conn.close()