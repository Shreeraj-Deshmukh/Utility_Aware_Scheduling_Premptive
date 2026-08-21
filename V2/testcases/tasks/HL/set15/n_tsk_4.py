"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.240758, 'e_o_k': [0.630765, 0.504612, 0.403690, 0.322952, 0.258361], 'p_i': 10, 'u_i': 3.0940},
        {'id': 1, 'e_m': 3.393953, 'e_o_k': [0.504812, 0.403850, 0.323080, 0.258464, 0.206771], 'p_i': 20, 'u_i': 2.1175},
        {'id': 2, 'e_m': 0.541246, 'e_o_k': [0.073354, 0.058683, 0.046946, 0.037557, 0.030046, 0.024037], 'p_i': 40, 'u_i': 3.6512},
        {'id': 3, 'e_m': 15.415630, 'e_o_k': [2.611049, 2.088839, 1.671071, 1.336857], 'p_i': 80, 'u_i': 2.9125},
    ]
    B_BUDGET = 110.400009
    return processors, tasks, B_BUDGET
