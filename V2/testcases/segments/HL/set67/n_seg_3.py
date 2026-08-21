"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399993, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399993, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.622255, 'e_o_k': [0.742265, 0.593812, 0.475050], 'p_i': 10, 'u_i': 3.4311},
        {'id': 1, 'e_m': 0.101434, 'e_o_k': [0.020786, 0.016628, 0.013303], 'p_i': 20, 'u_i': 3.8774},
        {'id': 2, 'e_m': 5.088426, 'e_o_k': [1.042710, 0.834168, 0.667335], 'p_i': 40, 'u_i': 3.3220},
        {'id': 3, 'e_m': 2.359092, 'e_o_k': [0.483420, 0.386736, 0.309389], 'p_i': 80, 'u_i': 2.5309},
        {'id': 4, 'e_m': 3.488235, 'e_o_k': [0.714802, 0.571842, 0.457473], 'p_i': 40, 'u_i': 3.7128},
        {'id': 5, 'e_m': 1.158934, 'e_o_k': [0.237486, 0.189989, 0.151991], 'p_i': 20, 'u_i': 4.9574},
        {'id': 6, 'e_m': 9.098933, 'e_o_k': [1.864535, 1.491628, 1.193303], 'p_i': 80, 'u_i': 3.9330},
        {'id': 7, 'e_m': 0.684572, 'e_o_k': [0.140281, 0.112225, 0.089780], 'p_i': 40, 'u_i': 3.5882},
    ]
    B_BUDGET = 110.399993
    return processors, tasks, B_BUDGET
