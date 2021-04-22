#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 20:58:51 2021

@author: pavan kumar palthode

#Sample code to access mysql db using python.

"""#Author :pavan kumar palthode
# Module Imports
import mysql.connector
import sys

# Connect to mysql Platform
try:
    conn = mysql.connector.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="pavandb"

    )
except mysql.Error as e:
    print(f"Error connecting to mysql Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
print(cur)

# Execute Cursor
cur.execute(
    "SELECT product_id,product_name FROM products_tbl")
print(cur)

# Cursor object as an iterator.
for (product_id, product_name) in cur:
    print(f"product_id:{product_id},product_name:{product_name}")
    
# Close cursor
cur.close()

# Close connection
conn.close()
