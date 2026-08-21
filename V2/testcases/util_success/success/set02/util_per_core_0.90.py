"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280023, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280023, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.601104, 'e_o_k': [0.266851, 0.213481], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 4.401086, 'e_o_k': [0.357882, 0.286305, 0.229044, 0.183235, 0.146588, 0.117271], 'p_i': 20, 'u_i': 3.2251},
        {'id': 2, 'e_m': 14.802543, 'e_o_k': [1.819985, 1.455988, 1.164790], 'p_i': 40, 'u_i': 4.0273},
        {'id': 3, 'e_m': 33.521202, 'e_o_k': [4.121459, 3.297167, 2.637734], 'p_i': 80, 'u_i': 2.2476},
        {'id': 4, 'e_m': 10.842980, 'e_o_k': [1.101929, 0.881543, 0.705234, 0.564188], 'p_i': 80, 'u_i': 1.3199},
        {'id': 5, 'e_m': 1.033732, 'e_o_k': [0.084060, 0.067248, 0.053798, 0.043039, 0.034431, 0.027545], 'p_i': 10, 'u_i': 4.7520},
        {'id': 6, 'e_m': 2.969240, 'e_o_k': [0.264985, 0.211988, 0.169590, 0.135672, 0.108538], 'p_i': 20, 'u_i': 3.4892},
        {'id': 7, 'e_m': 4.867685, 'e_o_k': [0.811281, 0.649025], 'p_i': 20, 'u_i': 1.4050},
    ]
    B_BUDGET = 215.280023
    return processors, tasks, B_BUDGET
