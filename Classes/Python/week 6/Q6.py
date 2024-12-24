movie_bookings = {}
num_bookings = int(input("Enter the number of bookings: "))

for _ in range(num_bookings):
    booking = input("Enter booking (CustomerName-MovieName-SeatNumber): ")
    customer_name, movie_name, seat_number = booking.split("-")
    
    if movie_name not in movie_bookings:
        movie_bookings[movie_name] = {}  
    
    if seat_number in movie_bookings[movie_name]:
        print(f"Duplicate booking detected! Seat {seat_number} for movie {movie_name} is already booked by {movie_bookings[movie_name][seat_number]}.")
        print(f"Booking request by {customer_name} is rejected.")
    else:
        movie_bookings[movie_name][seat_number] = customer_name
        print(f"Booking confirmed for {customer_name} in movie {movie_name}, seat {seat_number}.")
    
print("\nFinal bookings:")
for movie, seats in movie_bookings.items():
    print(f"Movie: {movie}")
    for seat, customer in seats.items():
        print(f"  Seat: {seat} > Customer: {customer}")
        
print(movie_bookings)
        
        

