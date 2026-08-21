"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.073209, 'e_o_k': [0.615776, 0.492621, 0.394096], 'p_i': 10, 'u_i': 3.4396},
        {'id': 1, 'e_m': 2.009822, 'e_o_k': [1.153177, 0.922541, 0.738033], 'p_i': 20, 'u_i': 1.7213},
        {'id': 2, 'e_m': 4.500422, 'e_o_k': [2.582210, 2.065768, 1.652614], 'p_i': 40, 'u_i': 2.3007},
        {'id': 3, 'e_m': 5.174123, 'e_o_k': [2.968759, 2.375007, 1.900006], 'p_i': 80, 'u_i': 2.4667},
        {'id': 4, 'e_m': 4.541214, 'e_o_k': [2.605615, 2.084492, 1.667593], 'p_i': 80, 'u_i': 2.4016},
        {'id': 5, 'e_m': 0.685731, 'e_o_k': [0.393452, 0.314762, 0.251809], 'p_i': 10, 'u_i': 3.4602},
        {'id': 6, 'e_m': 15.096114, 'e_o_k': [8.661705, 6.929364, 5.543491], 'p_i': 80, 'u_i': 3.9709},
        {'id': 7, 'e_m': 8.076896, 'e_o_k': [4.634284, 3.707427, 2.965942], 'p_i': 80, 'u_i': 1.7339},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET
