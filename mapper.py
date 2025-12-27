import sys

def mapper():
    """
    Mapper function untuk membaca transaksi dan emit pasangan produk
    
    Untuk setiap transaksi:
    1. Baca struk belanja (ambil produk yang dibeli)
    2. Buat semua kombinasi pasangan produk (item pairs)
    3. Emit pasangan dengan format: (item1, item2) -> 1
    
    Format input: setiap baris berisi produk yang dibeli, dipisahkan koma
    Contoh: Bread,Coffee,Muffin
    """
    
    # Proses setiap transaksi (setiap baris)
    for line in sys.stdin:
        line = line.strip()
        
        # Skip baris kosong
        if not line:
            continue
        
        # Split produk berdasarkan koma dan bersihkan whitespace
        items_purchased = [item.strip() for item in line.split(',') if item.strip()]
        
        # Skip jika hanya ada 1 item atau kurang (tidak bisa buat pasangan)
        if len(items_purchased) < 2:
            continue
        
        # Generate semua pasangan produk dari transaksi ini
        # Contoh: jika beli [Bread, Coffee, Muffin]
        # Maka emit: (Bread, Coffee), (Bread, Muffin), (Coffee, Muffin)
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
