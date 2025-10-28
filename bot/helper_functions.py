import re

def parse_names(text: str) -> list[str]:
    # Split by commas or any whitespace (space, tab, etc.)
    parts = re.split(r'[,\s]+', text.strip())
    # Remove any empty strings just in case
    return [p for p in parts if p]