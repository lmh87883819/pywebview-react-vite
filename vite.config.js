import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { resolve } from 'path';
import * as url from 'url';

const dirname = url.fileURLToPath(new URL('.', import.meta.url));
const r = (path) => resolve(dirname, path);

// https://vitejs.dev/config/
export default defineConfig({
  root: r('client'),
  base: '',
  resolve: {
    alias: {
      '~': r('client'),
    },
  },
  build: {
    emptyOutDir: true,
    outDir: r('gui'),
    rollupOptions: {
      input: {
        index: r('client/index.html'),
      },
    },
  },
  plugins: [
    react({
      babel: {
        plugins: ['babel-plugin-macros', 'babel-plugin-styled-components'],
      },
    }),
  ],
});
