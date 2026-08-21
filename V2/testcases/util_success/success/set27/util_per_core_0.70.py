"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440002, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440002, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.082144, 'e_o_k': [0.087996, 0.070397, 0.056318, 0.045054, 0.036043, 0.028835], 'p_i': 10, 'u_i': 1.3112},
        {'id': 1, 'e_m': 2.254887, 'e_o_k': [0.183360, 0.146688, 0.117350, 0.093880, 0.075104, 0.060083], 'p_i': 20, 'u_i': 2.1246},
        {'id': 2, 'e_m': 2.140528, 'e_o_k': [0.174061, 0.139248, 0.111399, 0.089119, 0.071295, 0.057036], 'p_i': 40, 'u_i': 2.2214},
        {'id': 3, 'e_m': 8.872447, 'e_o_k': [0.791806, 0.633445, 0.506756, 0.405405, 0.324324], 'p_i': 80, 'u_i': 3.1164},
        {'id': 4, 'e_m': 2.907910, 'e_o_k': [0.259511, 0.207609, 0.166087, 0.132870, 0.106296], 'p_i': 10, 'u_i': 2.9383},
        {'id': 5, 'e_m': 27.556295, 'e_o_k': [2.459212, 1.967370, 1.573896, 1.259117, 1.007293], 'p_i': 80, 'u_i': 2.8468},
        {'id': 6, 'e_m': 1.969827, 'e_o_k': [0.328305, 0.262644], 'p_i': 10, 'u_i': 4.6487},
        {'id': 7, 'e_m': 1.823951, 'e_o_k': [0.303992, 0.243193], 'p_i': 10, 'u_i': 3.0837},
    ]
    B_BUDGET = 167.440002
    return processors, tasks, B_BUDGET
