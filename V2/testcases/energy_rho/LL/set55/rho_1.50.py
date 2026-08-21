"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 64.39998, "H": 80, "J": 28, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.5, "seed": 1055, "set": 55, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.50"}
"""

_SPEC = '{"B": 64.39998, "H": 80, "J": 28, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.5, "seed": 1055, "set": 55, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.181209, 'e_o_k': [0.160087, 0.128069, 0.102455, 0.081964, 0.065571, 0.052457], 'p_i': 10, 'u_i': 4.5134},
        {'id': 1, 'e_m': 0.909186, 'e_o_k': [0.186309, 0.149047, 0.119237], 'p_i': 20, 'u_i': 4.5874},
        {'id': 2, 'e_m': 1.009200, 'e_o_k': [0.206803, 0.165443, 0.132354], 'p_i': 40, 'u_i': 2.7347},
        {'id': 3, 'e_m': 5.488802, 'e_o_k': [1.124755, 0.899804, 0.719843], 'p_i': 80, 'u_i': 4.9671},
        {'id': 4, 'e_m': 2.719998, 'e_o_k': [0.404569, 0.323655, 0.258924, 0.207139, 0.165711], 'p_i': 80, 'u_i': 4.8761},
        {'id': 5, 'e_m': 0.142051, 'e_o_k': [0.024060, 0.019248, 0.015398, 0.012319], 'p_i': 10, 'u_i': 2.5248},
        {'id': 6, 'e_m': 0.727869, 'e_o_k': [0.202186, 0.161749], 'p_i': 40, 'u_i': 4.9532},
        {'id': 7, 'e_m': 3.047121, 'e_o_k': [0.516111, 0.412889, 0.330311, 0.264249], 'p_i': 40, 'u_i': 2.2979},
    ]
    B_BUDGET = 64.399980
    return processors, tasks, B_BUDGET
