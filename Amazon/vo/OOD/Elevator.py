from enum import Enum
"""
code implement some methods? or stop at class hireachy
elevator system belong to a certain building?
how to judge overload? exisit a method?
guest? cargo elevator?
multiple elevator in a system?
"""


"""
priority rules? same direction > still > counter direction?
"""

Status = Enum("Status", ("upward", "downward", "still"))


class Request(object):
    def __init__(self, level, *args, **kwargs):
        self.level = level
        return super().__init__(*args, **kwargs)


class Elevator(object):
    def __init__(self, attributes, *args, **kwargs):
        # self.attributes = attributes  : capacity, size, ...
        self.status = Status.still
        self.level = 0
        self.curr_stops = []
        self.next_stops = []

        return super().__init__(*args, **kwargs)

    def recieve_request(self, request: Request):
        pass
    
    def generate_request(self, stop: int):
        import heapq
        if self.status == Status.still:
            heapq.heappush(self.stops, )

class ElevatorSystem(object):
    def __init__(self, *args, **kwargs):
        # self.elevators = []
        return super().__init__(*args, **kwargs)
