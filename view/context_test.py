from engine.resource_loader import ResourceLoader


prompt = ResourceLoader.load_text("prompts/automata_v1.txt")
print(prompt)
