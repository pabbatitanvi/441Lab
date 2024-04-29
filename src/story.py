import openai as ai

api = "api"
ai.api_key = api

class Generate_Story:
    def __init__(self, journal_events):
        self.journal_events = journal_events
    
    def generate(self):
        text = "\n".join(self.journal_events)

        prompt = "Create a 200 word story with these events \n" + text
        
        response = ai.Completion.create(engine = "text-davinci-003", prompt = prompt, temperature = 0.7, max_tokens = 100, n = 1)

        story = response.choices[0].text.strip()

        return story
    