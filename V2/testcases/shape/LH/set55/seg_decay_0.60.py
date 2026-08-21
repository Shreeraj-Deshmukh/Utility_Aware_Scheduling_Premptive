"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.181209, 'e_o_k': [0.693849, 0.416309, 0.249786, 0.149871, 0.089923, 0.053954], 'p_i': 10, 'u_i': 4.5134},
        {'id': 1, 'e_m': 0.909186, 'e_o_k': [0.649418, 0.389651, 0.233791], 'p_i': 20, 'u_i': 4.5874},
        {'id': 2, 'e_m': 1.009200, 'e_o_k': [0.720857, 0.432514, 0.259509], 'p_i': 40, 'u_i': 2.7347},
        {'id': 3, 'e_m': 5.488802, 'e_o_k': [3.920573, 2.352344, 1.411406], 'p_i': 80, 'u_i': 4.9671},
        {'id': 4, 'e_m': 2.719998, 'e_o_k': [1.651630, 0.990978, 0.594587, 0.356752, 0.214051], 'p_i': 80, 'u_i': 4.8761},
        {'id': 5, 'e_m': 0.142051, 'e_o_k': [0.091393, 0.054836, 0.032901, 0.019741], 'p_i': 10, 'u_i': 2.5248},
        {'id': 6, 'e_m': 0.727869, 'e_o_k': [0.636885, 0.382131], 'p_i': 40, 'u_i': 4.9532},
        {'id': 7, 'e_m': 3.047121, 'e_o_k': [1.960464, 1.176278, 0.705767, 0.423460], 'p_i': 40, 'u_i': 2.2979},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
