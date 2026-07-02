import mdx from '@astrojs/mdx';
import { defineConfig } from 'astro/config';
import icon from 'astro-icon';
import vercel from '@astrojs/vercel';
import tailwind from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
	site: 'https://astrotmp.vercel.app',
	output: 'server',
	adapter: vercel({
		webAnalytics: { enabled: true },
	}),
	vite: {
		plugins: [tailwind()],
		ssr: {
			external: ['@libsql/client'],
		},
	},
	integrations: [icon(), mdx()],
});
