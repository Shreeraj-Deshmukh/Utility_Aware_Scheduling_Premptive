"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 217.856003, "H": 80, "J": 20, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.4, "seed": 1014, "set": 14, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.40"}
"""

_SPEC = '{"B": 217.856003, "H": 80, "J": 20, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.4, "seed": 1014, "set": 14, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.722458, 'e_o_k': [0.561912, 0.449530], 'p_i': 10, 'u_i': 1.0216},
        {'id': 1, 'e_m': 3.086888, 'e_o_k': [1.771165, 1.416932, 1.133546], 'p_i': 20, 'u_i': 4.0085},
        {'id': 2, 'e_m': 11.212672, 'e_o_k': [6.433500, 5.146800, 4.117440], 'p_i': 40, 'u_i': 1.9931},
        {'id': 3, 'e_m': 4.466066, 'e_o_k': [2.562497, 2.049997, 1.639998], 'p_i': 80, 'u_i': 2.4773},
        {'id': 4, 'e_m': 0.168840, 'e_o_k': [0.080073, 0.064058, 0.051247, 0.040997], 'p_i': 80, 'u_i': 3.1022},
        {'id': 5, 'e_m': 1.988081, 'e_o_k': [0.754433, 0.603546, 0.482837, 0.386269, 0.309016, 0.247212], 'p_i': 40, 'u_i': 1.9821},
        {'id': 6, 'e_m': 7.911221, 'e_o_k': [4.539225, 3.631380, 2.905104], 'p_i': 80, 'u_i': 1.2190},
        {'id': 7, 'e_m': 6.925151, 'e_o_k': [3.284286, 2.627429, 2.101943, 1.681554], 'p_i': 80, 'u_i': 2.8489},
    ]
    B_BUDGET = 217.856003
    return processors, tasks, B_BUDGET
