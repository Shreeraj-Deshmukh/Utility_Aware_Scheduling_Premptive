"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 37, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "tasks", "util_per_core": 0.2, "value": "8"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 37, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "tasks", "util_per_core": 0.2, "value": "8"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.244220, 'e_o_k': [0.189949, 0.151959], 'p_i': 10, 'u_i': 1.2408},
        {'id': 1, 'e_m': 0.462328, 'e_o_k': [0.219261, 0.175409, 0.140327, 0.112262], 'p_i': 20, 'u_i': 2.7274},
        {'id': 2, 'e_m': 1.144163, 'e_o_k': [0.476508, 0.381206, 0.304965, 0.243972, 0.195178], 'p_i': 40, 'u_i': 3.7398},
        {'id': 3, 'e_m': 2.328605, 'e_o_k': [1.336085, 1.068868, 0.855094], 'p_i': 80, 'u_i': 1.4758},
        {'id': 4, 'e_m': 0.072384, 'e_o_k': [0.027468, 0.021974, 0.017580, 0.014064, 0.011251, 0.009001], 'p_i': 10, 'u_i': 1.9890},
        {'id': 5, 'e_m': 0.070477, 'e_o_k': [0.040438, 0.032350, 0.025880], 'p_i': 40, 'u_i': 1.7667},
        {'id': 6, 'e_m': 2.462336, 'e_o_k': [1.412816, 1.130253, 0.904202], 'p_i': 20, 'u_i': 2.7743},
        {'id': 7, 'e_m': 1.626328, 'e_o_k': [0.771294, 0.617035, 0.493628, 0.394902], 'p_i': 10, 'u_i': 3.3191},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET
