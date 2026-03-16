// @ts-check
import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'astro/config';
import icon from 'astro-icon';
import editableRegions from '@cloudcannon/editable-regions/astro-integration';

import mdx from '@astrojs/mdx';

// https://astro.build/config
export default defineConfig({
    site: 'https://astrotmp.vercel.app',
    vite: {
        plugins: [tailwindcss()],
    },
    integrations: [editableRegions(), icon(), mdx()],
});