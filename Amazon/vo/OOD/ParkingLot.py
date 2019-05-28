from enum import Enum
"""
设计一个停车场

一共有n层，每层m列，每列k个位置
2.停车场可以停摩托车，公交车，汽车
3.停车位分别有摩托车位，汽车位，大型停车位
4.每一列，摩托车位编号范围为[0,k/4)(注：包括0，不包括k/4),
    汽车停车位编号范围为[k/4,k/4*3),大型停车位编号范围为[k/4*3,k)
5.一辆摩托车可以停在任何停车位
6.一辆汽车可以停在一个汽车位或者大型停车位
7.一辆公交车可以停在一列里的连续5个大型停车位。
"""

"""
park from high level to low level? or other rules?
"""


class Size(Enum):
    small = 0
    medium = 1
    large = 2
    other = 9


class Vehicle(object):
    def __init__(self, *args, **kwargs):
        self.occupation = []
        self.license = None
        return super().__init__(*args, **kwargs)

    def park(self, spot: Spot):
        self.occupation.append(Spot)


class Motor(Vehicle):
    def __init__(self, *args, **kwargs):
        self.size = Size.small
        return super().__init__(*args, **kwargs)


class Car(Vehicle):
    def __init__(self, *args, **kwargs):
        self.size = Size.medium
        return super().__init__(*args, **kwargs)


class Bus(object):
    def __init__(self, *args, **kwargs):
        self.size = Size.large
        return super().__init__(*args, **kwargs)


class ParkingLot(object):
    def __init__(self, nlevels, ncols, nspots, *args, **kwargs):
        self.nlevels, self.ncols, self.nspots = nlevels, ncols, nspots
        self.levels = [Level(lv, self.ncol, self.nspots) for lv in range(nlevels)]
        self.vehicles = set()
        return super().__init__(*args, **kwargs)

    def park(self, vehicle: Vehicle):
        for level in self.levels:
            if level.park(vehicle):
                self.vehicles.add(vehicle)
                return True
        return False

    def remove(self, vehicle):
        if vehicle not in self.vehicles:
            return False
        spots = vehicle.occupation
        for spot in spots:
            spot.remove(vehicle)
        return True


class Level(object):
    def __init__(self, lv: int, ncols: int, nspots: int, *args, **kwargs):
        self.lv, self.ncols, self.nspots = lv, ncols, nspots
        self.spots = [[None for _ in range(nspots)] for _ in range(ncols)]
        return super().__init__(*args, **kwargs)

    def park(self, vehicle):
        is_found, spots = self.find_spots(vehicle.size)
        if is_found:
            for spot in spots:
                spot.park(vehicle)
            return True
        return False

    def find_spots(self, size: Size) -> (bool, [Spot]):
        if size == Size.small:
            for c in range(self.ncols):
                for sp in range(self.nspots // 4):
                    if not self.spots[c][sp].is_occupied():
                        return True, [self.spots[c][sp]]
            for c in range(self.ncols):
                for sp in range(self.nspots // 4, self.nspots // 4 * 3):
                    if not self.spots[c][sp].is_occupied():
                        return True, [self.spots[c][sp]]
            for c in range(self.ncols):
                for sp in range(self.nspots // 4 * 3, self.nspots):
                    if not self.spots[c][sp].is_occupied():
                        return True, [self.spots[c][sp]]
        elif size == Size.medium:
            for c in range(self.ncols):
                for sp in range(self.nspots // 4, self.nspots // 4 * 3):
                    if not self.spots[c][sp].is_occupied():
                        return True, [self.spots[c][sp]]
            for c in range(self.ncols):
                for sp in range(self.nspots // 4 * 3, self.nspots):
                    if not self.spots[c][sp].is_occupied():
                        return True, [self.spots[c][sp]]
        elif size == Size.large:
            for c in range(self.ncols):
                for sp in range(self.nspots // 4 * 3, self.nspots):
                    if not self.spots[c][sp].is_occupied():
                        return True, [self.spots[c][sp]]
            for c in range(self.ncols):
                for sp in range(self.nspots // 4 - 5):
                    if not self.spots[c][sp].is_occupied() and \
                            not self.spots[c][sp + 1].is_occupied() and \
                            not self.spots[c][sp + 2].is_occupied() and \
                            not self.spots[c][sp + 3].is_occupied() and \
                            not self.spots[c][sp + 4].is_occupied():
                        return (True,
                                [self.spots[c][sp],
                                 self.spots[c, sp + 1],
                                 self.spots[c, sp + 2],
                                 self.spots[c, sp + 3],
                                 self.spots[c, sp + 4]])
        return False, []


class Spot(object):
    def __init__(self, lv: int, c: int, sp: int, size: Size, *args, **kwargs):
        self.lv, self.c, self.sp, self.size = lv, c, sp, size
        self.vehicle = None
        return super().__init__(*args, **kwargs)

    def is_occupied(self):
        return self.vehicle is None

    def fit(self, size: Size):
        return size.value <= self.size.value

    def park(self, vehicle: Vehicle):
        vehicle.occupation.append(self)
        self.vehicle = vehicle

    def remove(self, vehicle: Vehicle):
        self.vehicle = None
