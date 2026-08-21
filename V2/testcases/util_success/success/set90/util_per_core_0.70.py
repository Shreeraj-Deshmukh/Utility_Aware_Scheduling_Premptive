"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439999, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439999, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.974488, 'e_o_k': [0.200659, 0.160527, 0.128422, 0.102738], 'p_i': 10, 'u_i': 1.1071},
        {'id': 1, 'e_m': 1.491006, 'e_o_k': [0.248501, 0.198801], 'p_i': 20, 'u_i': 4.7513},
        {'id': 2, 'e_m': 9.466188, 'e_o_k': [0.769759, 0.615807, 0.492646, 0.394117, 0.315293, 0.252235], 'p_i': 40, 'u_i': 2.4512},
        {'id': 3, 'e_m': 3.020587, 'e_o_k': [0.503431, 0.402745], 'p_i': 80, 'u_i': 1.4858},
        {'id': 4, 'e_m': 17.692328, 'e_o_k': [1.438681, 1.150945, 0.920756, 0.736605, 0.589284, 0.471427], 'p_i': 40, 'u_i': 3.8296},
        {'id': 5, 'e_m': 2.638675, 'e_o_k': [0.268158, 0.214526, 0.171621, 0.137297], 'p_i': 20, 'u_i': 2.8775},
        {'id': 6, 'e_m': 5.301814, 'e_o_k': [0.473151, 0.378521, 0.302817, 0.242253, 0.193803], 'p_i': 40, 'u_i': 4.5934},
        {'id': 7, 'e_m': 2.936032, 'e_o_k': [0.238748, 0.190999, 0.152799, 0.122239, 0.097791, 0.078233], 'p_i': 20, 'u_i': 1.6361},
    ]
    B_BUDGET = 167.439999
    return processors, tasks, B_BUDGET
