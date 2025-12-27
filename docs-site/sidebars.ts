import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  problemsSidebar: [
    {
      type: 'doc',
      id: 'problems/intro',
      label: 'Overview',
    },
    {
      type: 'category',
      label: 'Part I: Thermodynamics',
      collapsed: false,
      items: [
        {
          type: 'category',
          label: 'Ch.1: First Law',
          items: [
            'problems/thermodynamics/first-law',
            'problems/thermodynamics/first-law-problems',
          ],
        },
        {
          type: 'category',
          label: 'Ch.2: Entropy & Second Law',
          items: [
            'problems/thermodynamics/entropy',
            'problems/thermodynamics/entropy-problems',
          ],
        },
        {
          type: 'category',
          label: 'Ch.3: Thermodynamic Functions',
          items: [
            'problems/thermodynamics/functions',
            'problems/thermodynamics/functions-problems',
          ],
        },
      ],
    },
    {
      type: 'category',
      label: 'Part II: Statistical Physics',
      collapsed: false,
      items: [
        'problems/statistical/intro',
        'problems/statistical/maxwell-boltzmann',
        'problems/statistical/ensemble-theory',
        'problems/statistical/quantum-statistics',
      ],
    },
    {
      type: 'category',
      label: 'PDF Resources',
      items: [
        'problems/pdf-index',
      ],
    },
  ],

  solutionsSidebar: [
    {
      type: 'doc',
      id: 'solutions/intro',
      label: 'Overview',
    },
    {
      type: 'category',
      label: 'LaTeX Solutions',
      collapsed: false,
      items: [
        {
          type: 'category',
          label: 'Chapter 1: First Law',
          items: [
            'solutions/latex/chapter1/problems-1001-1010',
            'solutions/latex/chapter1/problems-1011-1020',
            'solutions/latex/chapter1/problems-1021-1030',
          ],
        },
        {
          type: 'category',
          label: 'Chapter 2: Entropy',
          items: [
            'solutions/latex/chapter2/problems-1031-1040',
            'solutions/latex/chapter2/problems-1041-1050',
            'solutions/latex/chapter2/problems-1051-1060',
            'solutions/latex/chapter2/problems-1061-1072',
          ],
        },
        {
          type: 'category',
          label: 'Chapter 3: Functions',
          items: [
            'solutions/latex/chapter3/problems-1073-1085',
            'solutions/latex/chapter3/problems-1086-1100',
            'solutions/latex/chapter3/problems-1101-1105',
          ],
        },
      ],
    },
    {
      type: 'doc',
      id: 'solutions/formulas',
      label: 'Key Formulas',
    },
    {
      type: 'doc',
      id: 'solutions/constants',
      label: 'Physical Constants',
    },
  ],

  codeSidebar: [
    {
      type: 'doc',
      id: 'code/intro',
      label: 'Overview',
    },
    {
      type: 'category',
      label: 'Python Solutions',
      collapsed: false,
      items: [
        'code/python/chapter1-first-law',
        'code/python/chapter2-entropy',
        'code/python/chapter3-functions',
      ],
    },
    {
      type: 'doc',
      id: 'code/setup',
      label: 'Setup Guide',
    },
  ],
};

export default sidebars;
