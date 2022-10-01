from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    users = []
    gather = data['messages']
    for i in range(len(gather)):
        gatherTwo = gather[i].items()
        for k, v in gatherTwo:
            if k == 'actor_id' or k == 'from_id':
                users.append(v)
    separateUsers = set(users)
    return list(separateUsers)

data1 = read_data('data/result.json')
print(find_all_users_name(data1))