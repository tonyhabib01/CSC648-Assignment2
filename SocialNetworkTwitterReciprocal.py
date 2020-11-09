import networkx as nx
import matplotlib.pyplot as plt
import csv


class User:
    def __init__(self, parent_name, child_name):
        self.parent_name = parent_name
        self.child_name = child_name

    def __repr__(self):
        return self.child_name


def csv_to_list(cv_file_name):
    node_list = []
    with open(cv_file_name, newline='') as csv_file:
        spam_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
        for row in spam_reader:
            if row[0] == '"Name";"Friend-Id";"ScreenName";"Followers"':  # checking if the row is the column header and skip it
                continue
            node_list.append(tuple(row[0].split(';')))

    return node_list


def list_to_user(node_list):
    users = []
    for i in node_list:
        users.append(User(i[0], i[2]))
    return users


def create_edges(users):
    edges = []
    j = 0  # iterator for the parent node
    for i in range(0, len(users)):
        if users[i].parent_name is None:
            continue
        elif users[i].parent_name != users[j].child_name:
            while users[i].parent_name != users[j].child_name:  # this is in case the next user doesn't have any nodes
                j += 1
            edges.append((users[j], users[i]))
        else:
            edges.append((users[j], users[i]))
    return edges


if __name__ == "__main__":

    list_nodes = csv_to_list('data_twitter.csv')
    list_nodes = list_nodes[0:28]  # Just to minimize my list for visualization
    users = list_to_user(list_nodes)

    root_user = User(None, '"Juliensthoughtz"')
    users.insert(0, root_user)

    edges = create_edges(users)

    print("\nNumber of users:", len(users))
    print("\nThe users are: ")
    for user in users:
        print(user, end=", ")
    print("\n\nNode Edges:")
    for edge in edges:
        print(edge)

    G = nx.Graph()
    G.add_nodes_from(users)  # add his distances account
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True)
    plt.show()
