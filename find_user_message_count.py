from operator import countOf
from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """

    users = []
    gather = data['messages']
    for i in range(len(gather)):
        gatherTwo = gather[i].items()
        for k, v in gatherTwo:
            if k == 'actor_id' or k == 'from_id':
                users.append(v)

    # I took all user name
    usersTwo = []
    for i in range(len(users)):
        if not users[i] in usersTwo:
            usersTwo.append(users[i])           

    count = 1
    counter = []
    for k in range(len(usersTwo)):
        count = 0
        for l in range(len(users)):
            if usersTwo[k] == users[l]:
                count += 1
        counter.append(count)

    myDictionary = {}
    
    for i in range(len(users_id)):
        # print(users_id[i])
        myDictionary[users_id[i]] = counter[i]
    # myDictionary[users_id] = counter
    # myDictionary = {"users_id": "counter"}


    return myDictionary

data3 = find_user_message_count(read_data('data/result.json'), find_all_users_id(read_data('data/result.json')))
print(data3)


    # {
    #     "user3454554":25,
    #     "user454545":
    # }
    