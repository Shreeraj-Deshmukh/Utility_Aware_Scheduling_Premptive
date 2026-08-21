"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599997, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599997, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.527819, 'e_o_k': [0.404077, 0.323262, 0.258609, 0.206887, 0.165510], 'p_i': 10, 'u_i': 3.4311},
        {'id': 1, 'e_m': 0.126792, 'e_o_k': [0.012885, 0.010308, 0.008247, 0.006597], 'p_i': 20, 'u_i': 3.8774},
        {'id': 2, 'e_m': 6.360533, 'e_o_k': [1.060089, 0.848071], 'p_i': 40, 'u_i': 3.3220},
        {'id': 3, 'e_m': 2.948864, 'e_o_k': [0.491477, 0.393182], 'p_i': 80, 'u_i': 2.5309},
        {'id': 4, 'e_m': 4.360293, 'e_o_k': [0.536102, 0.428881, 0.343105], 'p_i': 40, 'u_i': 3.7128},
        {'id': 5, 'e_m': 1.448667, 'e_o_k': [0.241445, 0.193156], 'p_i': 20, 'u_i': 4.9574},
        {'id': 6, 'e_m': 11.373666, 'e_o_k': [1.398402, 1.118721, 0.894977], 'p_i': 80, 'u_i': 3.9330},
        {'id': 7, 'e_m': 0.855715, 'e_o_k': [0.105211, 0.084169, 0.067335], 'p_i': 40, 'u_i': 3.5882},
    ]
    B_BUDGET = 119.599997
    return processors, tasks, B_BUDGET
