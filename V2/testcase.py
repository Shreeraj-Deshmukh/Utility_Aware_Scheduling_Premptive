import math

def testcase():
    processors = [
        {'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], 'id': 0},
        {'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], 'id': 1},
    ]

    tasks = [
        {
            'id': 0,
            'e_m': 2.451382,
            'e_o_k': [1.12341, 1.45892],
            'p_i': 10,
            'u_i': 2.15
        },
        {
            'id': 1,
            'e_m': 3.672109,
            'e_o_k': [2.10583, 1.34122, 1.05234],
            'p_i': 20,
            'u_i': 3.42
        },
        {
            'id': 2,
            'e_m': 4.105742,
            'e_o_k': [2.95123, 2.41876],
            'p_i': 20,
            'u_i': 1.88
        },
        {
            'id': 3,
            'e_m': 6.321855,
            'e_o_k': [4.12098, 2.85432, 2.11234],
            'p_i': 40,
            'u_i': 2.55
        },
        {
            'id': 4,
            'e_m': 8.443911,
            'e_o_k': [5.01234, 3.88452, 2.76123, 1.95432],
            'p_i': 60,
            'u_i': 3.10
        },
        {
            'id': 5,
            'e_m': 14.892341,
            'e_o_k': [9.85123, 7.62345, 5.99234],
            'p_i': 120,
            'u_i': 2.90
        }
    ]

    B_BUDGET = 400  # Generous budget to allow the solver to maximize optional segments
    
    return processors, tasks, B_BUDGET