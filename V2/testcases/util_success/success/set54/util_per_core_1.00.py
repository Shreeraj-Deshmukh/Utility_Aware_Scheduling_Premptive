"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199992, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199992, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.898582, 'e_o_k': [0.235703, 0.188562, 0.150850, 0.120680, 0.096544, 0.077235], 'p_i': 10, 'u_i': 4.3896},
        {'id': 1, 'e_m': 6.054830, 'e_o_k': [0.615328, 0.492263, 0.393810, 0.315048], 'p_i': 20, 'u_i': 4.5380},
        {'id': 2, 'e_m': 8.882383, 'e_o_k': [0.722286, 0.577829, 0.462263, 0.369810, 0.295848, 0.236679], 'p_i': 40, 'u_i': 2.5931},
        {'id': 3, 'e_m': 31.602698, 'e_o_k': [5.267116, 4.213693], 'p_i': 80, 'u_i': 2.1006},
        {'id': 4, 'e_m': 1.098905, 'e_o_k': [0.089359, 0.071487, 0.057190, 0.045752, 0.036602, 0.029281], 'p_i': 20, 'u_i': 1.6702},
        {'id': 5, 'e_m': 6.739507, 'e_o_k': [1.123251, 0.898601], 'p_i': 40, 'u_i': 4.1560},
        {'id': 6, 'e_m': 1.622012, 'e_o_k': [0.131897, 0.105517, 0.084414, 0.067531, 0.054025, 0.043220], 'p_i': 10, 'u_i': 3.0539},
        {'id': 7, 'e_m': 8.093457, 'e_o_k': [0.995097, 0.796078, 0.636862], 'p_i': 20, 'u_i': 4.7065},
    ]
    B_BUDGET = 239.199992
    return processors, tasks, B_BUDGET
