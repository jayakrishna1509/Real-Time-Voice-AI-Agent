appointments = {}

available_slots = ["10:00 AM","2:00 PM","4:30 PM"]


def create_booking(patient, doctor, date):

    for slot in available_slots:

        if slot not in appointments.values():

            appointments[patient] = slot

            return slot

    return "No slots available"


def cancel_booking(patient):

    if patient in appointments:
        del appointments[patient]


def reschedule_booking(patient):

    cancel_booking(patient)

    return create_booking(patient,"doctor","tomorrow")