import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const changelog = defineCollection({
	loader: glob({ pattern: '**/*.md', base: './src/content/changelog' }),
	schema: z.object({
		title: z.string(),
		version: z
			.string()
			.regex(
				/^v\d+\.\d+\.\d+(-[a-zA-Z0-9]+)?$/,
				'Must be a valid version string e.g., v2.4.0',
			),
		date: z.date(),
		type: z.enum([
			'Feature',
			'Improvement',
			'Bugfix',
			'Security',
			'Infrastructure',
		]),
		tags: z.array(z.string()).optional(),
		banner_image: z.string().optional(),
		author: z.string().optional(),
	}),
});

const roadmap = defineCollection({
	loader: glob({ pattern: '**/*.md', base: './src/content/roadmap' }),
	schema: z.object({
		title: z.string(),
		status: z.enum([
			'Under Consideration',
			'Planned',
			'In Development',
			'Launched',
		]),
		category: z.enum([
			'UI/UX',
			'Analytics',
			'AI',
			'Security',
			'Infrastructure',
			'Core API',
			'Webhooks',
		]),
		assignees: z
			.array(
				z.object({
					name: z.string(),
					avatar: z.string().optional(),
					initials: z.string().max(2),
				}),
			)
			.optional(),
		progress: z.number().min(0).max(100).optional(),
		priority: z.enum(['Low', 'Medium', 'High', 'Critical']).optional(),
	}),
});

const docs = defineCollection({
	loader: glob({ pattern: '**/*.mdx', base: './src/content/docs' }),
	schema: z.object({
		title: z.string(),
		description: z.string(),
		category: z.string(),
		author: z.string().optional(),
		updated_at: z.date().optional(),
		featured_image: z.string().optional(),
	}),
});

export const collections = {
	changelog,
	roadmap,
	docs,
};
