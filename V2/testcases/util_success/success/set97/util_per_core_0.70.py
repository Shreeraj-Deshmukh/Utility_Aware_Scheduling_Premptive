"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440013, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440013, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.136268, 'e_o_k': [0.092398, 0.073918, 0.059134, 0.047308, 0.037846, 0.030277], 'p_i': 10, 'u_i': 4.0993},
        {'id': 1, 'e_m': 1.118794, 'e_o_k': [0.186466, 0.149172], 'p_i': 20, 'u_i': 2.5958},
        {'id': 2, 'e_m': 13.395987, 'e_o_k': [1.647048, 1.317638, 1.054110], 'p_i': 40, 'u_i': 1.3643},
        {'id': 3, 'e_m': 12.039229, 'e_o_k': [0.978990, 0.783192, 0.626554, 0.501243, 0.400994, 0.320795], 'p_i': 80, 'u_i': 1.6218},
        {'id': 4, 'e_m': 5.420744, 'e_o_k': [0.550889, 0.440711, 0.352569, 0.282055], 'p_i': 20, 'u_i': 1.2955},
        {'id': 5, 'e_m': 1.435554, 'e_o_k': [0.145890, 0.116712, 0.093369, 0.074696], 'p_i': 10, 'u_i': 2.7520},
        {'id': 6, 'e_m': 10.604793, 'e_o_k': [0.946406, 0.757125, 0.605700, 0.484560, 0.387648], 'p_i': 40, 'u_i': 2.0302},
        {'id': 7, 'e_m': 0.653310, 'e_o_k': [0.080325, 0.064260, 0.051408], 'p_i': 10, 'u_i': 2.5969},
    ]
    B_BUDGET = 167.440013
    return processors, tasks, B_BUDGET
