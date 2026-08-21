"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280009, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280009, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.810420, 'e_o_k': [0.072324, 0.057860, 0.046288, 0.037030, 0.029624], 'p_i': 10, 'u_i': 2.4242},
        {'id': 1, 'e_m': 7.123787, 'e_o_k': [0.635750, 0.508600, 0.406880, 0.325504, 0.260403], 'p_i': 20, 'u_i': 1.3497},
        {'id': 2, 'e_m': 1.300932, 'e_o_k': [0.132208, 0.105767, 0.084613, 0.067691], 'p_i': 40, 'u_i': 4.8973},
        {'id': 3, 'e_m': 23.458226, 'e_o_k': [1.907545, 1.526036, 1.220829, 0.976663, 0.781330, 0.625064], 'p_i': 80, 'u_i': 4.4724},
        {'id': 4, 'e_m': 6.391800, 'e_o_k': [0.785877, 0.628702, 0.502961], 'p_i': 20, 'u_i': 4.7464},
        {'id': 5, 'e_m': 0.852460, 'e_o_k': [0.104811, 0.083849, 0.067079], 'p_i': 10, 'u_i': 2.8305},
        {'id': 6, 'e_m': 19.078324, 'e_o_k': [3.179721, 2.543777], 'p_i': 40, 'u_i': 4.0659},
        {'id': 7, 'e_m': 12.417872, 'e_o_k': [1.009780, 0.807824, 0.646259, 0.517007, 0.413606, 0.330885], 'p_i': 80, 'u_i': 3.0796},
    ]
    B_BUDGET = 215.280009
    return processors, tasks, B_BUDGET
