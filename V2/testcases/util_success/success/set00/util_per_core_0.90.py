"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279992, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279992, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.546252, 'e_o_k': [0.558965, 0.447172, 0.357738], 'p_i': 10, 'u_i': 2.8465},
        {'id': 1, 'e_m': 1.729569, 'e_o_k': [0.154352, 0.123482, 0.098785, 0.079028, 0.063223], 'p_i': 20, 'u_i': 3.7661},
        {'id': 2, 'e_m': 9.210105, 'e_o_k': [1.132390, 0.905912, 0.724730], 'p_i': 40, 'u_i': 1.0932},
        {'id': 3, 'e_m': 13.482426, 'e_o_k': [1.096346, 0.877077, 0.701662, 0.561329, 0.449063, 0.359251], 'p_i': 80, 'u_i': 2.8740},
        {'id': 4, 'e_m': 28.368271, 'e_o_k': [3.487902, 2.790322, 2.232257], 'p_i': 80, 'u_i': 4.9324},
        {'id': 5, 'e_m': 1.858156, 'e_o_k': [0.228462, 0.182769, 0.146216], 'p_i': 20, 'u_i': 4.5939},
        {'id': 6, 'e_m': 3.186679, 'e_o_k': [0.531113, 0.424891], 'p_i': 10, 'u_i': 2.0087},
        {'id': 7, 'e_m': 7.514742, 'e_o_k': [0.763693, 0.610955, 0.488764, 0.391011], 'p_i': 80, 'u_i': 1.3714},
    ]
    B_BUDGET = 215.279992
    return processors, tasks, B_BUDGET
