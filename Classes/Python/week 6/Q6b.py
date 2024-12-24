
movie_book = {}
num_book = int(input("Enter the number of bookings: "))
valid_book = 0

for i in range(num_book):
    booking = input("Enter booking (CustomerName-MovieName-SeatNumber): ")
    cust_name, movie_name, seat_number = booking.split("-")
    
    if movie_name not in movie_book:
        movie_book[movie_name] = {}  
    
    if seat_number in movie_book[movie_name]:
        print(f"Duplicate booking detected! Seat {seat_number} for movie {movie_name} is already booked by {movie_book[movie_name][seat_number]}.")
        print(f"Booking request by {cust_name} is rejected.")
    else:
        movie_book[movie_name][seat_number] = cust_name
        valid_book += 1  
        print(f"Booking confirmed for {cust_name} in movie {movie_name}, seat {seat_number}.")

print("\nFinal bookings:")

for movie, seats in movie_book.items():
#    print(f"Movie: {movie}")
    for seat, cust in seats.items():
#        print(f"  Seat: {seat} > customer: {cust}")
        print(seats)

print(f"\nTotal valid book: {valid_book}")
print(movie_book)
print(seats)

