from agent.tools import book_appointment
from agent.tools import cancel_appointment
from agent.tools import reschedule_appointment


def process_request(text, language):

    text = text.lower()

    if "book" in text:
        return book_appointment(text)

    if "cancel" in text:
        return cancel_appointment(text)

    if "reschedule" in text:
        return reschedule_appointment(text)

    return "Sorry, I did not understand your request."