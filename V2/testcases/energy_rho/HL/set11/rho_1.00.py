"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399985, "H": 80, "J": 30, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.399985, "H": 80, "J": 30, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.067561, 'e_o_k': [0.158788, 0.127030, 0.101624, 0.081299, 0.065039], 'p_i': 10, 'u_i': 4.6830},
        {'id': 1, 'e_m': 6.103602, 'e_o_k': [1.695445, 1.356356], 'p_i': 20, 'u_i': 2.4027},
        {'id': 2, 'e_m': 4.537756, 'e_o_k': [1.260488, 1.008390], 'p_i': 40, 'u_i': 2.7203},
        {'id': 3, 'e_m': 4.054946, 'e_o_k': [0.549558, 0.439646, 0.351717, 0.281374, 0.225099, 0.180079], 'p_i': 80, 'u_i': 2.4000},
        {'id': 4, 'e_m': 0.349178, 'e_o_k': [0.096994, 0.077595], 'p_i': 20, 'u_i': 2.9059},
        {'id': 5, 'e_m': 0.690991, 'e_o_k': [0.141597, 0.113277, 0.090622], 'p_i': 10, 'u_i': 3.1411},
        {'id': 6, 'e_m': 5.436589, 'e_o_k': [0.920832, 0.736665, 0.589332, 0.471466], 'p_i': 80, 'u_i': 3.1206},
        {'id': 7, 'e_m': 2.776704, 'e_o_k': [0.568997, 0.455197, 0.364158], 'p_i': 40, 'u_i': 4.7030},
    ]
    B_BUDGET = 110.399985
    return processors, tasks, B_BUDGET
