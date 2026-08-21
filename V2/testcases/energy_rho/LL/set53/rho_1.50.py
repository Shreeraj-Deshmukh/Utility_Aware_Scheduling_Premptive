"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 64.400023, "H": 80, "J": 30, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.5, "seed": 1053, "set": 53, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.50"}
"""

_SPEC = '{"B": 64.400023, "H": 80, "J": 30, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.5, "seed": 1053, "set": 53, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.159031, 'e_o_k': [0.044175, 0.035340], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 1.218826, 'e_o_k': [0.338563, 0.270850], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 0.995792, 'e_o_k': [0.148113, 0.118490, 0.094792, 0.075834, 0.060667], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 5.369863, 'e_o_k': [1.491629, 1.193303], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 0.918489, 'e_o_k': [0.124481, 0.099585, 0.079668, 0.063734, 0.050987, 0.040790], 'p_i': 40, 'u_i': 2.8481},
        {'id': 5, 'e_m': 0.851463, 'e_o_k': [0.144218, 0.115374, 0.092300, 0.073840], 'p_i': 10, 'u_i': 3.6691},
        {'id': 6, 'e_m': 1.430219, 'e_o_k': [0.242246, 0.193797, 0.155037, 0.124030], 'p_i': 20, 'u_i': 3.0767},
        {'id': 7, 'e_m': 4.121451, 'e_o_k': [0.558571, 0.446857, 0.357486, 0.285988, 0.228791, 0.183033], 'p_i': 80, 'u_i': 1.7471},
    ]
    B_BUDGET = 64.400023
    return processors, tasks, B_BUDGET
