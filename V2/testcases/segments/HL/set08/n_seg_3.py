"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400018, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400018, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.713852, 'e_o_k': [0.146281, 0.117025, 0.093620], 'p_i': 10, 'u_i': 2.0315},
        {'id': 1, 'e_m': 0.102835, 'e_o_k': [0.021073, 0.016858, 0.013487], 'p_i': 20, 'u_i': 1.5871},
        {'id': 2, 'e_m': 5.612205, 'e_o_k': [1.150042, 0.920034, 0.736027], 'p_i': 40, 'u_i': 1.8711},
        {'id': 3, 'e_m': 3.855748, 'e_o_k': [0.790112, 0.632090, 0.505672], 'p_i': 80, 'u_i': 4.9538},
        {'id': 4, 'e_m': 0.273644, 'e_o_k': [0.056075, 0.044860, 0.035888], 'p_i': 20, 'u_i': 2.3994},
        {'id': 5, 'e_m': 4.043450, 'e_o_k': [0.828576, 0.662861, 0.530289], 'p_i': 10, 'u_i': 1.5904},
        {'id': 6, 'e_m': 1.584227, 'e_o_k': [0.324637, 0.259709, 0.207768], 'p_i': 40, 'u_i': 2.4893},
        {'id': 7, 'e_m': 0.773382, 'e_o_k': [0.158480, 0.126784, 0.101427], 'p_i': 10, 'u_i': 4.7173},
    ]
    B_BUDGET = 110.400018
    return processors, tasks, B_BUDGET
