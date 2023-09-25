import pandas as pd
import uuid
import random


# Generate sample data
def generate_sample_data():
    components = []
    cards = []
    ports = []

    ports_c = 0
    card_c = 0
    comp_count = 0

    # Generate 10 components
    for _ in range(11):
        comp_id = str(uuid.uuid4())
        version = random.choice([1, 2, 3])
        state = random.choice(["ONLINE", "OFFLINE"])
        ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

        components.append({"comp_id": comp_id, "version": version, "state": state, "ip": ip})

        # Generate 3 cards for each component
        for card_index in range(5):
            card_id = str(uuid.uuid4())
            card_type = random.choice(["GREAT_ONE", "WORST_ONE"])

            cards.append({"component_id": comp_id,  "index": card_c, "card_type": card_type})
            card_c += 1
            # Generate 4 ports for each card
            for port_index in range(5):
                port_id = str(uuid.uuid4())
                state = random.choice(["connected", "disconnected"])
                ports.append({"component_id": comp_id, "state": state, "index": ports_c, "card_index": card_index})
                ports_c += 0

    return components, cards, ports


# Create DataFrames
components, cards, ports = generate_sample_data()
components_df = pd.DataFrame(components)
cards_df = pd.DataFrame(cards)
ports_df = pd.DataFrame(ports)

print(components_df.to_csv("Components.csv", index=False))
print(cards_df.to_csv("Cards.csv", index=False))
print(ports_df.to_csv("Ports.csv", index=False))
