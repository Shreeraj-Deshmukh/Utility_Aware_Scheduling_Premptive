"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600009, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600009, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.953022, 'e_o_k': [0.240130, 0.192104, 0.153683, 0.122947, 0.098357, 0.078686], 'p_i': 10, 'u_i': 4.5134},
        {'id': 1, 'e_m': 2.272965, 'e_o_k': [0.279463, 0.223570, 0.178856], 'p_i': 20, 'u_i': 4.5874},
        {'id': 2, 'e_m': 2.523000, 'e_o_k': [0.310205, 0.248164, 0.198531], 'p_i': 40, 'u_i': 2.7347},
        {'id': 3, 'e_m': 13.722006, 'e_o_k': [1.687132, 1.349705, 1.079764], 'p_i': 80, 'u_i': 4.9671},
        {'id': 4, 'e_m': 6.799996, 'e_o_k': [0.606854, 0.485483, 0.388386, 0.310709, 0.248567], 'p_i': 80, 'u_i': 4.8761},
        {'id': 5, 'e_m': 0.355127, 'e_o_k': [0.036090, 0.028872, 0.023098, 0.018478], 'p_i': 10, 'u_i': 2.5248},
        {'id': 6, 'e_m': 1.819672, 'e_o_k': [0.303279, 0.242623], 'p_i': 40, 'u_i': 4.9532},
        {'id': 7, 'e_m': 7.617803, 'e_o_k': [0.774167, 0.619334, 0.495467, 0.396374], 'p_i': 40, 'u_i': 2.2979},
    ]
    B_BUDGET = 119.600009
    return processors, tasks, B_BUDGET
