from ps1_partition import get_partitions
import time


def load_cows(filename):
    file = open(filename, "r")
    cow_dict = {}
    for line in file:
        line = line.strip("\n")
        line = line.split(",")
        cow_dict[line[0]] = int(line[1])
    file.close()
    return cow_dict


def greedy_cow_transport(cows, limit=10):
    cows_copy = sorted(cows, key=cows.get, reverse=True)
    result = []
    while len(cows_copy) > 0:
        totalWeight = 0
        trip = []
        for name in cows_copy[:]:
            if cows[name] + totalWeight <= limit:
                trip.append(name)
                totalWeight += cows[name]
                cows_copy.remove(name)
        result.append(trip)
    return result


def brute_force_cow_transport(cows, limit=10):
    result = []
    for partition in get_partitions(cows.keys()):
        score = []
        for trip in partition:
            totalWeight = 0
            for name in trip:
                totalWeight += cows[name]
            if totalWeight <= limit:
                score.append(1)
            else:
                score.append(0)
        if len(partition) == sum(score):
            result.append(partition)
    return result


def compare_cow_transport_algorithms():
    cows = load_cows("ps1_cow_data_2.txt")
    start = time.time()
    print(greedy_cow_transport(cows))
    end = time.time()
    print("Greedy cow transport time:", end - start)
    print("Number of trips: ", len(greedy_cow_transport(cows)))

    start = time.time()
    cows_list = brute_force_cow_transport(cows)
    test = {}
    for i, v in enumerate(cows_list):
        test[len(v)] = i
    minimum = min(test, key=test.get)
    print()
    print(cows_list[test[minimum]])
    end = time.time()
    print("Brute force cow transport time:", end - start)
    print("Number of trips:", minimum)


compare_cow_transport_algorithms()
