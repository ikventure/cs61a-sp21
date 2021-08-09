test = {
  'name': 'ebnf-pycombinator',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'add()',
          'choices': [
            'add(1, 2)',
            'sub(3, 4)',
            'add(sub(1, 2))',
            'add()'
          ],
          'hidden': False,
          'locked': False,
          'question': 'Which of the following expressions would NOT be parsable according to this BNF?'
        },
        {
          'answer': 'add(10, 20)',
          'choices': [
            'add(a, b)',
            'add("a", "b")',
            'add(10, 20)',
            'All of these'
          ],
          'hidden': False,
          'locked': False,
          'question': 'Which of these expressions WOULD be parsable according to this BNF?'
        },
        {
          'answer': 'FUNCNAME: "add" | "mul" | "sub"',
          'choices': [
            'pycomb_call: func "(" arg ("," arg)* ")"',
            'arg: pycomb_call | NUMBER',
            'func: FUNCNAME',
            'FUNCNAME: "add" | "mul" | "sub"'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What line of the BNF should we modify to add support for a "div" operation?'
        },
        {
          'answer': 'both FUNCNAME and NUMBER',
          'choices': [
            'pycomb_call',
            'arg',
            'func',
            'FUNCNAME',
            'NUMBER',
            'both FUNCNAME and NUMBER',
            'All of these'
          ],
          'hidden': False,
          'locked': False,
          'question': 'Which of the following are considered a terminal?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
