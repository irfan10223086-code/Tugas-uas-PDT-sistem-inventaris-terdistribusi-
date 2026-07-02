cat <<EOF> app.py

import psycopg2

def get_conn_a():
    return psycopg2.connect("host=localhost port=5433 dbname=inventaris_a user=admin password=password123")

def get_conn_b():
    return psycopg2.connect("host=localhost port=5434 dbname=inventaris_b user=admin password=password123")

def simpan_barang(nama, stok, kategori):
    if kategori == "A":
        conn = get_conn_a()
        print(f"Mengirim {nama} ke Node A...")
    else:
        conn = get_conn_b()
        print(f"Mengirim {nama} ke Node B...")
    
    cur = conn.cursor()
    cur.execute("INSERT INTO barang (nama_barang, stok) VALUES (%s, %s)", (nama, stok))
    conn.commit()
    cur.close()
    conn.close()

# Menjalankan perintah simpan
simpan_barang("Laptop", 10, "A")
simpan_barang("Mouse", 50, "B")
simpan_barang("Keyboard", 20, "A")
simpan_barang("Monitor", 5, "B")
