"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760005, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760005, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.095856, 'e_o_k': [0.009741, 0.007793, 0.006235, 0.004988], 'p_i': 10, 'u_i': 3.7146},
        {'id': 1, 'e_m': 3.478715, 'e_o_k': [0.427711, 0.342169, 0.273735], 'p_i': 20, 'u_i': 2.7971},
        {'id': 2, 'e_m': 0.600593, 'e_o_k': [0.073843, 0.059075, 0.047260], 'p_i': 40, 'u_i': 1.6396},
        {'id': 3, 'e_m': 7.078395, 'e_o_k': [0.870295, 0.696236, 0.556988], 'p_i': 80, 'u_i': 4.1445},
        {'id': 4, 'e_m': 2.612347, 'e_o_k': [0.265482, 0.212386, 0.169909, 0.135927], 'p_i': 20, 'u_i': 4.6205},
        {'id': 5, 'e_m': 10.892727, 'e_o_k': [0.885760, 0.708608, 0.566887, 0.453509, 0.362807, 0.290246], 'p_i': 80, 'u_i': 1.3665},
        {'id': 6, 'e_m': 0.055017, 'e_o_k': [0.005591, 0.004473, 0.003578, 0.002863], 'p_i': 20, 'u_i': 3.3652},
        {'id': 7, 'e_m': 0.869133, 'e_o_k': [0.077564, 0.062051, 0.049641, 0.039713, 0.031770], 'p_i': 20, 'u_i': 2.1692},
    ]
    B_BUDGET = 71.760005
    return processors, tasks, B_BUDGET
