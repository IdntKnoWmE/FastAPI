def note_instance(item) -> dict:
    return {
        "id": str(item.get("_id")),
        "title": item.get("title"),
        "description": item.get("description"),
        "important": item.get("important")
    }


def notes_instance(items) -> list:
    return [note_instance(item) for item in items]
