# TODO Найдите количество книг, которое можно разместить на дискете
disk_space_mb = 1.44
disk_space_b = disk_space_mb * 1024 * 1024
count_of_pages = 100
count_of_lines_on_page = 50
count_of_symbols_on_line = 25
one_symbol_weight_b = 4

one_book_weight_b = (one_symbol_weight_b * count_of_symbols_on_line * count_of_lines_on_page * count_of_pages)
max_count_of_books_on_disk = int(disk_space_b // one_book_weight_b)

print("Количество книг, помещающихся на дискету:", max_count_of_books_on_disk)
