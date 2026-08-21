"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.573715, 'e_o_k': [0.159365, 0.127492], 'p_i': 10, 'u_i': 2.0200},
        {'id': 1, 'e_m': 0.355799, 'e_o_k': [0.072910, 0.058328, 0.046662], 'p_i': 20, 'u_i': 3.9687},
        {'id': 2, 'e_m': 7.195452, 'e_o_k': [0.975184, 0.780147, 0.624118, 0.499294, 0.399435, 0.319548], 'p_i': 40, 'u_i': 2.3030},
        {'id': 3, 'e_m': 4.599977, 'e_o_k': [0.942618, 0.754095, 0.603276], 'p_i': 80, 'u_i': 2.6501},
        {'id': 4, 'e_m': 0.710090, 'e_o_k': [0.105618, 0.084494, 0.067595, 0.054076, 0.043261], 'p_i': 10, 'u_i': 1.7748},
        {'id': 5, 'e_m': 0.328872, 'e_o_k': [0.067392, 0.053913, 0.043131], 'p_i': 20, 'u_i': 3.9815},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
