import vk

def get_access_token():
    #https://oauth.vk.com/authorize?client_id=6163745&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token
    return 'bf1321eeb62bd79cd50467f03963e462e3aa388612c680e48bf866b68cb7c6253bf58f11a74c53069f634'

def get_friends_list():
    # TODO: сходить Вк и получить список друзей аккаунта из credentials
    friends = []

    session = vk.Session(access_token=get_access_token())
    api = vk.API(session)

    id_friends = api.friends.get()
    for id_friend in id_friends:
        friends.append(api.users.get(user_ids=id_friend)[0])
    
    return friends

def ouptut_friends(friends):
    # TODO: вывести список друзей в консоль
    for friend in friends:
        print(friend.get('last_name'), friend.get('first_name'), 'id' + str(friend.get('uid')))

if __name__ == '__main__':
    friends = get_friends_list()
    ouptut_friends(friends)
