"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 57.408001, "H": 80, "J": 31, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.4, "seed": 1032, "set": 32, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.40"}
"""

_SPEC = '{"B": 57.408001, "H": 80, "J": 31, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.4, "seed": 1032, "set": 32, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.507641, 'e_o_k': [0.211417, 0.169133, 0.135307, 0.108245, 0.086596], 'p_i': 10, 'u_i': 2.6437},
        {'id': 1, 'e_m': 0.669069, 'e_o_k': [0.253897, 0.203117, 0.162494, 0.129995, 0.103996, 0.083197], 'p_i': 20, 'u_i': 2.4707},
        {'id': 2, 'e_m': 0.607685, 'e_o_k': [0.230603, 0.184482, 0.147586, 0.118069, 0.094455, 0.075564], 'p_i': 40, 'u_i': 1.1046},
        {'id': 3, 'e_m': 5.713737, 'e_o_k': [4.444017, 3.555214], 'p_i': 80, 'u_i': 3.2848},
        {'id': 4, 'e_m': 2.096375, 'e_o_k': [0.994216, 0.795373, 0.636298, 0.509039], 'p_i': 40, 'u_i': 2.0063},
        {'id': 5, 'e_m': 0.270524, 'e_o_k': [0.128297, 0.102638, 0.082110, 0.065688], 'p_i': 10, 'u_i': 1.2869},
        {'id': 6, 'e_m': 2.830351, 'e_o_k': [2.201384, 1.761107], 'p_i': 20, 'u_i': 2.7193},
        {'id': 7, 'e_m': 0.327572, 'e_o_k': [0.254778, 0.203823], 'p_i': 40, 'u_i': 1.9085},
    ]
    B_BUDGET = 57.408001
    return processors, tasks, B_BUDGET
