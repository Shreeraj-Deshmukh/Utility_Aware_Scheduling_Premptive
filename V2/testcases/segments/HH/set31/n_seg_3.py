"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640009, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640009, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.396008, 'e_o_k': [0.227218, 0.181774, 0.145419], 'p_i': 10, 'u_i': 2.2582},
        {'id': 1, 'e_m': 1.438192, 'e_o_k': [0.825192, 0.660154, 0.528123], 'p_i': 20, 'u_i': 2.9332},
        {'id': 2, 'e_m': 0.174158, 'e_o_k': [0.099927, 0.079942, 0.063953], 'p_i': 40, 'u_i': 1.0372},
        {'id': 3, 'e_m': 2.213172, 'e_o_k': [1.269853, 1.015882, 0.812706], 'p_i': 80, 'u_i': 1.7921},
        {'id': 4, 'e_m': 8.410664, 'e_o_k': [4.825791, 3.860633, 3.088506], 'p_i': 40, 'u_i': 3.3121},
        {'id': 5, 'e_m': 14.019005, 'e_o_k': [8.043691, 6.434953, 5.147962], 'p_i': 40, 'u_i': 3.7636},
        {'id': 6, 'e_m': 1.468623, 'e_o_k': [0.842653, 0.674122, 0.539298], 'p_i': 80, 'u_i': 1.1326},
        {'id': 7, 'e_m': 6.189722, 'e_o_k': [3.551480, 2.841184, 2.272947], 'p_i': 80, 'u_i': 3.1203},
    ]
    B_BUDGET = 176.640009
    return processors, tasks, B_BUDGET
