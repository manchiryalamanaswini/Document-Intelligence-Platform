def generate_summary(text):
    # simple logic (guaranteed output)
    if not text:
        return "No summary available"
    return "Summary: " + text[:50]


def classify_genre(text):
    if not text:
        return "Unknown"

    text = text.lower()

    if "love" in text or "romance" in text:
        return "Romance"
    elif "war" in text:
        return "History"
    elif "magic" in text:
        return "Fantasy"
    else:
        return "General"
    
def answer_question(question, context):
    # simple RAG logic (no heavy LLM needed)
    question = question.lower()

    if "summary" in question:
        return "Summary: " + context[:100]

    elif "genre" in question:
        return classify_genre(context)

    elif "about" in question:
        return "This book is about: " + context

    else:
        return "This book discusses: " + context