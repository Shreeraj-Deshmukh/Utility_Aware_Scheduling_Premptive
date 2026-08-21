"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360001, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360001, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.422611, 'e_o_k': [0.042948, 0.034359, 0.027487, 0.021990], 'p_i': 10, 'u_i': 1.2796},
        {'id': 1, 'e_m': 9.427119, 'e_o_k': [0.958041, 0.766432, 0.613146, 0.490517], 'p_i': 20, 'u_i': 2.4526},
        {'id': 2, 'e_m': 18.206571, 'e_o_k': [2.238513, 1.790810, 1.432648], 'p_i': 40, 'u_i': 3.7482},
        {'id': 3, 'e_m': 11.479004, 'e_o_k': [1.024423, 0.819539, 0.655631, 0.524505, 0.419604], 'p_i': 80, 'u_i': 2.1247},
        {'id': 4, 'e_m': 5.605062, 'e_o_k': [0.569620, 0.455696, 0.364557, 0.291646], 'p_i': 40, 'u_i': 4.6336},
        {'id': 5, 'e_m': 2.068613, 'e_o_k': [0.254338, 0.203470, 0.162776], 'p_i': 80, 'u_i': 4.4629},
        {'id': 6, 'e_m': 1.535181, 'e_o_k': [0.137005, 0.109604, 0.087683, 0.070146, 0.056117], 'p_i': 10, 'u_i': 1.2397},
        {'id': 7, 'e_m': 1.682287, 'e_o_k': [0.170964, 0.136771, 0.109417, 0.087534], 'p_i': 10, 'u_i': 2.9672},
    ]
    B_BUDGET = 191.360001
    return processors, tasks, B_BUDGET
