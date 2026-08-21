"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199997, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199997, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.958028, 'e_o_k': [0.326338, 0.261070], 'p_i': 10, 'u_i': 1.5356},
        {'id': 1, 'e_m': 5.553420, 'e_o_k': [0.925570, 0.740456], 'p_i': 20, 'u_i': 4.5907},
        {'id': 2, 'e_m': 17.544703, 'e_o_k': [1.782998, 1.426399, 1.141119, 0.912895], 'p_i': 40, 'u_i': 2.9431},
        {'id': 3, 'e_m': 14.836194, 'e_o_k': [1.206430, 0.965144, 0.772115, 0.617692, 0.494154, 0.395323], 'p_i': 80, 'u_i': 4.4457},
        {'id': 4, 'e_m': 7.105885, 'e_o_k': [0.722143, 0.577714, 0.462171, 0.369737], 'p_i': 40, 'u_i': 2.2657},
        {'id': 5, 'e_m': 8.210434, 'e_o_k': [0.834394, 0.667515, 0.534012, 0.427210], 'p_i': 40, 'u_i': 3.5479},
        {'id': 6, 'e_m': 1.404165, 'e_o_k': [0.172643, 0.138115, 0.110492], 'p_i': 10, 'u_i': 2.5301},
        {'id': 7, 'e_m': 30.330535, 'e_o_k': [3.082371, 2.465897, 1.972718, 1.578174], 'p_i': 80, 'u_i': 3.4603},
    ]
    B_BUDGET = 239.199997
    return processors, tasks, B_BUDGET
