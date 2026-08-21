"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 30, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 30, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.159031, 'e_o_k': [0.123690, 0.098952], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 1.218826, 'e_o_k': [0.947976, 0.758380], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 0.995792, 'e_o_k': [0.414716, 0.331773, 0.265418, 0.212335, 0.169868], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 5.369863, 'e_o_k': [4.176560, 3.341248], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 0.918489, 'e_o_k': [0.348546, 0.278837, 0.223069, 0.178456, 0.142764, 0.114212], 'p_i': 40, 'u_i': 2.8481},
        {'id': 5, 'e_m': 0.851463, 'e_o_k': [0.403810, 0.323048, 0.258439, 0.206751], 'p_i': 10, 'u_i': 3.6691},
        {'id': 6, 'e_m': 1.430219, 'e_o_k': [0.678288, 0.542630, 0.434104, 0.347283], 'p_i': 20, 'u_i': 3.0767},
        {'id': 7, 'e_m': 4.121451, 'e_o_k': [1.563999, 1.251199, 1.000960, 0.800768, 0.640614, 0.512491], 'p_i': 80, 'u_i': 1.7471},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
