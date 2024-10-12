def largest_pair_sum(numbers): 
    # Urutkan angka dari yang terbesar ke yang terkecil
    sorted_numbers = sorted(numbers, reverse=True)
    # Ambil dua angka terbesar dan jumlahkan
    return sorted_numbers[0] + sorted_numbers[1]