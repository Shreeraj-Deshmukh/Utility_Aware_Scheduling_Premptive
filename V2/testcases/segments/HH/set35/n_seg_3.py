"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640013, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640013, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.306627, 'e_o_k': [0.175933, 0.140747, 0.112597], 'p_i': 10, 'u_i': 2.6246},
        {'id': 1, 'e_m': 0.296738, 'e_o_k': [0.170260, 0.136208, 0.108966], 'p_i': 20, 'u_i': 1.9533},
        {'id': 2, 'e_m': 4.540447, 'e_o_k': [2.605174, 2.084139, 1.667312], 'p_i': 40, 'u_i': 2.5491},
        {'id': 3, 'e_m': 14.551355, 'e_o_k': [8.349138, 6.679310, 5.343448], 'p_i': 80, 'u_i': 2.9783},
        {'id': 4, 'e_m': 5.361003, 'e_o_k': [3.075985, 2.460788, 1.968631], 'p_i': 20, 'u_i': 1.6186},
        {'id': 5, 'e_m': 2.936211, 'e_o_k': [1.684711, 1.347769, 1.078215], 'p_i': 40, 'u_i': 1.1221},
        {'id': 6, 'e_m': 1.139762, 'e_o_k': [0.653962, 0.523170, 0.418536], 'p_i': 20, 'u_i': 1.0173},
        {'id': 7, 'e_m': 0.606538, 'e_o_k': [0.348014, 0.278411, 0.222729], 'p_i': 10, 'u_i': 4.7591},
    ]
    B_BUDGET = 176.640013
    return processors, tasks, B_BUDGET
