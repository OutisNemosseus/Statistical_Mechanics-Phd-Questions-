import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

const config: Config = {
  title: 'Statistical Mechanics PhD Problems',
  tagline: 'Problems and Solutions on Thermodynamics and Statistical Mechanics',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://outisnemosseus.github.io',
  baseUrl: '/Statistical_Mechanics-Phd-Questions-/',

  organizationName: 'OutisNemosseus',
  projectName: 'Statistical_Mechanics-Phd-Questions-',

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
          editUrl:
            'https://github.com/OutisNemosseus/Statistical_Mechanics-Phd-Questions-/tree/main/docs-site/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.13.24/dist/katex.min.css',
      type: 'text/css',
      integrity:
        'sha384-odtC+0UGzzFL/6PNoE8rX/SPcQDXBJ+uRepguP4QkPCm2LBxH3FA3y+fKSiJ+AmM',
      crossorigin: 'anonymous',
    },
  ],

  themeConfig: {
    image: 'img/social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Statistical Mechanics',
      logo: {
        alt: 'Physics Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'problemsSidebar',
          position: 'left',
          label: 'Problems',
        },
        {
          type: 'docSidebar',
          sidebarId: 'solutionsSidebar',
          position: 'left',
          label: 'Solutions',
        },
        {
          type: 'docSidebar',
          sidebarId: 'codeSidebar',
          position: 'left',
          label: 'Code',
        },
        {
          href: 'https://github.com/OutisNemosseus/Statistical_Mechanics-Phd-Questions-',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Documentation',
          items: [
            {
              label: 'Problems Overview',
              to: '/docs/problems/intro',
            },
            {
              label: 'LaTeX Solutions',
              to: '/docs/solutions/intro',
            },
            {
              label: 'Python Code',
              to: '/docs/code/intro',
            },
          ],
        },
        {
          title: 'Topics',
          items: [
            {
              label: 'First Law of Thermodynamics',
              to: '/docs/problems/thermodynamics/first-law',
            },
            {
              label: 'Entropy & Second Law',
              to: '/docs/problems/thermodynamics/entropy',
            },
            {
              label: 'Thermodynamic Functions',
              to: '/docs/problems/thermodynamics/functions',
            },
          ],
        },
        {
          title: 'Resources',
          items: [
            {
              label: 'GitHub Repository',
              href: 'https://github.com/OutisNemosseus/Statistical_Mechanics-Phd-Questions-',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Statistical Mechanics PhD Problems. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['python', 'latex', 'matlab', 'bash'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
