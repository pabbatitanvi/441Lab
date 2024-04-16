import ollama

paragraph = "Artificial Intelligence is a new technology in the field of computer science. “Artificial” means man-made that is not natural and “Intelligence” refers to the ability to think and make decisions. Therefore, we can say that making machines like computers to take their own decisions is Artificial Intelligence. This could be possible using various computer programming and codes."
sentences = paragraph.split(". ")

map = {}

for line in sentences:
    embedding = ollama.embeddings(line)
    map[line] = embedding

user_input = input("Enter text: ")