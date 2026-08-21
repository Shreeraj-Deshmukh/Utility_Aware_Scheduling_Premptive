"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120007, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120007, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.153831, 'e_o_k': [0.358972, 0.287177], 'p_i': 10, 'u_i': 1.5356},
        {'id': 1, 'e_m': 6.108762, 'e_o_k': [1.018127, 0.814502], 'p_i': 20, 'u_i': 4.5907},
        {'id': 2, 'e_m': 19.299173, 'e_o_k': [1.961298, 1.569038, 1.255231, 1.004185], 'p_i': 40, 'u_i': 2.9431},
        {'id': 3, 'e_m': 16.319814, 'e_o_k': [1.327073, 1.061658, 0.849327, 0.679461, 0.543569, 0.434855], 'p_i': 80, 'u_i': 4.4457},
        {'id': 4, 'e_m': 7.816473, 'e_o_k': [0.794357, 0.635486, 0.508389, 0.406711], 'p_i': 40, 'u_i': 2.2657},
        {'id': 5, 'e_m': 9.031478, 'e_o_k': [0.917833, 0.734266, 0.587413, 0.469931], 'p_i': 40, 'u_i': 3.5479},
        {'id': 6, 'e_m': 1.544582, 'e_o_k': [0.189908, 0.151926, 0.121541], 'p_i': 10, 'u_i': 2.5301},
        {'id': 7, 'e_m': 33.363588, 'e_o_k': [3.390609, 2.712487, 2.169989, 1.735992], 'p_i': 80, 'u_i': 3.4603},
    ]
    B_BUDGET = 263.120007
    return processors, tasks, B_BUDGET
