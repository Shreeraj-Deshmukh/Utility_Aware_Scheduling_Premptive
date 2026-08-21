"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599997, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599997, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.320793, 'e_o_k': [0.039442, 0.031553, 0.025243], 'p_i': 10, 'u_i': 2.2542},
        {'id': 1, 'e_m': 0.675095, 'e_o_k': [0.054897, 0.043917, 0.035134, 0.028107, 0.022486, 0.017988], 'p_i': 20, 'u_i': 3.1493},
        {'id': 2, 'e_m': 0.948422, 'e_o_k': [0.096384, 0.077108, 0.061686, 0.049349], 'p_i': 40, 'u_i': 4.3022},
        {'id': 3, 'e_m': 20.245756, 'e_o_k': [1.646318, 1.317054, 1.053643, 0.842915, 0.674332, 0.539465], 'p_i': 80, 'u_i': 4.8493},
        {'id': 4, 'e_m': 12.663985, 'e_o_k': [2.110664, 1.688531], 'p_i': 40, 'u_i': 1.1754},
        {'id': 5, 'e_m': 7.606179, 'e_o_k': [0.618509, 0.494807, 0.395846, 0.316677, 0.253341, 0.202673], 'p_i': 40, 'u_i': 3.0798},
        {'id': 6, 'e_m': 1.031549, 'e_o_k': [0.126830, 0.101464, 0.081171], 'p_i': 10, 'u_i': 3.4237},
        {'id': 7, 'e_m': 0.949488, 'e_o_k': [0.077209, 0.061767, 0.049414, 0.039531, 0.031625, 0.025300], 'p_i': 20, 'u_i': 3.1726},
    ]
    B_BUDGET = 119.599997
    return processors, tasks, B_BUDGET
