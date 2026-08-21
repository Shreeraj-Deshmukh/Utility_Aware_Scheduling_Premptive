"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32001, "H": 80, "J": 33, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "freq", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32001, "H": 80, "J": 33, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "freq", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.190797, 'e_o_k': [0.926175, 0.740940], 'p_i': 10, 'u_i': 3.1340},
        {'id': 1, 'e_m': 0.359142, 'e_o_k': [0.170325, 0.136260, 0.109008, 0.087206], 'p_i': 20, 'u_i': 4.7064},
        {'id': 2, 'e_m': 0.831853, 'e_o_k': [0.346441, 0.277152, 0.221722, 0.177378, 0.141902], 'p_i': 40, 'u_i': 3.9461},
        {'id': 3, 'e_m': 10.420760, 'e_o_k': [4.942095, 3.953676, 3.162941, 2.530353], 'p_i': 80, 'u_i': 2.2173},
        {'id': 4, 'e_m': 0.657127, 'e_o_k': [0.511098, 0.408879], 'p_i': 20, 'u_i': 4.4667},
        {'id': 5, 'e_m': 0.368053, 'e_o_k': [0.153283, 0.122626, 0.098101, 0.078481, 0.062785], 'p_i': 10, 'u_i': 3.9626},
        {'id': 6, 'e_m': 0.634198, 'e_o_k': [0.363884, 0.291107, 0.232886], 'p_i': 20, 'u_i': 1.6271},
        {'id': 7, 'e_m': 0.421433, 'e_o_k': [0.175514, 0.140411, 0.112329, 0.089863, 0.071890], 'p_i': 40, 'u_i': 2.4987},
    ]
    B_BUDGET = 88.320010
    return processors, tasks, B_BUDGET
