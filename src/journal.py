
print("draft")
class journal:
    def __init__(self):
        self.history = []
    
    def add_event(self, event):
        self.history.append(event)
    
    def generate_journal_entry(self, state):
        if state.travelling:
            if state.encounter.event:
                event = f"Encountered an event while travelling from {state.current_city} to {state.destination_city}"
            else:
                event = f"Player is going from {state.current_city} to {state.destination_city}"
                self.add_event(event)
        else:
            event = f"Arrived at {state.current_city}"
            self.add_event(event)
    
    def display(self):
        for event in self.history:
            print(event)