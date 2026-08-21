"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 32, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "freq", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 32, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "freq", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 1.0]},
        {'id': 1, 'frequencies': [0.4, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.498376, 'e_o_k': [0.207558, 0.166046, 0.132837, 0.106270, 0.085016], 'p_i': 10, 'u_i': 4.1058},
        {'id': 1, 'e_m': 0.297010, 'e_o_k': [0.170415, 0.136332, 0.109066], 'p_i': 20, 'u_i': 1.5782},
        {'id': 2, 'e_m': 0.891273, 'e_o_k': [0.371187, 0.296950, 0.237560, 0.190048, 0.152038], 'p_i': 40, 'u_i': 1.2072},
        {'id': 3, 'e_m': 2.329510, 'e_o_k': [0.970167, 0.776134, 0.620907, 0.496726, 0.397380], 'p_i': 80, 'u_i': 4.8515},
        {'id': 4, 'e_m': 0.437113, 'e_o_k': [0.165875, 0.132700, 0.106160, 0.084928, 0.067942, 0.054354], 'p_i': 20, 'u_i': 3.3809},
        {'id': 5, 'e_m': 9.162615, 'e_o_k': [4.345414, 3.476331, 2.781065, 2.224852], 'p_i': 80, 'u_i': 4.9290},
        {'id': 6, 'e_m': 0.776607, 'e_o_k': [0.604028, 0.483222], 'p_i': 20, 'u_i': 1.8035},
        {'id': 7, 'e_m': 1.086925, 'e_o_k': [0.515479, 0.412383, 0.329907, 0.263925], 'p_i': 10, 'u_i': 3.4846},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
