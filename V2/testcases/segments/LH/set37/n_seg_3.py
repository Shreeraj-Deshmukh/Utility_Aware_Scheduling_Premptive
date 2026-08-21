"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.31999, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.31999, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.190797, 'e_o_k': [0.683244, 0.546595, 0.437276], 'p_i': 10, 'u_i': 3.1340},
        {'id': 1, 'e_m': 0.359142, 'e_o_k': [0.206065, 0.164852, 0.131882], 'p_i': 20, 'u_i': 4.7064},
        {'id': 2, 'e_m': 0.831853, 'e_o_k': [0.477293, 0.381834, 0.305467], 'p_i': 40, 'u_i': 3.9461},
        {'id': 3, 'e_m': 10.420760, 'e_o_k': [5.979125, 4.783300, 3.826640], 'p_i': 80, 'u_i': 2.2173},
        {'id': 4, 'e_m': 0.657127, 'e_o_k': [0.377040, 0.301632, 0.241305], 'p_i': 20, 'u_i': 4.4667},
        {'id': 5, 'e_m': 0.368053, 'e_o_k': [0.211178, 0.168942, 0.135154], 'p_i': 10, 'u_i': 3.9626},
        {'id': 6, 'e_m': 0.634198, 'e_o_k': [0.363884, 0.291107, 0.232886], 'p_i': 20, 'u_i': 1.6271},
        {'id': 7, 'e_m': 0.421433, 'e_o_k': [0.241806, 0.193445, 0.154756], 'p_i': 40, 'u_i': 2.4987},
    ]
    B_BUDGET = 88.319990
    return processors, tasks, B_BUDGET
