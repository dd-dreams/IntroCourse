###############################
# LOGIN: avinoam_nukrai
# NAME: Avinoam Nukrai
# ID: 206997132
# EX: ex11 intro2cs 2019 - 2020
# CONSULTATION: I consulted with maoratar and
# yonigaz1 regarding functions number 1, 5, 6.
###############################


from itertools import combinations


class Node:
    """The current class contains __init__ with data members of each node in the
    program each node vertex has two sons unless it is a leaf"""

    def __init__(self, data, positive_child=None, negative_child=None):
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child


class Record:
    """this class is contains __init__ with the data members of each record"""

    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    """the current function is opening a file and creates the records list
    in the program"""
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    """this class is the main class of the program. she contains __init__ that
    creates a data member which is the root of the tree. Then, by a few
    simple methods, the department is able to diagnose the correct disease,
    calculate the chances of success of the diagnosis, and calculate all
    possible combinations of symptoms for diagnosing a particular disease."""

    def __init__(self, root):
        """creates the root of the tree"""
        self.root = root

    def diagnose_helper(self, update_root, symptoms):
        """The current function gets a list of symptoms and root causes. The
        function travels the data to the root of each read and checks whether
        its symptom is within the list of symptoms or not."""
        if update_root.positive_child is None:
            return update_root.data
        if update_root.data in symptoms:
            return self.diagnose_helper(update_root.positive_child, symptoms)
        if update_root.data not in symptoms:
            return self.diagnose_helper(update_root.negative_child, symptoms)

    def diagnose(self, symptoms):
        """The current function receives a list of symptoms "and diagnoses" for
        which disease is appropriate for them according to the decision
        tree that the class is keeping in self."""
        return self.diagnose_helper(self.root, symptoms)

    def calculate_success_rate(self, records):
        """The current function receives a list of records and calculates the
        number of successes in diagnosing illnesses compared to
        the number of records"""
        sum_of_sec = 0
        for record in records:
            if self.diagnose(record.symptoms) == record.illness:
                sum_of_sec += 1
        return sum_of_sec / len(records)

    def check_if_data_exist(self, data, lst_of_illnesses):
        """The current function receives a record of data and checks whether
        it is in one of the disease list pairs when each pair first contains
        the disease name and the number of times it appeared on the record"""
        for couple in lst_of_illnesses:
            if data == couple[0]:
                return couple
        return False

    def compare_two_couple(self, couple1, couple2):
        """The function accepts two pairs of diseases and compares them and
        thus helps us to know whether they are equal, or different
        from each other."""
        if couple1 > couple2:
            return 1
        elif couple2 < couple1:
            return -1
        return 0

    def all_illnesses_helper(self, root, lst_of_illnesses):
        """this method gets root and illnesses list and the method is update
        the list of illnesses in each case the root.data is in the list or not
        in the list. the function returns the update list of illnesses"""
        if root.positive_child is None:
            couple = self.check_if_data_exist(root.data, lst_of_illnesses)
            if couple:
                couple[1] += 1
            else:
                if root.data is not None:
                    lst_of_illnesses.append([root.data, 1])
            return
        self.all_illnesses_helper(root.positive_child, lst_of_illnesses)
        self.all_illnesses_helper(root.negative_child, lst_of_illnesses)

    def all_illnesses(self):
        """this method is returns the list of illnesses after sorting it from
        the highest amount of existence of the illness"""
        if self.root is None:
            return []
        lst_ill = []
        self.all_illnesses_helper(self.root, lst_ill)
        lst_ill.sort(key=lambda couple: -couple[1])
        final_list = []
        for sub_list in lst_ill:
            final_list.append(sub_list[0])
        return final_list

    def paths_helper(self, illness, root, path, paths_lst):
        """the method gets illness, root, path and path list. the function
        by two recursion calling, is calculates all the paths to the current
        illness that she gets with a bools value and returning it"""
        if root.positive_child is None:
            if root.data == illness:
                paths_lst.append(path)
            return
        self.paths_helper(illness, root.positive_child, path + [True],
                          paths_lst)
        self.paths_helper(illness, root.negative_child, path + [False],
                          paths_lst)
        return paths_lst

    def paths_to_illness(self, illness):
        """the method gets an illness and returns all the path to that illness"""
        path_lst = []
        self.paths_helper(illness, self.root, [], path_lst)
        return path_lst


##########################----BUILD TREE FUNCTIONS-----########################


def build_tree(records, symptoms):
    """The present function builds a tree whose root is the first symptom on
    the list and its sons constitute the other symptoms on the final leaf which
    is the final disease corresponding to the same path and return the tree root"""
    if len(symptoms) == 0:
        if len(records) == 0:
            root = Node(None)
        else:
            new_records = []
            for record in records:
                new_records.append(record.illness)
            illness = max(new_records, key=new_records.count)
            root = Node(illness)
    else:
        root = Node(symptoms[0])
        tree_helper(records, symptoms, root)
    return root


def tree_helper(records, symptoms, node):
    """The current function builds a tree whose depth is equal to the list of
    symptoms and each parallel row of vertices contains the same symptom.
    When you reach the end of the symptom list, the function
    adds a leaf to each track"""
    if len(symptoms) == 1:
        leaf_builder(records, symptoms, node)
    else:
        node.positive_child = Node(symptoms[1])
        update_illnesses_lst = nodes_candidates(records, symptoms[0], "y")
        tree_helper(update_illnesses_lst, symptoms[1:], node.positive_child)
        node.negative_child = Node(symptoms[1])
        update_illnesses_lst = nodes_candidates(records, symptoms[0], "n")
        tree_helper(update_illnesses_lst, symptoms[1:], node.negative_child)


def nodes_candidates(records, symptom, run_side):
    """The current function updates the record list according to each symptom
    from the symptom list in the symptoms of each record individually"""
    update_records_lst = records[:]
    for record in records:
        if run_side == "y":
            if symptom not in record.symptoms:
                update_records_lst.remove(record)
        if run_side == "n":
            if symptom in record.symptoms:
                update_records_lst.remove(record)
    return update_records_lst


def final_candidate(records):
    """The current function returns the disease with the highest
    incidence in the list of all diseases from the record"""
    records_lst = []
    for record in records:
        records_lst.append(record.illness)
    if records_lst == []:
        return None
    illness = max(records_lst, key=records_lst.count)
    return illness


def leaf_builder_helper(records, symptom, answer):
    """The current function calculates the candidates and returns the most
    desired candidate according to what is defined in the exercise"""
    candidates = nodes_candidates(records, symptom, answer)
    illness = final_candidate(candidates)
    return illness


def leaf_builder(records, symptoms, node):
    """The current function produces the leaf with the desired disease"""
    y_illness = leaf_builder_helper(records, symptoms[0], "y")
    n_illness = leaf_builder_helper(records, symptoms[0], "n")
    node.positive_child = Node(y_illness)
    node.negative_child = Node(n_illness)


def optimal_tree(records, symptoms, depth):
    """The current function gets a list of records, symptoms and tree depth.
    The function returns the tree with the highest success rate that
    always asks about a subset of symptoms that is
    equal in length to the tree depth"""
    max_success = 0
    optimal_root = Node(None)
    combinations_symptoms = combinations(symptoms, depth)
    for lst_symptom in combinations_symptoms:
        tree = build_tree(records, lst_symptom)
        diagnoser_obj = Diagnoser(tree)
        success_rate = diagnoser_obj.calculate_success_rate(records)
        if success_rate > max_success:
            max_success = success_rate
            optimal_root = tree
    return optimal_root
