"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440015, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440015, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.264302, 'e_o_k': [0.210717, 0.168574], 'p_i': 10, 'u_i': 1.0216},
        {'id': 1, 'e_m': 5.402054, 'e_o_k': [0.664187, 0.531350, 0.425080], 'p_i': 20, 'u_i': 4.0085},
        {'id': 2, 'e_m': 19.622176, 'e_o_k': [2.412563, 1.930050, 1.544040], 'p_i': 40, 'u_i': 1.9931},
        {'id': 3, 'e_m': 7.815615, 'e_o_k': [0.960936, 0.768749, 0.614999], 'p_i': 80, 'u_i': 2.4773},
        {'id': 4, 'e_m': 0.295469, 'e_o_k': [0.030027, 0.024022, 0.019218, 0.015374], 'p_i': 80, 'u_i': 3.1022},
        {'id': 5, 'e_m': 3.479141, 'e_o_k': [0.282912, 0.226330, 0.181064, 0.144851, 0.115881, 0.092705], 'p_i': 40, 'u_i': 1.9821},
        {'id': 6, 'e_m': 13.844638, 'e_o_k': [1.702210, 1.361768, 1.089414], 'p_i': 80, 'u_i': 1.2190},
        {'id': 7, 'e_m': 12.119015, 'e_o_k': [1.231607, 0.985286, 0.788229, 0.630583], 'p_i': 80, 'u_i': 2.8489},
    ]
    B_BUDGET = 167.440015
    return processors, tasks, B_BUDGET
