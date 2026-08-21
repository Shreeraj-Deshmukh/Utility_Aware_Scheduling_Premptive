"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.304154, 'e_o_k': [0.062327, 0.049861, 0.039889], 'p_i': 10, 'u_i': 2.5184},
        {'id': 1, 'e_m': 2.335008, 'e_o_k': [0.347306, 0.277845, 0.222276, 0.177821, 0.142257], 'p_i': 20, 'u_i': 4.2996},
        {'id': 2, 'e_m': 3.020032, 'e_o_k': [0.409298, 0.327439, 0.261951, 0.209561, 0.167649, 0.134119], 'p_i': 40, 'u_i': 3.3901},
        {'id': 3, 'e_m': 0.952703, 'e_o_k': [0.129118, 0.103294, 0.082635, 0.066108, 0.052887, 0.042309], 'p_i': 80, 'u_i': 2.3217},
        {'id': 4, 'e_m': 10.325824, 'e_o_k': [1.748954, 1.399163, 1.119331, 0.895464], 'p_i': 80, 'u_i': 2.1118},
        {'id': 5, 'e_m': 2.908145, 'e_o_k': [0.492572, 0.394058, 0.315246, 0.252197], 'p_i': 80, 'u_i': 4.2305},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
