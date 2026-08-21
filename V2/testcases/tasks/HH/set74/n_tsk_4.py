"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.543848, 'e_o_k': [0.422993, 0.338394], 'p_i': 10, 'u_i': 4.4654},
        {'id': 1, 'e_m': 5.701150, 'e_o_k': [3.271152, 2.616921, 2.093537], 'p_i': 20, 'u_i': 1.2910},
        {'id': 2, 'e_m': 15.008227, 'e_o_k': [5.695290, 4.556232, 3.644985, 2.915988, 2.332791, 1.866232], 'p_i': 40, 'u_i': 1.4207},
        {'id': 3, 'e_m': 6.828165, 'e_o_k': [2.843715, 2.274972, 1.819977, 1.455982, 1.164785], 'p_i': 80, 'u_i': 4.1417},
    ]
    B_BUDGET = 176.640007
    return processors, tasks, B_BUDGET
