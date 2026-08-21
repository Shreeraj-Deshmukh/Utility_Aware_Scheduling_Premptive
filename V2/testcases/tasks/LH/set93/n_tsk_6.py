"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.31998, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.31998, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.777998, 'e_o_k': [0.295233, 0.236186, 0.188949, 0.151159, 0.120927, 0.096742], 'p_i': 10, 'u_i': 3.2097},
        {'id': 1, 'e_m': 0.780808, 'e_o_k': [0.448005, 0.358404, 0.286723], 'p_i': 20, 'u_i': 3.3970},
        {'id': 2, 'e_m': 1.200644, 'e_o_k': [0.455618, 0.364494, 0.291595, 0.233276, 0.186621, 0.149297], 'p_i': 40, 'u_i': 4.0644},
        {'id': 3, 'e_m': 7.863449, 'e_o_k': [3.274878, 2.619902, 2.095922, 1.676737, 1.341390], 'p_i': 80, 'u_i': 4.4775},
        {'id': 4, 'e_m': 1.305076, 'e_o_k': [0.618938, 0.495151, 0.396121, 0.316896], 'p_i': 10, 'u_i': 1.6225},
        {'id': 5, 'e_m': 1.947436, 'e_o_k': [0.739009, 0.591207, 0.472966, 0.378373, 0.302698, 0.242158], 'p_i': 80, 'u_i': 1.5082},
    ]
    B_BUDGET = 88.319980
    return processors, tasks, B_BUDGET
