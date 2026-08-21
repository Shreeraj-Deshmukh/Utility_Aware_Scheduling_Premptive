"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640013, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640013, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.219440, 'e_o_k': [0.125908, 0.100727, 0.080581], 'p_i': 10, 'u_i': 1.2368},
        {'id': 1, 'e_m': 1.145357, 'e_o_k': [0.657172, 0.525738, 0.420590], 'p_i': 20, 'u_i': 3.8785},
        {'id': 2, 'e_m': 11.261726, 'e_o_k': [6.461646, 5.169317, 4.135453], 'p_i': 40, 'u_i': 2.8542},
        {'id': 3, 'e_m': 7.430483, 'e_o_k': [4.263392, 3.410713, 2.728571], 'p_i': 80, 'u_i': 3.7707},
        {'id': 4, 'e_m': 2.663123, 'e_o_k': [1.528021, 1.222417, 0.977934], 'p_i': 20, 'u_i': 1.9627},
        {'id': 5, 'e_m': 3.271381, 'e_o_k': [1.877022, 1.501618, 1.201294], 'p_i': 40, 'u_i': 4.9296},
        {'id': 6, 'e_m': 0.028377, 'e_o_k': [0.016282, 0.013026, 0.010420], 'p_i': 40, 'u_i': 2.8369},
        {'id': 7, 'e_m': 1.307139, 'e_o_k': [0.749998, 0.599998, 0.479999], 'p_i': 10, 'u_i': 1.1432},
    ]
    B_BUDGET = 176.640013
    return processors, tasks, B_BUDGET
