"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.51999, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.51999, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.318111, 'e_o_k': [0.269818, 0.215854, 0.172683, 0.138147, 0.110517, 0.088414], 'p_i': 10, 'u_i': 4.6267},
        {'id': 1, 'e_m': 3.149472, 'e_o_k': [0.524912, 0.419930], 'p_i': 20, 'u_i': 4.4310},
        {'id': 2, 'e_m': 0.383252, 'e_o_k': [0.034203, 0.027362, 0.021890, 0.017512, 0.014009], 'p_i': 40, 'u_i': 4.5357},
        {'id': 3, 'e_m': 9.243319, 'e_o_k': [0.751636, 0.601309, 0.481047, 0.384838, 0.307870, 0.246296], 'p_i': 80, 'u_i': 2.3203},
        {'id': 4, 'e_m': 4.885883, 'e_o_k': [0.600723, 0.480579, 0.384463], 'p_i': 80, 'u_i': 3.8723},
        {'id': 5, 'e_m': 2.689050, 'e_o_k': [0.273277, 0.218622, 0.174898, 0.139918], 'p_i': 40, 'u_i': 1.1816},
        {'id': 6, 'e_m': 21.896117, 'e_o_k': [1.780520, 1.424416, 1.139533, 0.911626, 0.729301, 0.583441], 'p_i': 80, 'u_i': 4.5942},
        {'id': 7, 'e_m': 1.835912, 'e_o_k': [0.163843, 0.131074, 0.104859, 0.083887, 0.067110], 'p_i': 10, 'u_i': 3.3631},
    ]
    B_BUDGET = 143.519990
    return processors, tasks, B_BUDGET
