"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120009, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120009, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.374531, 'e_o_k': [0.274406, 0.219525, 0.175620, 0.140496, 0.112397, 0.089917], 'p_i': 10, 'u_i': 2.6086},
        {'id': 1, 'e_m': 6.015121, 'e_o_k': [0.489130, 0.391304, 0.313043, 0.250434, 0.200348, 0.160278], 'p_i': 20, 'u_i': 1.1783},
        {'id': 2, 'e_m': 11.265679, 'e_o_k': [1.144886, 0.915909, 0.732727, 0.586182], 'p_i': 40, 'u_i': 4.9217},
        {'id': 3, 'e_m': 23.358960, 'e_o_k': [2.872003, 2.297603, 1.838082], 'p_i': 80, 'u_i': 3.2220},
        {'id': 4, 'e_m': 9.816335, 'e_o_k': [1.206926, 0.965541, 0.772433], 'p_i': 40, 'u_i': 4.7017},
        {'id': 5, 'e_m': 9.425137, 'e_o_k': [1.158828, 0.927063, 0.741650], 'p_i': 40, 'u_i': 4.3910},
        {'id': 6, 'e_m': 3.721238, 'e_o_k': [0.302599, 0.242079, 0.193663, 0.154931, 0.123944, 0.099156], 'p_i': 10, 'u_i': 2.8355},
        {'id': 7, 'e_m': 1.350012, 'e_o_k': [0.165985, 0.132788, 0.106230], 'p_i': 10, 'u_i': 3.6585},
    ]
    B_BUDGET = 263.120009
    return processors, tasks, B_BUDGET
