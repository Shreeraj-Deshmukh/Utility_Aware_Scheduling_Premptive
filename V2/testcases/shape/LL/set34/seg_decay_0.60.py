"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.109720, 'e_o_k': [0.027990, 0.016794, 0.010076], 'p_i': 10, 'u_i': 1.2368},
        {'id': 1, 'e_m': 0.572679, 'e_o_k': [0.120141, 0.072085, 0.043251, 0.025950, 0.015570, 0.009342], 'p_i': 20, 'u_i': 2.8306},
        {'id': 2, 'e_m': 5.630863, 'e_o_k': [1.436445, 0.861867, 0.517120], 'p_i': 40, 'u_i': 2.9234},
        {'id': 3, 'e_m': 3.715241, 'e_o_k': [0.947766, 0.568659, 0.341196], 'p_i': 80, 'u_i': 3.7707},
        {'id': 4, 'e_m': 1.331561, 'e_o_k': [0.339684, 0.203810, 0.122286], 'p_i': 20, 'u_i': 1.9627},
        {'id': 5, 'e_m': 1.635691, 'e_o_k': [0.511153, 0.306692], 'p_i': 40, 'u_i': 4.9296},
        {'id': 6, 'e_m': 0.014189, 'e_o_k': [0.002977, 0.001786, 0.001072, 0.000643, 0.000386, 0.000231], 'p_i': 40, 'u_i': 4.5772},
        {'id': 7, 'e_m': 0.653569, 'e_o_k': [0.141735, 0.085041, 0.051025, 0.030615, 0.018369], 'p_i': 10, 'u_i': 4.4816},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
