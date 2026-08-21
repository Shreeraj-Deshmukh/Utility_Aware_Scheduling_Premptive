"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600003, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600003, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.495010, 'e_o_k': [0.044176, 0.035341, 0.028273, 0.022618, 0.018095], 'p_i': 10, 'u_i': 2.2582},
        {'id': 1, 'e_m': 1.797740, 'e_o_k': [0.299623, 0.239699], 'p_i': 20, 'u_i': 2.9332},
        {'id': 2, 'e_m': 0.217698, 'e_o_k': [0.026766, 0.021413, 0.017130], 'p_i': 40, 'u_i': 1.0372},
        {'id': 3, 'e_m': 2.766465, 'e_o_k': [0.340139, 0.272111, 0.217689], 'p_i': 80, 'u_i': 1.7921},
        {'id': 4, 'e_m': 10.513330, 'e_o_k': [0.854909, 0.683927, 0.547142, 0.437713, 0.350171, 0.280137], 'p_i': 40, 'u_i': 1.1296},
        {'id': 5, 'e_m': 17.523756, 'e_o_k': [2.154560, 1.723648, 1.378918], 'p_i': 40, 'u_i': 3.7636},
        {'id': 6, 'e_m': 1.835779, 'e_o_k': [0.149279, 0.119424, 0.095539, 0.076431, 0.061145, 0.048916], 'p_i': 80, 'u_i': 2.3342},
        {'id': 7, 'e_m': 7.737152, 'e_o_k': [0.690488, 0.552391, 0.441913, 0.353530, 0.282824], 'p_i': 80, 'u_i': 1.6627},
    ]
    B_BUDGET = 119.600003
    return processors, tasks, B_BUDGET
