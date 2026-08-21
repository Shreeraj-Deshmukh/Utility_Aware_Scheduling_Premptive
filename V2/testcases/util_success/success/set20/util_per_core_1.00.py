"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200014, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200014, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.294178, 'e_o_k': [0.527973, 0.422378, 0.337903], 'p_i': 10, 'u_i': 2.1494},
        {'id': 1, 'e_m': 2.676222, 'e_o_k': [0.329044, 0.263235, 0.210588], 'p_i': 20, 'u_i': 4.2411},
        {'id': 2, 'e_m': 19.573814, 'e_o_k': [1.989209, 1.591367, 1.273094, 1.018475], 'p_i': 40, 'u_i': 1.9272},
        {'id': 3, 'e_m': 28.369138, 'e_o_k': [2.883043, 2.306434, 1.845147, 1.476118], 'p_i': 80, 'u_i': 4.8493},
        {'id': 4, 'e_m': 0.468305, 'e_o_k': [0.078051, 0.062441], 'p_i': 10, 'u_i': 3.1752},
        {'id': 5, 'e_m': 12.045284, 'e_o_k': [1.480978, 1.184782, 0.947826], 'p_i': 80, 'u_i': 4.0094},
        {'id': 6, 'e_m': 11.809791, 'e_o_k': [1.200182, 0.960146, 0.768116, 0.614493], 'p_i': 80, 'u_i': 3.0877},
        {'id': 7, 'e_m': 4.955851, 'e_o_k': [0.402993, 0.322395, 0.257916, 0.206333, 0.165066, 0.132053], 'p_i': 20, 'u_i': 2.5780},
    ]
    B_BUDGET = 239.200014
    return processors, tasks, B_BUDGET
