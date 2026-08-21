"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279988, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279988, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.136104, 'e_o_k': [0.369119, 0.295295, 0.236236, 0.188989, 0.151191], 'p_i': 10, 'u_i': 1.0628},
        {'id': 1, 'e_m': 1.318677, 'e_o_k': [0.162132, 0.129706, 0.103765], 'p_i': 20, 'u_i': 2.8143},
        {'id': 2, 'e_m': 5.605286, 'e_o_k': [0.569643, 0.455714, 0.364571, 0.291657], 'p_i': 40, 'u_i': 2.2180},
        {'id': 3, 'e_m': 16.501443, 'e_o_k': [2.028866, 1.623093, 1.298474], 'p_i': 80, 'u_i': 2.6552},
        {'id': 4, 'e_m': 3.909351, 'e_o_k': [0.397292, 0.317833, 0.254267, 0.203413], 'p_i': 20, 'u_i': 2.3560},
        {'id': 5, 'e_m': 9.863751, 'e_o_k': [0.880273, 0.704218, 0.563375, 0.450700, 0.360560], 'p_i': 20, 'u_i': 3.1359},
        {'id': 6, 'e_m': 9.233649, 'e_o_k': [0.938379, 0.750703, 0.600563, 0.480450], 'p_i': 80, 'u_i': 1.7649},
        {'id': 7, 'e_m': 3.399597, 'e_o_k': [0.417983, 0.334387, 0.267509], 'p_i': 20, 'u_i': 1.5174},
    ]
    B_BUDGET = 215.279988
    return processors, tasks, B_BUDGET
