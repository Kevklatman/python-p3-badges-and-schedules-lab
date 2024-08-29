def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(f"Hello, my name is {name}.")
    return badges

def assign_rooms(speakers):
    rooms = [None] * 8
    room_assignments = []

    for i in range(len(speakers)):
        if i < 8:
            speaker = speakers[i]
            rooms[i] = speaker
            room_number = i + 1
            assignment_message = f"Hello, {speaker}! You'll be assigned to room {room_number}!"
            room_assignments.append(assignment_message)

    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    room_assignments = assign_rooms(names)
    for assignment in room_assignments:
        print(assignment)
