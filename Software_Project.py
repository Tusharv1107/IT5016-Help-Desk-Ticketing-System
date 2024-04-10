class Ticket:
    counter = 1
    open_tickets = 0
    closed_tickets = 0
    all_tickets = []

    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_number = Ticket.counter + 2000
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.counter += 1
        Ticket.open_tickets += 1
        Ticket.all_tickets.append(self)

    @staticmethod
    def generate_password(staff_id, creator_name):
        return staff_id[:2] + creator_name[:3]

    def reset_password(self):
        if "Password Change" in self.description:
            new_password = Ticket.generate_password(self.staff_id, self.creator_name)
            self.response = f"New password generated: {new_password}"
            self.status = "Closed"
            Ticket.closed_tickets += 1
            Ticket.open_tickets -= 1

    def respond(self, response):
        self.response = response
        self.status = "Closed"
        Ticket.closed_tickets += 1
        Ticket.open_tickets -= 1

    def reopen(self):
        self.status = "Reopened"
        Ticket.closed_tickets -= 1
        Ticket.open_tickets += 1

    @classmethod
    def ticket_stats(cls):
        return {
            "Tickets Created": cls.counter - 1,
            "Tickets Resolved": cls.closed_tickets,
            "Tickets To Solve": cls.open_tickets
        }

    @classmethod
    def print_all_tickets(cls):
        print("\nPrinting Tickets:")
        for ticket in cls.all_tickets:
            ticket.display()

    def display(self):
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Ticket Creator: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Ticket Status: {self.status}\n")


def create_ticket():
    print("Submit Ticket:")
    staff_id = input("Staff ID: ")
    creator_name = input("Creator Name: ")
    contact_email = input("Contact Email: ")
    description = input("Description: ")
    ticket = Ticket(staff_id, creator_name, contact_email, description)
    print(f"Ticket created successfully! Ticket Number: {ticket.ticket_number}")


def respond_to_tickets():
    ticket_number = int(input("Enter Ticket Number to respond: "))
    for ticket in Ticket.all_tickets:
        if ticket.ticket_number == ticket_number:
            response = input("Enter Response to the Ticket: ")
            ticket.respond(response)
            print("Response added successfully!")
            break
    else:
        print("Ticket not found!")


def main():
    while True:
        print("\nMenu:")
        print("1. Create Ticket")
        print("2. Respond to Ticket")
        print("3. Display Ticket Statistics")
        print("4. Print All Tickets")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_ticket()
        elif choice == "2":
            respond_to_tickets()
        elif choice == "3":
            stats = Ticket.ticket_stats()
            print("\nDisplaying Ticket Statistics:")
            for key, value in stats.items():
                print(f"{key}: {value}")
        elif choice == "4":
            Ticket.print_all_tickets()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
