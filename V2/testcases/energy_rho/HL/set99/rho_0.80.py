"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 103.040009, "H": 80, "J": 28, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.8, "seed": 1099, "set": 99, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.80"}
"""

_SPEC = '{"B": 103.040009, "H": 80, "J": 28, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.8, "seed": 1099, "set": 99, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.970629, 'e_o_k': [0.144370, 0.115496, 0.092397, 0.073917, 0.059134], 'p_i': 10, 'u_i': 1.8657},
        {'id': 1, 'e_m': 2.923011, 'e_o_k': [0.434765, 0.347812, 0.278249, 0.222600, 0.178080], 'p_i': 20, 'u_i': 1.6547},
        {'id': 2, 'e_m': 1.109904, 'e_o_k': [0.187992, 0.150393, 0.120315, 0.096252], 'p_i': 40, 'u_i': 3.2690},
        {'id': 3, 'e_m': 3.648613, 'e_o_k': [0.747667, 0.598133, 0.478507], 'p_i': 80, 'u_i': 2.0883},
        {'id': 4, 'e_m': 1.035116, 'e_o_k': [0.212114, 0.169691, 0.135753], 'p_i': 10, 'u_i': 2.4453},
        {'id': 5, 'e_m': 10.125219, 'e_o_k': [1.506012, 1.204809, 0.963848, 0.771078, 0.616862], 'p_i': 40, 'u_i': 4.4841},
        {'id': 6, 'e_m': 4.891882, 'e_o_k': [1.002435, 0.801948, 0.641558], 'p_i': 40, 'u_i': 2.2759},
        {'id': 7, 'e_m': 0.359380, 'e_o_k': [0.099828, 0.079862], 'p_i': 80, 'u_i': 4.2544},
    ]
    B_BUDGET = 103.040009
    return processors, tasks, B_BUDGET
