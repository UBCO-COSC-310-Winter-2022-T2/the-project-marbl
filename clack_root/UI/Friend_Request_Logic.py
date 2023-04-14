class User:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.pending_requests = []

    def send_friend_request(self, other_user):
        if other_user in self.friends:
            print(f"{other_user.name} is already your friend.")
        elif other_user in self.pending_requests:
            print(f"A friend request to {other_user.name} is already pending.")
        else:
            other_user.pending_requests.append(self)
            print(f"Sent friend request to {other_user.name}.")

    def accept_friend_request(self, other_user):
        if other_user not in self.pending_requests:
            print(f"No pending friend request from {other_user.name}.")
        else:
            self.friends.append(other_user)
            other_user.friends.append(self)
            self.pending_requests.remove(other_user)
            print(f"You are now friends with {other_user.name}.")

    def reject_friend_request(self, other_user):
        if other_user not in self.pending_requests:
            print(f"No pending friend request from {other_user.name}.")
        else:
            self.pending_requests.remove(other_user)
            print(f"Rejected friend request from {other_user.name}.")

#Test the User class
# if __name__ == '__main__':
#     # Create some users
#     alice = User('Alice')
#     bob = User('Bob')
#     charlie = User('Charlie')

#     # Alice sends a friend request to Bob
#     alice.send_friend_request(bob)

#     # Bob accepts Alice's friend request
#     bob.accept_friend_request(alice)

#     # Alice tries to send another friend request to Bob
#     alice.send_friend_request(bob)

#     # Charlie sends a friend request to Bob
#     charlie.send_friend_request(bob)

#     # Bob rejects Charlie's friend request
#     bob.reject_friend_request(charlie)

#     # Alice and Bob are now friends
#     print(f"{alice.name}'s friends: {[f.name for f in alice.friends]}")
#     print(f"{bob.name}'s friends: {[f.name for f in bob.friends]}")