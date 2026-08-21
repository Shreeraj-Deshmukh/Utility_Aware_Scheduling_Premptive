"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760018, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760018, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.625678, 'e_o_k': [0.104280, 0.083424], 'p_i': 10, 'u_i': 4.4926},
        {'id': 1, 'e_m': 1.547212, 'e_o_k': [0.190231, 0.152185, 0.121748], 'p_i': 20, 'u_i': 3.2922},
        {'id': 2, 'e_m': 1.626959, 'e_o_k': [0.271160, 0.216928], 'p_i': 40, 'u_i': 3.7450},
        {'id': 3, 'e_m': 9.770239, 'e_o_k': [0.992910, 0.794328, 0.635463, 0.508370], 'p_i': 80, 'u_i': 4.8771},
        {'id': 4, 'e_m': 0.211130, 'e_o_k': [0.035188, 0.028151], 'p_i': 20, 'u_i': 4.0203},
        {'id': 5, 'e_m': 0.908788, 'e_o_k': [0.092357, 0.073885, 0.059108, 0.047287], 'p_i': 10, 'u_i': 3.4418},
        {'id': 6, 'e_m': 0.888711, 'e_o_k': [0.109268, 0.087414, 0.069931], 'p_i': 10, 'u_i': 4.8003},
        {'id': 7, 'e_m': 1.069633, 'e_o_k': [0.131512, 0.105210, 0.084168], 'p_i': 10, 'u_i': 3.9154},
    ]
    B_BUDGET = 71.760018
    return processors, tasks, B_BUDGET
