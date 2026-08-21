"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279986, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279986, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.886891, 'e_o_k': [0.477896, 0.382317, 0.305854], 'p_i': 10, 'u_i': 2.7456},
        {'id': 1, 'e_m': 3.709764, 'e_o_k': [0.456119, 0.364895, 0.291916], 'p_i': 20, 'u_i': 1.4781},
        {'id': 2, 'e_m': 7.954034, 'e_o_k': [0.646796, 0.517436, 0.413949, 0.331159, 0.264927, 0.211942], 'p_i': 40, 'u_i': 4.2271},
        {'id': 3, 'e_m': 9.126166, 'e_o_k': [0.927456, 0.741965, 0.593572, 0.474857], 'p_i': 80, 'u_i': 2.1613},
        {'id': 4, 'e_m': 2.190498, 'e_o_k': [0.222612, 0.178089, 0.142471, 0.113977], 'p_i': 10, 'u_i': 3.4475},
        {'id': 5, 'e_m': 2.801906, 'e_o_k': [0.466984, 0.373587], 'p_i': 10, 'u_i': 3.7603},
        {'id': 6, 'e_m': 3.979322, 'e_o_k': [0.489261, 0.391409, 0.313127], 'p_i': 10, 'u_i': 4.2692},
        {'id': 7, 'e_m': 0.628886, 'e_o_k': [0.104814, 0.083851], 'p_i': 40, 'u_i': 2.3975},
    ]
    B_BUDGET = 215.279986
    return processors, tasks, B_BUDGET
