"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.35999, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.35999, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.724835, 'e_o_k': [0.384208, 0.307366, 0.245893, 0.196714, 0.157372, 0.125897], 'p_i': 10, 'u_i': 4.5134},
        {'id': 1, 'e_m': 3.636743, 'e_o_k': [0.447141, 0.357712, 0.286170], 'p_i': 20, 'u_i': 4.5874},
        {'id': 2, 'e_m': 4.036800, 'e_o_k': [0.496328, 0.397062, 0.317650], 'p_i': 40, 'u_i': 2.7347},
        {'id': 3, 'e_m': 21.955209, 'e_o_k': [2.699411, 2.159529, 1.727623], 'p_i': 80, 'u_i': 4.9671},
        {'id': 4, 'e_m': 10.879994, 'e_o_k': [0.970966, 0.776773, 0.621418, 0.497134, 0.397708], 'p_i': 80, 'u_i': 4.8761},
        {'id': 5, 'e_m': 0.568203, 'e_o_k': [0.057744, 0.046195, 0.036956, 0.029565], 'p_i': 10, 'u_i': 2.5248},
        {'id': 6, 'e_m': 2.911475, 'e_o_k': [0.485246, 0.388197], 'p_i': 40, 'u_i': 4.9532},
        {'id': 7, 'e_m': 12.188485, 'e_o_k': [1.238667, 0.990934, 0.792747, 0.634198], 'p_i': 40, 'u_i': 2.2979},
    ]
    B_BUDGET = 191.359990
    return processors, tasks, B_BUDGET
