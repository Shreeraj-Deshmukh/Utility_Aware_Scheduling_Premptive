"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439997, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439997, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.384020, 'e_o_k': [0.047216, 0.037772, 0.030218], 'p_i': 10, 'u_i': 1.2368},
        {'id': 1, 'e_m': 2.004375, 'e_o_k': [0.162989, 0.130391, 0.104313, 0.083450, 0.066760, 0.053408], 'p_i': 20, 'u_i': 2.8306},
        {'id': 2, 'e_m': 19.708020, 'e_o_k': [2.423117, 1.938494, 1.550795], 'p_i': 40, 'u_i': 2.9234},
        {'id': 3, 'e_m': 13.003345, 'e_o_k': [1.598772, 1.279018, 1.023214], 'p_i': 80, 'u_i': 3.7707},
        {'id': 4, 'e_m': 4.660465, 'e_o_k': [0.573008, 0.458406, 0.366725], 'p_i': 20, 'u_i': 1.9627},
        {'id': 5, 'e_m': 5.724917, 'e_o_k': [0.954153, 0.763322], 'p_i': 40, 'u_i': 4.9296},
        {'id': 6, 'e_m': 0.049660, 'e_o_k': [0.004038, 0.003231, 0.002584, 0.002068, 0.001654, 0.001323], 'p_i': 40, 'u_i': 4.5772},
        {'id': 7, 'e_m': 2.287493, 'e_o_k': [0.204143, 0.163315, 0.130652, 0.104521, 0.083617], 'p_i': 10, 'u_i': 4.4816},
    ]
    B_BUDGET = 167.439997
    return processors, tasks, B_BUDGET
