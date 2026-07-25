import re
import spacy

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Regex Patterns
EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
PHONE_PATTERN = r"(?:\+91[-\s]?)?[6-9]\d{9}"


def detect_entities(text):
    """
    Detect named entities, emails, and phone numbers from text.

    Parameters:
        text (str): Input document text

    Returns:
        list: List of detected entities
    """

    doc = nlp(text)

    entities = []

    # ----------------------------
    # SpaCy Named Entity Recognition
    # ----------------------------
    for ent in doc.ents:
        # Ignore plain numbers
        if ent.label_ == "CARDINAL":
            continue

        entities.append({
            "text": ent.text.strip(),
            "label": ent.label_
    })

    # ----------------------------
    # Email Detection
    # ----------------------------
    emails = re.findall(EMAIL_PATTERN, text)

    for email in emails:
        entities.append({
            "text": email,
            "label": "EMAIL"
        })

    # ----------------------------
    # Phone Number Detection
    # ----------------------------
    phones = re.findall(PHONE_PATTERN, text)

    for phone in phones:
        entities.append({
            "text": phone,
            "label": "PHONE"
        })

    # ----------------------------
    # Remove Duplicates
    # ----------------------------
    unique = []
    seen = set()

    for entity in entities:
        key = (entity["text"].lower(), entity["label"])

        if key not in seen:
            seen.add(key)
            unique.append(entity)

    return unique