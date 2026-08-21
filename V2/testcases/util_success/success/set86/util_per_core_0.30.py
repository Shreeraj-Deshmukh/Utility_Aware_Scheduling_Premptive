"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759988, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759988, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.075332, 'e_o_k': [0.009262, 0.007410, 0.005928], 'p_i': 10, 'u_i': 2.4144},
        {'id': 1, 'e_m': 0.310388, 'e_o_k': [0.051731, 0.041385], 'p_i': 20, 'u_i': 2.6559},
        {'id': 2, 'e_m': 1.785569, 'e_o_k': [0.159350, 0.127480, 0.101984, 0.081587, 0.065270], 'p_i': 40, 'u_i': 2.8681},
        {'id': 3, 'e_m': 10.457921, 'e_o_k': [1.742987, 1.394390], 'p_i': 80, 'u_i': 1.8896},
        {'id': 4, 'e_m': 0.826293, 'e_o_k': [0.073741, 0.058993, 0.047194, 0.037755, 0.030204], 'p_i': 20, 'u_i': 1.6645},
        {'id': 5, 'e_m': 0.437800, 'e_o_k': [0.039071, 0.031257, 0.025005, 0.020004, 0.016003], 'p_i': 40, 'u_i': 1.3774},
        {'id': 6, 'e_m': 2.417519, 'e_o_k': [0.402920, 0.322336], 'p_i': 80, 'u_i': 1.9412},
        {'id': 7, 'e_m': 25.528435, 'e_o_k': [4.254739, 3.403791], 'p_i': 80, 'u_i': 2.2237},
    ]
    B_BUDGET = 71.759988
    return processors, tasks, B_BUDGET
