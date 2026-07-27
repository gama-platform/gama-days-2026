import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://gama-platform.org',
  base: '/gama-days-2026',
  trailingSlash: 'always',
  redirects: {
    '/CFP.html': '/gama-days-2026/#call-for-papers',
    '/CFParticipation.html': '/gama-days-2026/#call-for-papers',
    '/program.html': '/gama-days-2026/',
    '/keynotes.html': '/gama-days-2026/',
    '/openfora.html': '/gama-days-2026/',
    '/committee.html': '/gama-days-2026/committee/',
  },
});
