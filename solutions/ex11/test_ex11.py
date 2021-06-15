##############################################
#               Tester for ex11              #
##############################################
# Move ALL files to the same folder with ex11#
# then run pytest                            #
# Daniel Shookroun                           #
# daniel.shookroun@mail.huji.ac.il           #
##############################################

import ex11
from ex11 import Node, Diagnoser, Record, build_tree, optimal_tree, parse_data

# Manually build a simple tree.
#                cough
#          Yes /       \ No
#        fever           healthy
#   Yes /     \ No
# influenza   cold

flu_leaf = Node("influenza", None, None)
cold_leaf = Node("cold", None, None)
inner_vertex = Node("fever", flu_leaf, cold_leaf)
healthy_leaf = Node("healthy", None, None)
root = Node("cough", inner_vertex, healthy_leaf)

diagnoser = Diagnoser(root)

flu_leaf2 = Node("influenza", None, None)
cold_leaf2 = Node("cold", None, None)
hard_leaf2 = Node("hard influenza", None, None)
headache_node2 = Node("headache", hard_leaf2, flu_leaf2)
inner_vertex2 = Node("fever", headache_node2, cold_leaf2)
healthy_leaf2 = Node("healthy", None, None)
root2 = Node("cough", inner_vertex2, healthy_leaf2)

diagnoser2 = Diagnoser(root2)
# Manually build of diagnoser2.
#                          cough
#                    Yes /       \ No
#                  fever           healthy
#             Yes /     \ No
#            headache   cold
#       Yes /     \ No
# hard influenza influenza

flu_leaf3 = Node("influenza", None, None)
cold_leaf3 = Node("cold", None, None)
hard_leaf3 = Node("hard influenza", None, None)
headache_node3 = Node("headache", hard_leaf3, flu_leaf3)
inner_vertex3 = Node("fever", headache_node3, cold_leaf3)
healthy_leaf3 = Node("hard influenza", None, None)
root3 = Node("cough", inner_vertex3, healthy_leaf3)

diagnoser3 = Diagnoser(root3)
# Manually build of diagnoser3.
#                          cough
#                    Yes /       \ No
#                  fever       hard influenza
#             Yes /     \ No
#            headache   cold
#       Yes /     \ No
# hard influenza influenza

flu_leaf4 = Node("influenza", None, None)
cold_leaf4 = Node("cold", None, None)
hard_leaf4 = Node("hard influenza", None, None)
headache_node4 = Node("headache", hard_leaf4, flu_leaf4)
inner_vertex4 = Node("fever", headache_node4, cold_leaf4)
healthy_leaf4 = Node("influenza", None, None)
root4 = Node("cough", inner_vertex4, healthy_leaf4)

diagnoser4 = Diagnoser(root4)
# Manually build of diagnoser4.
#                          cough
#                    Yes /       \ No
#                  fever        influenza
#             Yes /     \ No
#            headache   cold
#       Yes /     \ No
# hard influenza influenza

flu_leaf5 = Node("influenza", None, None)
cold_leaf5 = Node("cold", None, None)
healthy_leaf5 = Node("influenza", None, None)
inner_vertex6 = Node("headache", cold_leaf5, healthy_leaf5)
inner_vertex5 = Node("headache", flu_leaf5, cold_leaf5)
root5 = Node("cough", inner_vertex5, inner_vertex6)

diagnoser5 = Diagnoser(root5)
# Manually build of diagnoser5.
#                          cough
#                    Yes /       \ No
#                     headache  headache
#             Yes /     \ No  Yes /     \ No
#           influenza  cold     cold    healthy

root6 = Node("cold", None, None)
diagnoser6 = Diagnoser(root6)


def test_diagnose1():
    assert "cold" == diagnoser.diagnose(["cough"])


def test_diagnose2():
    assert "influenza" == diagnoser2.diagnose(["cough", "fever"])


def test_success_rate1():
    records = [Record("influenza", ["cough", "fever"]), Record("healthy", []),
               Record('hard influenza', ["cough", "fever", "headache"])]
    assert 0.6666666666666666 == diagnoser.calculate_success_rate(records)


def test_success_rate2():
    records2 = [Record("influenza", ["cough", "fever"]), Record("healthy", []),
                Record('hard influenza', ["cough", "fever", "headache"])]
    assert 1.0 == diagnoser2.calculate_success_rate(records2)


def test_success_rate3():
    records3 = [Record("influenza", ["cough", "fever"]), Record("indigestion", ["stomachache"])]
    assert 0.5 == diagnoser2.calculate_success_rate(records3)


def test_all_illnesses1():
    result = diagnoser3.all_illnesses()
    assert "hard influenza" == result[0]


def test_paths_to_illness1():
    paths1 = diagnoser4.paths_to_illness('influenza')
    assert [[True, True, False], [False]] == paths1 or [[False], [True, True, False]] == paths1


def test_paths_to_illness2():
    paths2 = diagnoser4.paths_to_illness('cold')
    assert [[True, False]] == paths2


def test_paths_to_illness3():
    paths3 = diagnoser4.paths_to_illness('something_that_doesnt_exist')
    assert [] == paths3


def test_paths_to_illness4():
    paths4 = diagnoser6.paths_to_illness("cold")
    assert [] == paths4 or [[]] == paths4


def test_paths_to_illness5():
    paths5 = diagnoser2.paths_to_illness('healthy')
    assert [[False]] == paths5


def test_paths_to_illness6():
    paths6 = diagnoser5.paths_to_illness('cold')
    assert [[True, False], [False, True]] == paths6 or [[False, True], [True, False]] == paths6


def test_build_tree1():
    records = parse_data(r"tiny_data2.txt")
    tree1 = build_tree(records, ["headache", "fever"])

    assert "meningitis" == tree1.positive_child.positive_child.data
    assert "influenza" == tree1.positive_child.negative_child.data
    assert "cold" == tree1.negative_child.positive_child.data
    assert "healthy" == tree1.negative_child.negative_child.data


def test_build_tree2():
    records = parse_data(r"small_data1.txt")
    tree2 = build_tree(records, ["headache", "fever"])

    assert "influenza" == tree2.positive_child.positive_child.data
    assert "cold" == tree2.positive_child.negative_child.data
    assert "strep" == tree2.negative_child.positive_child.data
    assert "healthy" == tree2.negative_child.negative_child.data


def test_build_tree3():
    records = parse_data(r"medium_data1.txt")
    tree3 = build_tree(records, ["fever", "cough"])

    assert "influenza" == tree3.positive_child.positive_child.data
    assert "meningitis" == tree3.positive_child.negative_child.data
    assert "cold" == tree3.negative_child.positive_child.data
    assert "healthy" == tree3.negative_child.negative_child.data


def test_build_tree4():
    records = parse_data(r"medium_data2.txt")
    tree4 = build_tree(records, ["fever", "cough"])

    assert "influenza" == tree4.positive_child.positive_child.data
    assert "strep" == tree4.positive_child.negative_child.data
    assert "cold" == tree4.negative_child.positive_child.data
    assert "healthy" == tree4.negative_child.negative_child.data


def test_optimal_tree1():
    records = parse_data(r"test_optimal_tree1.txt")
    tree = optimal_tree(records, ["cough", "fever", "headache"], 2)

    assert "cough" == tree.data or "fever" == tree.data
    assert "cough" == tree.positive_child.data or "fever" == tree.positive_child.data


def test_optimal_tree2():
    records = parse_data(r"test_optimal_tree2.txt")
    tree = optimal_tree(records, ["cough", "fever", "headache"], 1)

    assert "fever" == tree.data or "headache" == tree.data


def test_optimal_tree3():
    records = parse_data(r"test_optimal_tree3.txt")
    tree = optimal_tree(records, ["fever", "cough", "headache"], 2)

    assert "influenza" == tree.positive_child.positive_child.data
    assert "meningitis" == tree.positive_child.negative_child.data
    assert "cold" == tree.negative_child.positive_child.data
    assert "healthy" == tree.negative_child.negative_child.data
