class Mansion:
    def __init__(self):
        self.rooms = {
            "Kitchen": ["Ballroom", "Dining Room"],
            "Ballroom": ["Kitchen", "Conservatory"],
            "Dining Room": ["Kitchen", "Lounge"],
            "Lounge": ["Dining Room", "Library"],
            "Library": ["Lounge", "Study"],
            "Study": ["Library", "Hall"],
            "Hall": ["Study", "Conservatory"],
            "Conservatory": ["Ballroom", "Hall"]
        }

    def show_layout(self):
        for room, connections in self.rooms.items():
            print(f"{room} is connected to: {', '.join(connections)}")