

players_items_chosen = []
players_pay = []
agents = []


class Agent:
    #def __init__(self):
    #    self.items_value = []

    def __init__(self, arr):
        self.items_value = arr

    #def __init__(self, agent:Agent):
    #    self = agent

    def value(self, option:int) -> float:
        return self.items_value[option]

def calculate_max_without_player_for_rest_of_items(player_already_chosen:int, item_chosen:int):
    item_index = 0
    items_sum = 0
    while item_index < len(agents):
        if item_chosen == item_index:
            item_index += 1
            continue
        player_index = 0
        max_value = 0
        while player_index < len(agents):
            if player_index == player_already_chosen:
                player_index += 1
                continue
            if max_value < agents[player_index].value(item_index):
                max_value = agents[player_index].value(item_index)
            player_index += 1
        
        item_index += 1
        items_sum += max_value
    
    return items_sum
            

def calculate_players_pay():
    index = 0
    while index < len(agents):
        current_item = players_items_chosen[index]
        current_player_value = agents[index].value(index)
        sum_without_player = calculate_max_without_player_for_rest_of_items(index,current_item)
        sum_with_player = get_max_for_items_without_index(index)
        players_pay.append(current_player_value + sum_with_player - sum_without_player)
        index += 1

def set_max_for_item():
    index = 0
    chosen_agents = [False]*len(agents)
    while index < len(agents):
        players_items_chosen.append(init_max_for_items(index,chosen_agents))
        chosen_agents[index] = True
        index += 1

def get_max_for_items_without_index(player_index_to_skip:int):
    index = 0
    sum_for_item = 0
    while index < len(agents):
        if player_index_to_skip == index:
            index += 1
            continue
        sum_for_item += get_max_for_item(index)
        index += 1
    return sum_for_item

def init_max_for_items(item_index:int, agent_chosen:list[bool]):
    index = 1
    agent_index = 0
    while index < len(agents):
        if agents[index-1].value(item_index) >= agents[index].value(item_index) and not agent_chosen[index-1]:
            agent_index = index-1

        elif not agent_chosen[index]:
            agent_index = index
        index += 1

    return agent_index

def get_max_for_item(item_index:int):
    index = 1
    agent_index = 0
    while index < len(agents):
        if agents[index-1].value(item_index) >= agents[index].value(item_index):
            agent_index = index-1

        else:
            agent_index = index
        index += 1

    return agent_index

def vcg(agents: list[Agent], num_options:int):
    set_max_for_item()
    calculate_players_pay()

    index = 0
    players_pay = []
    while index < len(agents):
        print("Agent #{} pays {}".format(index,players_pay[index]))
        index += 1

    run_additional_tests()

def run_additional_tests():
    print("TESTS")
    

if __name__ == "__main__":
    #option_num_str = input("Choose option number: ")
    #print("The chosen option is {}".format(option_num_str))
    #option_num = int(option_num_str)
    option_num = 4
    '''index = 0
    while index < option_num:
        agent_values_str = input("Enter Array (with seperator ',') ")
        agent_values = list(map(int,agent_values_str.split(",")))
        agent = Agent(agent_values)
        agents.append(agent)
    '''
    agents = [Agent([8,7,6,5]),Agent([6,5,4,3]),Agent([5,4,3,2]),Agent([4,3,2,1])]
    vcg(agents,option_num)