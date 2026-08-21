"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400009, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.400009, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.505787, 'e_o_k': [0.158058, 0.094835], 'p_i': 10, 'u_i': 2.8589},
        {'id': 1, 'e_m': 0.195219, 'e_o_k': [0.049801, 0.029880, 0.017928], 'p_i': 20, 'u_i': 2.7598},
        {'id': 2, 'e_m': 10.184228, 'e_o_k': [3.182571, 1.909543], 'p_i': 40, 'u_i': 2.0735},
        {'id': 3, 'e_m': 6.561179, 'e_o_k': [1.376456, 0.825873, 0.495524, 0.297314, 0.178389, 0.107033], 'p_i': 80, 'u_i': 3.6242},
        {'id': 4, 'e_m': 4.539403, 'e_o_k': [1.418563, 0.851138], 'p_i': 20, 'u_i': 2.1240},
        {'id': 5, 'e_m': 6.765491, 'e_o_k': [1.554571, 0.932742, 0.559645, 0.335787], 'p_i': 80, 'u_i': 2.2796},
        {'id': 6, 'e_m': 1.084629, 'e_o_k': [0.235216, 0.141130, 0.084678, 0.050807, 0.030484], 'p_i': 20, 'u_i': 4.8637},
        {'id': 7, 'e_m': 0.372698, 'e_o_k': [0.095076, 0.057046, 0.034227], 'p_i': 10, 'u_i': 2.9768},
    ]
    B_BUDGET = 110.400009
    return processors, tasks, B_BUDGET
