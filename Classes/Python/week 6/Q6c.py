# Initialize a dictionary to store movie bookings by seat numbers
movie_bookings = {}

# Number of bookings to process
num_bookings = int(input("Enter the number of bookings: "))

# Initialize a counter for valid bookings
valid_bookings = 0

# Initialize a counter for total booking attempts (including duplicates)
total_bookings_attempted = 0

# Process each booking
for _ in range(num_bookings):
    # Take the booking input from the user
    booking = input("Enter booking (CustomerName-MovieName-SeatNumber): ")
    
    # Split the input into parts: customer name, movie name, and seat number
    customer_name, movie_name, seat_number = booking.split("-")
    
    # Increment total booking attempts
    total_bookings_attempted += 1
    
    # Check if the movie has a dictionary for seats
    if movie_name not in movie_bookings:
        movie_bookings[movie_name] = {}  # Initialize a dictionary for that movie
    
    # Check if the seat number is already booked for this movie
    if seat_number in movie_bookings[movie_name]:
        print(f"Duplicate booking detected! Seat {seat_number} for movie {movie_name} is already booked by {movie_bookings[movie_name][seat_number]}.")
        print(f"Booking request by {customer_name} is rejected.")
    else:
        # Book the seat and associate it with the customer
        movie_bookings[movie_name][seat_number] = customer_name
        valid_bookings += 1  # Increment only if the booking is successful
        print(f"Booking confirmed for {customer_name} in movie {movie_name}, seat {seat_number}.")

# Final output: Show the bookings for each movie
print("\nFinal bookings:")
for movie, seats in movie_bookings.items():
    print(f"Movie: {movie}")
    for seat, customer in seats.items():
        print(f"  Seat: {seat} -> Customer: {customer}")

# Show the total number of valid bookings
print(f"\nTotal valid bookings: {valid_bookings}")
print(f"Total booking attempts (including duplicates): {total_bookings_attempted}")

