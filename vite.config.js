import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

const { resolve } = require('path');

const r = (path) => resolve(__dirname, path);

// https://vitejs.dev/config/
export default defineConfig({
  root: r('client'),
  base: '',
  resolve: {
    alias: {
      '~': path.resolve(__dirname, './client'),
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
