class Ticket:
    def __init__(self, ticket_id, event_name, price):
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.price = price

    def display_ticket_info(self):
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Event Name: {self.event_name}")
        print(f"Price: ${self.price:.2f}")