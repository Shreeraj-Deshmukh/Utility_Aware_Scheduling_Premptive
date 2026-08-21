"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439987, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439987, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.023138, 'e_o_k': [0.371697, 0.297358, 0.237886], 'p_i': 10, 'u_i': 2.7456},
        {'id': 1, 'e_m': 2.885372, 'e_o_k': [0.354759, 0.283807, 0.227046], 'p_i': 20, 'u_i': 1.4781},
        {'id': 2, 'e_m': 6.186471, 'e_o_k': [0.503063, 0.402451, 0.321960, 0.257568, 0.206055, 0.164844], 'p_i': 40, 'u_i': 4.2271},
        {'id': 3, 'e_m': 7.098129, 'e_o_k': [0.721355, 0.577084, 0.461667, 0.369334], 'p_i': 80, 'u_i': 2.1613},
        {'id': 4, 'e_m': 1.703720, 'e_o_k': [0.173142, 0.138514, 0.110811, 0.088649], 'p_i': 10, 'u_i': 3.4475},
        {'id': 5, 'e_m': 2.179260, 'e_o_k': [0.363210, 0.290568], 'p_i': 10, 'u_i': 3.7603},
        {'id': 6, 'e_m': 3.095028, 'e_o_k': [0.380536, 0.304429, 0.243543], 'p_i': 10, 'u_i': 4.2692},
        {'id': 7, 'e_m': 0.489134, 'e_o_k': [0.081522, 0.065218], 'p_i': 40, 'u_i': 2.3975},
    ]
    B_BUDGET = 167.439987
    return processors, tasks, B_BUDGET
