discounts = {
    1: 0,
    2: 0.05,
    3: 0.10,
    4: 0.15,
    5: 0.20
}


def calculate_price(books):
    num_books = len(books)

    if num_books <= 1:
        return 8 * len(books)

    num_different_books = len(set(books))
    discount = discounts[num_different_books]

    if num_different_books == num_books:
        return 8 * num_books * (1 - discount)

    if num_different_books < num_books:
        if many_sets(books):
            num_sets = num_books / num_different_books
            return calculate_price(list(set(books))) * num_sets
        else:
            return 8 * num_different_books * (1 - discount) + (8 * (num_books - num_different_books))


def many_sets(books):
    books_set = set(books)
    for book in books_set:
        if books.count(book) == 1:
            return False
    return True
