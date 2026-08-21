"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 104.512008, "H": 80, "J": 21, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.3, "seed": 1019, "set": 19, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.30"}
"""

_SPEC = '{"B": 104.512008, "H": 80, "J": 21, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.3, "seed": 1019, "set": 19, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.059421, 'e_o_k': [1.450945, 1.160756, 0.928605, 0.742884], 'p_i': 10, 'u_i': 1.9017},
        {'id': 1, 'e_m': 2.238024, 'e_o_k': [1.740685, 1.392548], 'p_i': 20, 'u_i': 4.1004},
        {'id': 2, 'e_m': 0.750637, 'e_o_k': [0.355993, 0.284794, 0.227836, 0.182268], 'p_i': 40, 'u_i': 2.6358},
        {'id': 3, 'e_m': 5.306501, 'e_o_k': [3.044714, 2.435771, 1.948617], 'p_i': 80, 'u_i': 4.3577},
        {'id': 4, 'e_m': 0.055926, 'e_o_k': [0.026523, 0.021219, 0.016975, 0.013580], 'p_i': 40, 'u_i': 4.2383},
        {'id': 5, 'e_m': 0.091009, 'e_o_k': [0.037902, 0.030322, 0.024258, 0.019406, 0.015525], 'p_i': 80, 'u_i': 1.1754},
        {'id': 6, 'e_m': 18.185686, 'e_o_k': [14.144422, 11.315538], 'p_i': 80, 'u_i': 2.9766},
        {'id': 7, 'e_m': 2.688109, 'e_o_k': [1.020078, 0.816062, 0.652850, 0.522280, 0.417824, 0.334259], 'p_i': 40, 'u_i': 4.8798},
    ]
    B_BUDGET = 104.512008
    return processors, tasks, B_BUDGET
