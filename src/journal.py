from story import Generate_Story
class journal:
    def __init__(self):
        self.history = []
    
    def add_event(self, event):
        self.history.append(event)
    
    def generate_journal_entry(self, state, city_names):
        current = city_names[state.current_city]
        destination = city_names[state.destination_city]
        if len(self.history) > 0 and self.history[-1] == f"Encountered an event at {current}":
            return
        if state.travelling:
            if state.encounter_event:
                event = f"Encountered an event at {current}"
                self.add_event(event)
            else:
                event = f"Player is going from {current} to {destination}"
                self.add_event(event)

        if state.current_city == state.destination_city:
            final = city_names[state.destination_city]
            event = f"Arrived at {final}"
            self.add_event(event)
    
    def display(self):
        for event in self.history:
            print(event)
            
        #uncomment this to make the model create a story

        #story_generate = Generate_Story(self.history)
        #story = story_generate.generate()
        #print(story)