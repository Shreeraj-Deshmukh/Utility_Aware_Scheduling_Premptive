"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 37, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 37, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.713852, 'e_o_k': [0.096747, 0.077397, 0.061918, 0.049534, 0.039627, 0.031702], 'p_i': 10, 'u_i': 3.2910},
        {'id': 1, 'e_m': 0.102835, 'e_o_k': [0.017418, 0.013934, 0.011147, 0.008918], 'p_i': 20, 'u_i': 2.7579},
        {'id': 2, 'e_m': 5.612205, 'e_o_k': [0.834752, 0.667802, 0.534241, 0.427393, 0.341914], 'p_i': 40, 'u_i': 2.6468},
        {'id': 3, 'e_m': 3.855748, 'e_o_k': [1.071041, 0.856833], 'p_i': 80, 'u_i': 2.7178},
        {'id': 4, 'e_m': 0.273644, 'e_o_k': [0.076012, 0.060810], 'p_i': 20, 'u_i': 3.4885},
        {'id': 5, 'e_m': 4.043450, 'e_o_k': [0.601418, 0.481134, 0.384907, 0.307926, 0.246341], 'p_i': 10, 'u_i': 2.8499},
        {'id': 6, 'e_m': 1.584227, 'e_o_k': [0.440063, 0.352050], 'p_i': 40, 'u_i': 2.6476},
        {'id': 7, 'e_m': 0.773382, 'e_o_k': [0.158480, 0.126784, 0.101427], 'p_i': 10, 'u_i': 2.8723},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET
