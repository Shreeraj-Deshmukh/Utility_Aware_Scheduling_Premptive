"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.19999, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.19999, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.604549, 'e_o_k': [0.293110, 0.234488, 0.187590, 0.150072, 0.120058, 0.096046], 'p_i': 10, 'u_i': 4.3963},
        {'id': 1, 'e_m': 0.370519, 'e_o_k': [0.033066, 0.026453, 0.021162, 0.016930, 0.013544], 'p_i': 20, 'u_i': 4.6647},
        {'id': 2, 'e_m': 12.050569, 'e_o_k': [2.008428, 1.606743], 'p_i': 40, 'u_i': 3.3449},
        {'id': 3, 'e_m': 32.951005, 'e_o_k': [3.348679, 2.678943, 2.143155, 1.714524], 'p_i': 80, 'u_i': 1.1238},
        {'id': 4, 'e_m': 3.369256, 'e_o_k': [0.561543, 0.449234], 'p_i': 80, 'u_i': 1.3826},
        {'id': 5, 'e_m': 9.473043, 'e_o_k': [0.770316, 0.616253, 0.493002, 0.394402, 0.315522, 0.252417], 'p_i': 20, 'u_i': 1.5263},
        {'id': 6, 'e_m': 6.285080, 'e_o_k': [0.560901, 0.448721, 0.358976, 0.287181, 0.229745], 'p_i': 40, 'u_i': 2.5074},
        {'id': 7, 'e_m': 2.349725, 'e_o_k': [0.288901, 0.231121, 0.184896], 'p_i': 10, 'u_i': 2.8865},
    ]
    B_BUDGET = 239.199990
    return processors, tasks, B_BUDGET
