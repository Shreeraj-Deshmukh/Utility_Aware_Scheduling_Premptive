"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640006, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640006, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.145211, 'e_o_k': [0.657088, 0.525670, 0.420536], 'p_i': 10, 'u_i': 1.6225},
        {'id': 1, 'e_m': 1.131105, 'e_o_k': [0.648995, 0.519196, 0.415357], 'p_i': 20, 'u_i': 4.7220},
        {'id': 2, 'e_m': 1.635759, 'e_o_k': [0.938550, 0.750840, 0.600672], 'p_i': 40, 'u_i': 1.8233},
        {'id': 3, 'e_m': 10.249639, 'e_o_k': [5.880941, 4.704752, 3.763802], 'p_i': 80, 'u_i': 1.9473},
        {'id': 4, 'e_m': 4.233912, 'e_o_k': [2.429294, 1.943435, 1.554748], 'p_i': 20, 'u_i': 3.9894},
        {'id': 5, 'e_m': 0.437464, 'e_o_k': [0.251004, 0.200803, 0.160643], 'p_i': 10, 'u_i': 1.1602},
        {'id': 6, 'e_m': 2.093940, 'e_o_k': [1.201441, 0.961153, 0.768922], 'p_i': 20, 'u_i': 4.5224},
        {'id': 7, 'e_m': 7.981619, 'e_o_k': [4.579617, 3.663694, 2.930955], 'p_i': 80, 'u_i': 3.6370},
    ]
    B_BUDGET = 176.640006
    return processors, tasks, B_BUDGET
