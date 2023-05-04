import random
from my_queue import Queue
from Client import Client
from Stylist import Stylist


def simulate_mani_salon(num_minutes, chance):
    stylist_1 = Stylist()
    stylist_2 = Stylist(exp=2)
    queue = Queue()
    total_time, total_clients = 0, 0

    for cur_minute in range(num_minutes):
        if random.random() < chance:
            new_client = Client(cur_minute)
            queue.enqueue(new_client)
            print('queued a new client with {} steps mani'.format(new_client.get_steps()))

        if not stylist_1.busy() and not queue.is_empty():
            new_client = queue.dequeue()
            stylist_1.start_next(new_client)
            total_clients += 1
            total_time += new_client.waiting_time(cur_minute)
            print('started mani with {} steps'.format(new_client.get_steps()))
        elif not stylist_2.busy() and not queue.is_empty():
            new_client = queue.dequeue()
            stylist_2.start_next(new_client)
            total_clients += 1
            total_time += new_client.waiting_time(cur_minute)
            print('started mani with {} steps'.format(new_client.get_steps()))

        print("Time: {} minutes, queued clients: {}".format(cur_minute, queue.size()))
        print(str(stylist_1))
        print(str(stylist_2))

        if cur_minute % 20 == 0: 
            stylist_1.tick()
            stylist_2.tick()

    print(f"Average waiting time: {total_time / total_clients}, {total_clients}")


if __name__ == "__main__":
    simulate_mani_salon(600, 0.05)
