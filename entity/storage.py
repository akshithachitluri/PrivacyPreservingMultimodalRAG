import json
import os

# Location to store detected entities
ENTITY_FILE = "data/entities.json"


def save_entities(entities):
    """
    Save detected entities to entities.json.
    If the file already exists, merge new entities without duplicates.
    """

    os.makedirs("data", exist_ok=True)

    existing = []

    if os.path.exists(ENTITY_FILE):
        with open(ENTITY_FILE, "r", encoding="utf-8") as file:
            try:
                existing = json.load(file)
            except json.JSONDecodeError:
                existing = []

    seen = {
        (item["text"].lower(), item["label"])
        for item in existing
    }

    for entity in entities:
        key = (entity["text"].lower(), entity["label"])

        if key not in seen:
            existing.append(entity)
            seen.add(key)

    with open(ENTITY_FILE, "w", encoding="utf-8") as file:
        json.dump(existing, file, indent=4)


def load_entities():
    """
    Load all saved entities.
    """

    if not os.path.exists(ENTITY_FILE):
        return []

    with open(ENTITY_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def clear_entities():
    """
    Remove all stored entities.
    """

    with open(ENTITY_FILE, "w", encoding="utf-8") as file:
        json.dump([], file, indent=4)


def entity_exists(text, label):
    """
    Check if an entity already exists.
    """

    entities = load_entities()

    for entity in entities:
        if (
            entity["text"].lower() == text.lower()
            and entity["label"] == label
        ):
            return True

    return False


def get_entities_by_label(label):
    """
    Return all entities of a given type.
    Example:
        PERSON
        ORG
        GPE
        EMAIL
    """

    entities = load_entities()

    return [
        entity
        for entity in entities
        if entity["label"] == label
    ]