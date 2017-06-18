def load_balancer(config, service, instance_number):

    for i in range(instance_number):
        current_server_load = sorted([(sum(config[service].values()), service) for service in config])
        less_loaded_server = current_server_load[0][1]
        if service in config[less_loaded_server]:
            config[less_loaded_server][service] += 1
        else:
            config[less_loaded_server][service] = 1

    return config


if __name__ == '__main__':

    server_count = int(input("Please enter the number of servers"))
    config = {}

    for service_index in range(server_count):
        service = input("Enter name for server № {}".format(service_index + 1))
        config[service] = {}

    while True:
        service = input("Enter name for the service ")
        instance_number = int(input("Enter the number of instances"))
        print('New configuration looks like this :', load_balancer(config, service, instance_number))


