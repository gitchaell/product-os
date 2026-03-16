// @ts-check

import mdx from '@astrojs/mdx';
import editableRegions from '@cloudcannon/editable-regions/astro-integration';
import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'astro/config';
import icon from 'astro-icon';

// https://astro.build/config
export default defineConfig({
	site: 'https://astrotmp.vercel.app',
	vite: {
		plugins: [tailwindcss()],
	},
	integrations: [editableRegions(), icon(), mdx()],
});
