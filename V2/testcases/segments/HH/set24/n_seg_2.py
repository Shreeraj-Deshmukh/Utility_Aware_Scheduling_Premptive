"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.255086, 'e_o_k': [0.198400, 0.158720], 'p_i': 10, 'u_i': 1.4092},
        {'id': 1, 'e_m': 1.766930, 'e_o_k': [1.374279, 1.099423], 'p_i': 20, 'u_i': 2.7448},
        {'id': 2, 'e_m': 4.717796, 'e_o_k': [3.669397, 2.935518], 'p_i': 40, 'u_i': 3.9391},
        {'id': 3, 'e_m': 2.076602, 'e_o_k': [1.615135, 1.292108], 'p_i': 80, 'u_i': 3.4662},
        {'id': 4, 'e_m': 0.980401, 'e_o_k': [0.762534, 0.610027], 'p_i': 40, 'u_i': 1.1407},
        {'id': 5, 'e_m': 28.292425, 'e_o_k': [22.005219, 17.604175], 'p_i': 80, 'u_i': 3.5457},
        {'id': 6, 'e_m': 0.799254, 'e_o_k': [0.621642, 0.497313], 'p_i': 10, 'u_i': 1.4096},
        {'id': 7, 'e_m': 1.683036, 'e_o_k': [1.309028, 1.047222], 'p_i': 20, 'u_i': 4.8654},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
