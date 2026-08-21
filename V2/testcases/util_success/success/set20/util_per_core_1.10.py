"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119986, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119986, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.155876, 'e_o_k': [0.359313, 0.287450], 'p_i': 10, 'u_i': 4.3950},
        {'id': 1, 'e_m': 8.500601, 'e_o_k': [0.758621, 0.606897, 0.485517, 0.388414, 0.310731], 'p_i': 20, 'u_i': 2.5526},
        {'id': 2, 'e_m': 7.074209, 'e_o_k': [0.718924, 0.575139, 0.460111, 0.368089], 'p_i': 40, 'u_i': 1.4385},
        {'id': 3, 'e_m': 25.107317, 'e_o_k': [3.086965, 2.469572, 1.975658], 'p_i': 80, 'u_i': 4.9656},
        {'id': 4, 'e_m': 4.442325, 'e_o_k': [0.361235, 0.288988, 0.231190, 0.184952, 0.147962, 0.118370], 'p_i': 10, 'u_i': 1.9844},
        {'id': 5, 'e_m': 9.427778, 'e_o_k': [1.571296, 1.257037], 'p_i': 40, 'u_i': 2.5062},
        {'id': 6, 'e_m': 29.460538, 'e_o_k': [2.395633, 1.916506, 1.533205, 1.226564, 0.981251, 0.785001], 'p_i': 80, 'u_i': 1.0877},
        {'id': 7, 'e_m': 0.205019, 'e_o_k': [0.018297, 0.014637, 0.011710, 0.009368, 0.007494], 'p_i': 10, 'u_i': 1.1221},
    ]
    B_BUDGET = 263.119986
    return processors, tasks, B_BUDGET
