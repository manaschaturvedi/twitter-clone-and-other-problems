"""
Write a function that reads from chats.txt and returns the 3 most active users in the
conversation.
"""

def most_active_users():
    all_users = {}
    with open('chats.txt') as f:
        for line in f:
            name = line[line.find("<")+1:line.find(">")]
            if name in all_users:
                all_users[name] += 1
            else:
                all_users[name] = 1
    del all_users['']

    return sorted(all_users, key=all_users.get, reverse=True)[:3]

print(most_active_users())