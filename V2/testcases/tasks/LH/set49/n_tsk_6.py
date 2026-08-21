"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.001301, 'e_o_k': [0.000494, 0.000395, 0.000316, 0.000253, 0.000202, 0.000162], 'p_i': 10, 'u_i': 2.0413},
        {'id': 1, 'e_m': 0.760011, 'e_o_k': [0.436072, 0.348858, 0.279086], 'p_i': 20, 'u_i': 1.2036},
        {'id': 2, 'e_m': 0.400720, 'e_o_k': [0.311671, 0.249337], 'p_i': 40, 'u_i': 1.4564},
        {'id': 3, 'e_m': 3.071005, 'e_o_k': [1.456439, 1.165151, 0.932121, 0.745697], 'p_i': 80, 'u_i': 1.4719},
        {'id': 4, 'e_m': 23.514057, 'e_o_k': [13.491672, 10.793338, 8.634670], 'p_i': 80, 'u_i': 1.0831},
        {'id': 5, 'e_m': 0.781522, 'e_o_k': [0.325479, 0.260383, 0.208307, 0.166645, 0.133316], 'p_i': 40, 'u_i': 3.5025},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
