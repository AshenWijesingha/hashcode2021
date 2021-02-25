# hello

from hash_code_parser import *
from pprint import pprint


def solve(input_file_name):
    problem = parse_file(input_file_name)
    # pprint(problem)
    output = create_streets(
        problem["intersections_in"],
        int(problem["duration"]),
        problem["streets"],
        problem["black_list"],
    )
    with open("output_" + input_file_name, "w") as output_file:
        output_file.write(output)


def create_streets(intersections, time, streets_dict, blacklist):
    max_time = min(10, time)
    res = ""
    inter_count = 0
    for inter in intersections.items():
        if len(inter[1]) == 1:
            res += inter[0] + "\n"
            res += "1\n" + inter[1][0] + " " + str(time) + "\n"
            inter_count += 1
        else:
            streets = sorted_streets(inter[1], streets_dict)
            num_streets = len(inter[1])
            streets_time = [
                i
                + " "
                + str(1)
                for acc, i in enumerate(streets)
                if round(max_time - max_time * (acc / num_streets)) != 0
                and i not in blacklist
            ]
            if len(streets_time) > 0:
                res += inter[0] + "\n"
                res += str(len(streets_time)) + "\n" + "\n".join(streets_time) + "\n"
                inter_count += 1
    res = str(inter_count) + "\n" + res
    return res


def sorted_streets(streets, streets_dict):
    return sorted(
        streets,
        key=lambda s: streets_dict[s]["nb_use"] / streets_dict[s]["L"],
        reverse=True,
    )


def main():
    for l in "abcdef":
        solve(l + ".txt")


def test_():
    # solve("a.txt")
    pprint(parse_file('b.txt'))


if __name__ == "__main__":
    # main()
    test_()
