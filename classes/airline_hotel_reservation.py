from datetime import datetime, timedelta


class ReservationSystem:
    def __init__(self):
        self.airline_seats = {'First Class': 10, 'Business Class': 20, 'Economy Class': 50}
        self.hotel_rooms = {'Penthouse Suite': 5, 'Standard Room': 20}
        self.reservations = {}

    def book_airline_seat(self, seat_class):
        if self.airline_seats.get(seat_class, 0) > 0:
            self.airline_seats[seat_class] -= 1
            return True
        else:
            return False

    def book_hotel_room(self, room_type):
        if self.hotel_rooms.get(room_type, 0) > 0:
            self.hotel_rooms[room_type] -= 1
            return True
        else:
            return False

    def make_reservation(self, name, reservation_type, item_type):
        if reservation_type.lower() == 'airline':
            if self.book_airline_seat(item_type):
                self.reservations[name] = (reservation_type, item_type, datetime.now())
                return f"Reservation successful for {name} in {reservation_type} - {item_type}"
            else:
                return f"No available {item_type} seats in {reservation_type}"

        elif reservation_type.lower() == 'hotel':
            if self.book_hotel_room(item_type):
                self.reservations[name] = (reservation_type, item_type, datetime.now())
                return f"Reservation successful for {name} in {reservation_type} - {item_type}"
            else:
                return f"No available {item_type} rooms in {reservation_type}"

    def get_reservation_status(self):
        return self.reservations

    def cancel_reservation(self, name):
        if name in self.reservations:
            reservation = self.reservations.pop(name)
            reservation_type, item_type, booking_time = reservation
            if reservation_type == 'airline':
                self.airline_seats[item_type] += 1
            elif reservation_type == 'hotel':
                self.hotel_rooms[item_type] += 1
            return f"Reservation for {name} ({reservation_type} - {item_type}) has been canceled."
        else:
            return "No reservation found for this name."


if __name__ == "__main__":
    system = ReservationSystem()

    # reservations
    print(system.make_reservation('John Doe', 'Airline', 'First Class'))
    print(system.make_reservation('Jane Smith', 'Hotel', 'Penthouse Suite'))
    print(system.make_reservation('Alice', 'Hotel', 'Standard Room'))

    # Checking reservation
    print(system.get_reservation_status())

    # Cancelling a reservation
    print(system.cancel_reservation('John Doe'))

    # Checking reservation status after cancellation
    print(system.get_reservation_status())
