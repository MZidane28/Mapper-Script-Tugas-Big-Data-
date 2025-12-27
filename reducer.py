import sys

def reducer():
    """
    Reducer function untuk mengagregasi pasangan produk dari mapper
    
    Menerima input terurut dari mapper dalam format:
    item1\titem2\tcount
    
    Output: pasangan produk dengan total frekuensi kemunculannya
    """
    
    current_key = None
    current_count = 0
    
    # Baca setiap baris dari stdin
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        # Parse input: item1\titem2\tcount
        parts = line.split('\t')
        
        if len(parts) != 3:
            continue
        
        item1, item2, count = parts[0], parts[1], int(parts[2])
        
        # Buat key dari pasangan item
        key = f"{item1}\t{item2}"
        
        # Jika key berubah, emit hasil aggregasi sebelumnya
        if current_key is not None and current_key != key:
            print(f"{current_key}\t{current_count}")
        
        # Update key dan count untuk iterasi saat ini
        if current_key != key:
            current_key = key
            current_count = 0
        
        current_count += count
    
    # Emit hasil terakhir
    if current_key is not None:
        print(f"{current_key}\t{current_count}")

if __name__ == "__main__":
    reducer()
