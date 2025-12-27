import sys
import csv

def mapper():
    """
    Mapper function untuk membaca transaksi dan emit pasangan produk
    
    Untuk setiap transaksi:
    1. Baca struk belanja (ambil produk yang dibeli)
    2. Buat semua kombinasi pasangan produk (item pairs)
    3. Emit pasangan dengan format: (item1, item2) -> 1
    """
    
    # Baca header untuk mendapatkan nama produk
    reader = csv.reader(sys.stdin)
    header = next(reader)
    product_names = header[1:]  # Skip kolom 'Transaction'
    
    # Proses setiap transaksi
    for line in reader:
        if not line:
            continue
            
        transaction_id = line[0]
        items_purchased = []
        
        # Ambil semua produk yang dibeli (nilai = 1)
        for i, value in enumerate(line[1:], start=0):
            if value.strip() == '1':
                items_purchased.append(product_names[i])
        
        # Generate semua pasangan produk dari transaksi ini
        # Contoh: jika beli [Roti, Susu, Telur]
        # Maka emit: (Roti, Susu), (Roti, Telur), (Susu, Telur)
        num_items = len(items_purchased)
        for i in range(num_items):
            for j in range(i + 1, num_items):
                item1 = items_purchased[i]
                item2 = items_purchased[j]
                
                # Emit pasangan item (diurutkan agar konsisten)
                # Format: item1\titem2\t1
                if item1 < item2:
                    print(f"{item1}\t{item2}\t1")
                else:
                    print(f"{item2}\t{item1}\t1")

if __name__ == "__main__":
    mapper()
