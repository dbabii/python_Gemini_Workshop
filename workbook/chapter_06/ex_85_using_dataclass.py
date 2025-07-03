import dataclasses

@dataclasses.dataclass
class Point:
    x: int
    y: int
# create an instance
p = Point(10, 20)
print(p)
# compare instances
p2 = Point(x=10, y=20)
print(p == p2)

# serialize the data
dataclasses.asdict(p)
