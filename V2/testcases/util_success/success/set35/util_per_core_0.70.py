"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.536597, 'e_o_k': [0.054532, 0.043626, 0.034901, 0.027920], 'p_i': 10, 'u_i': 2.6246},
        {'id': 1, 'e_m': 0.519292, 'e_o_k': [0.042227, 0.033782, 0.027025, 0.021620, 0.017296, 0.013837], 'p_i': 20, 'u_i': 2.3478},
        {'id': 2, 'e_m': 7.945782, 'e_o_k': [0.976940, 0.781552, 0.625242], 'p_i': 40, 'u_i': 2.5491},
        {'id': 3, 'e_m': 25.464870, 'e_o_k': [2.272567, 1.818054, 1.454443, 1.163554, 0.930843], 'p_i': 80, 'u_i': 2.9783},
        {'id': 4, 'e_m': 9.381755, 'e_o_k': [1.563626, 1.250901], 'p_i': 20, 'u_i': 1.6186},
        {'id': 5, 'e_m': 5.138370, 'e_o_k': [0.417835, 0.334268, 0.267415, 0.213932, 0.171145, 0.136916], 'p_i': 40, 'u_i': 2.1935},
        {'id': 6, 'e_m': 1.994584, 'e_o_k': [0.245236, 0.196189, 0.156951], 'p_i': 20, 'u_i': 1.0173},
        {'id': 7, 'e_m': 1.061441, 'e_o_k': [0.176907, 0.141525], 'p_i': 10, 'u_i': 4.7591},
    ]
    B_BUDGET = 167.440001
    return processors, tasks, B_BUDGET
