"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319995, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319995, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.063904, 'e_o_k': [0.036666, 0.029333, 0.023466], 'p_i': 10, 'u_i': 3.7146},
        {'id': 1, 'e_m': 2.319143, 'e_o_k': [1.330656, 1.064525, 0.851620], 'p_i': 20, 'u_i': 2.7971},
        {'id': 2, 'e_m': 0.400395, 'e_o_k': [0.229735, 0.183788, 0.147030], 'p_i': 40, 'u_i': 1.6396},
        {'id': 3, 'e_m': 4.718930, 'e_o_k': [2.707583, 2.166066, 1.732853], 'p_i': 80, 'u_i': 4.1445},
        {'id': 4, 'e_m': 1.741564, 'e_o_k': [0.999258, 0.799407, 0.639525], 'p_i': 20, 'u_i': 4.6205},
        {'id': 5, 'e_m': 7.261818, 'e_o_k': [4.166617, 3.333294, 2.666635], 'p_i': 80, 'u_i': 4.6158},
        {'id': 6, 'e_m': 0.036678, 'e_o_k': [0.021045, 0.016836, 0.013469], 'p_i': 20, 'u_i': 3.3652},
        {'id': 7, 'e_m': 0.579422, 'e_o_k': [0.332455, 0.265964, 0.212771], 'p_i': 20, 'u_i': 2.1692},
    ]
    B_BUDGET = 88.319995
    return processors, tasks, B_BUDGET
