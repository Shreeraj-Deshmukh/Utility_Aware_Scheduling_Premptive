"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.306627, 'e_o_k': [0.085174, 0.068139], 'p_i': 10, 'u_i': 2.6246},
        {'id': 1, 'e_m': 0.296738, 'e_o_k': [0.082427, 0.065942], 'p_i': 20, 'u_i': 1.9533},
        {'id': 2, 'e_m': 4.540447, 'e_o_k': [1.261235, 1.008988], 'p_i': 40, 'u_i': 2.5491},
        {'id': 3, 'e_m': 14.551355, 'e_o_k': [4.042043, 3.233634], 'p_i': 80, 'u_i': 2.9783},
        {'id': 4, 'e_m': 5.361003, 'e_o_k': [1.489168, 1.191334], 'p_i': 20, 'u_i': 1.6186},
        {'id': 5, 'e_m': 2.936211, 'e_o_k': [0.815614, 0.652491], 'p_i': 40, 'u_i': 1.1221},
        {'id': 6, 'e_m': 1.139762, 'e_o_k': [0.316601, 0.253281], 'p_i': 20, 'u_i': 1.0173},
        {'id': 7, 'e_m': 0.606538, 'e_o_k': [0.168483, 0.134786], 'p_i': 10, 'u_i': 4.7591},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET
