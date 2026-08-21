"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279997, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279997, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.257912, 'e_o_k': [0.112260, 0.089808, 0.071846, 0.057477, 0.045982], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 3.633708, 'e_o_k': [0.295481, 0.236385, 0.189108, 0.151286, 0.121029, 0.096823], 'p_i': 20, 'u_i': 1.1622},
        {'id': 2, 'e_m': 14.305602, 'e_o_k': [1.758885, 1.407108, 1.125687], 'p_i': 40, 'u_i': 4.1752},
        {'id': 3, 'e_m': 34.988387, 'e_o_k': [3.555730, 2.844584, 2.275667, 1.820534], 'p_i': 80, 'u_i': 1.9420},
        {'id': 4, 'e_m': 0.008243, 'e_o_k': [0.001374, 0.001099], 'p_i': 10, 'u_i': 2.5093},
        {'id': 5, 'e_m': 8.719411, 'e_o_k': [1.072059, 0.857647, 0.686118], 'p_i': 80, 'u_i': 3.6510},
        {'id': 6, 'e_m': 1.625938, 'e_o_k': [0.165238, 0.132190, 0.105752, 0.084602], 'p_i': 10, 'u_i': 3.1983},
        {'id': 7, 'e_m': 17.004711, 'e_o_k': [1.728121, 1.382497, 1.105997, 0.884798], 'p_i': 40, 'u_i': 4.3627},
    ]
    B_BUDGET = 215.279997
    return processors, tasks, B_BUDGET
