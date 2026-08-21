"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "segments", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "segments", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.153313, 'e_o_k': [0.072710, 0.058168, 0.046534, 0.037227], 'p_i': 10, 'u_i': 2.6246},
        {'id': 1, 'e_m': 0.148369, 'e_o_k': [0.070365, 0.056292, 0.045033, 0.036027], 'p_i': 20, 'u_i': 1.9533},
        {'id': 2, 'e_m': 2.270223, 'e_o_k': [1.076664, 0.861331, 0.689065, 0.551252], 'p_i': 40, 'u_i': 2.5491},
        {'id': 3, 'e_m': 7.275677, 'e_o_k': [3.450524, 2.760420, 2.208336, 1.766669], 'p_i': 80, 'u_i': 2.9783},
        {'id': 4, 'e_m': 2.680502, 'e_o_k': [1.271241, 1.016992, 0.813594, 0.650875], 'p_i': 20, 'u_i': 1.6186},
        {'id': 5, 'e_m': 1.468106, 'e_o_k': [0.696256, 0.557005, 0.445604, 0.356483], 'p_i': 40, 'u_i': 1.1221},
        {'id': 6, 'e_m': 0.569881, 'e_o_k': [0.270269, 0.216215, 0.172972, 0.138378], 'p_i': 20, 'u_i': 1.0173},
        {'id': 7, 'e_m': 0.303269, 'e_o_k': [0.143827, 0.115061, 0.092049, 0.073639], 'p_i': 10, 'u_i': 4.7591},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
