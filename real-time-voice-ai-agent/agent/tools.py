from scheduler.appointment_engine import create_booking
from scheduler.appointment_engine import cancel_booking
from scheduler.appointment_engine import reschedule_booking


def book_appointment(text):

    slot = create_booking("patient1","cardiologist","tomorrow")

    return f"Your appointment is booked at {slot}"


def cancel_appointment(text):

    cancel_booking("patient1")

    return "Your appointment has been cancelled"


def reschedule_appointment(text):

    slot = reschedule_booking("patient1")

    return f"Your appointment is moved to {slot}"