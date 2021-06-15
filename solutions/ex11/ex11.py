class Node:
    def __init__(self, data, positive_child=None, negative_child=None):
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child


class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    def __init__(self, root):
        self.root = root

        self.tmp_root = root
        self.illness = root  # default at the start
        self.all_illnesses_list = []
        self.path = []

    def get_root(self):
        return self.root

    def check_if_has_children(self, node):
        if node.positive_child is None and node.negative_child is None:
            return False
        return True

    def diagnose(self, symptoms):
        # base case
        if not self.check_if_has_children(self.illness):
            return self.illness.data
        if self.illness.data in symptoms:
            self.illness = self.illness.positive_child
        else:
            self.illness = self.illness.negative_child
        self.diagnose(symptoms)
        final_illness = self.illness.data
        return final_illness

    def calculate_success_rate(self, records):
        num_of_success = 0
        for record in records:
            self.illness = self.get_root()
            symptoms = record.symptoms
            result_diagnose = self.diagnose(symptoms)
            if result_diagnose == record.illness:
                num_of_success += 1
        average = num_of_success / len(records)
        return average

    def all_illnesses_helper(self, prev_node):
        """
        this is an helper method for all_illness method.
        its working by first checking recursively all the positive (YES) nodes, and counting how much the illness
        have been found. same thing with the negative (NO) nodes.
        :param prev_node: the previous node, keeping tracks which father of which node.
        :type prev_node: node object
        :return:
        """
        # base case
        if not self.check_if_has_children(self.illness):
            for illness in self.all_illnesses_list:
                if self.illness.data == illness[0]:  # checking if illness already in list
                    illness[1] += 1
                    return
            self.all_illnesses_list.append([self.illness.data, 1])  # appending the leaf node
            return

        self.illness = self.illness.positive_child  # checking only positive nodes
        self.all_illnesses_helper(self.illness)

        self.illness = prev_node
        self.illness = self.illness.negative_child  # checking only negative nodes
        self.all_illnesses_helper(self.illness)

    def sort_all_illnesses(self):
        """
        this list will sort the list of all illnesses by putting in the first index-
        the highest founded illness in tree, and the next highest and so on.
        it will first create a list and append to it the number of times (call it x) an illness appeared in the tree.
        then, it will check which illness is matched with this x, and also check if this-
        illness is not already sorted, because sometimes illnesses can be found the same
        amount of times, and append it to a new list.
        :return:
        """
        sorted_list = []
        number_found_of_illnesses = sorted([illness[1] for illness in self.all_illnesses_list], reverse=True)
        for time in number_found_of_illnesses:
            for illness in self.all_illnesses_list:
                if illness[1] == time and illness not in sorted_list:
                    sorted_list.append(illness)
                    break
        # removing the amount of times each illness has been found
        self.all_illnesses_list = [i[0] for i in sorted_list]

    def all_illnesses(self):
        self.illness = self.get_root()
        self.all_illnesses_helper(self.root)
        self.sort_all_illnesses()
        return self.all_illnesses_list

    def paths_to_illness_helper(self, path, illness, prev_node):
        """
        this method basically works like all_illness_helper method, but with
        logging the path with true or false.
        :param path: the true false path
        :param illness: which illness path to find
        :param prev_node: previous node
        :return: recursive
        """
        # base case
        if not self.check_if_has_children(self.illness) and self.illness.data == illness:
            self.path.append(path)
            return
        if not self.check_if_has_children(self.illness):
            return
        self.illness = self.illness.positive_child
        self.paths_to_illness_helper(path + [True], illness, self.illness)

        self.illness = prev_node
        self.illness = self.illness.negative_child
        self.paths_to_illness_helper(path + [False], illness, self.illness)
        return

    def paths_to_illness(self, illness):
        self.illness = self.get_root()
        self.path = []
        self.paths_to_illness_helper([], illness, self.root)
        return self.path


def build_tree_helper(root, symptoms, prev_node):
    pass


def build_tree(records, symptoms):
    root = Node(symptoms[0])  # first index is always the root
    build_tree_helper(root, symptoms, root)

























def optimal_tree(records, symptoms, depth):
    pass


if __name__ == "__main__":

    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           headache
    #   Yes /     \ No   Yes /      \ No
    # influenza   cold    cold       healthy

    # flu_leaf = Node("influenza", None, None)
    # cold_leaf = Node("cold", None, None)
    # inner_vertex = Node("fever", flu_leaf, cold_leaf)
    # healthy_leaf = Node("healthy", None, None)
    # headache_leaf = Node("headache", cold_leaf, healthy_leaf)
    # # root = Node("cough", inner_vertex, healthy_leaf)
    #
    # diagnoser = Diagnoser(root)
    #
    # # Simple test
    # diagnosis = diagnoser.diagnose(["cough"])
    # if diagnosis == "cold":
    #     print("Test passed")
    # else:
    #     print("Test failed. Should have printed cold, printed: ", diagnosis)
    #
    # # Add more tests for sections 2-7 here.
    #
    # # records test
    # record1 = Record("cold", [inner_vertex, healthy_leaf])
    # record2 = Record("cough", [inner_vertex, healthy_leaf])
    # record3 = Record("cold", [inner_vertex, healthy_leaf])
    #
    # calculate_rate = diagnoser.calculate_success_rate([record1, record2, record3])
    # if calculate_rate == 2 / 3:
    #     print("Records test passed")
    # else:
    #     print("Records test failed, printed:", calculate_rate)
    #
    # # all illnesses test
    # all_illnesses_test_list = [['cold', 2], ['influenza', 1], ['healthy', 1]]
    # all_illnesses = diagnoser.all_illnesses()
    # if all_illnesses == all_illnesses_test_list:
    #     print("All illnesses method passed")
    # else:
    #     print("All illnesses method failed, printed:", all_illnesses)
    #
    # # paths to illness test
    # paths = diagnoser.paths_to_illness("cold")
    # if paths == [[True, False], [False, True]]:
    #     print("Paths to illness method passed.")
    # else:
    #     print("Paths to illness method failed, printed:", paths)
    pass