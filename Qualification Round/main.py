import sys


class Street:
    def __init__(self, text):
        self.start_intersection, self.end_intersection, self.name, self.time = text.split(' ')


class Intersection:
    def __init__(self, id):
        self.id = id
        self.incoming_streets = []

    def add_street(self, street):
        self.incoming_streets.append(street)


class Car:
    def __init__(self, text):
        self.nbr_streets, *self.text_streets = text.split(' ')


def read_file(file_name):
    file = open(file_name, "r")
    lines = [line.rstrip() for line in file.readlines()]
    file.close()

    instructions = lines.pop(0)

    return instructions, lines


def main():
    instructions, lines = read_file(sys.argv[1])

    duration, intersections_number, streets_number, cars_number, score = instructions.split(' ')

    streets = []
    intersections = {}
    paths = []

    for i in range(0, int(streets_number)):
        line = lines.pop(0)

        if not line.split(' ')[1] in intersections.keys():
            intersections[line.split(' ')[1]] = Intersection(line.split(' ')[1])
            intersections[line.split(' ')[1]].add_street(line.split(' ')[2])
        else:
            intersections[line.split(' ')[1]].add_street(line.split(' ')[2])
        streets.append(Street(line))

    for i in range(0, int(cars_number)):
        paths.append(Car(lines.pop(0)))

    file = open("result-" + sys.argv[1], "w")

    file.write(str(len(intersections.keys())) + "\n")
    for k, v in intersections.items():
        file.write(v.id + "\n")
        file.write(str(len(v.incoming_streets)) + "\n")
        for street in v.incoming_streets:
            file.write(street + " 1" + "\n")

    file.close()


if __name__ == "__main__":
    main()
