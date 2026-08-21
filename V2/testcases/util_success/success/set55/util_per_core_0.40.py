"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680005, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680005, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.362417, 'e_o_k': [0.192104, 0.153683, 0.122947, 0.098357, 0.078686, 0.062949], 'p_i': 10, 'u_i': 4.5134},
        {'id': 1, 'e_m': 1.818372, 'e_o_k': [0.223570, 0.178856, 0.143085], 'p_i': 20, 'u_i': 4.5874},
        {'id': 2, 'e_m': 2.018400, 'e_o_k': [0.248164, 0.198531, 0.158825], 'p_i': 40, 'u_i': 2.7347},
        {'id': 3, 'e_m': 10.977605, 'e_o_k': [1.349705, 1.079764, 0.863812], 'p_i': 80, 'u_i': 4.9671},
        {'id': 4, 'e_m': 5.439997, 'e_o_k': [0.485483, 0.388386, 0.310709, 0.248567, 0.198854], 'p_i': 80, 'u_i': 4.8761},
        {'id': 5, 'e_m': 0.284101, 'e_o_k': [0.028872, 0.023098, 0.018478, 0.014783], 'p_i': 10, 'u_i': 2.5248},
        {'id': 6, 'e_m': 1.455737, 'e_o_k': [0.242623, 0.194098], 'p_i': 40, 'u_i': 4.9532},
        {'id': 7, 'e_m': 6.094243, 'e_o_k': [0.619334, 0.495467, 0.396374, 0.317099], 'p_i': 40, 'u_i': 2.2979},
    ]
    B_BUDGET = 95.680005
    return processors, tasks, B_BUDGET
