import { sql } from 'drizzle-orm';
import { integer, sqliteTable, text } from 'drizzle-orm/sqlite-core';

export const products = sqliteTable('products', {
	id: text('id').primaryKey(),
	name: text('name').notNull(),
	description: text('description').notNull(),
	createdAt: integer('created_at', { mode: 'timestamp' })
		.notNull()
		.default(sql`(strftime('%s', 'now'))`),
});

export const changelogEntries = sqliteTable('changelog_entries', {
	id: text('id').primaryKey(),
	productId: text('product_id')
		.notNull()
		.references(() => products.id),
	title: text('title').notNull(),
	description: text('description'),
	version: text('version').notNull(),
	date: integer('date', { mode: 'timestamp' }).notNull(),
	type: text('type').notNull(),
	content: text('content').notNull(),
});

export const roadmapEntries = sqliteTable('roadmap_entries', {
	id: text('id').primaryKey(),
	productId: text('product_id')
		.notNull()
		.references(() => products.id),
	title: text('title').notNull(),
	status: text('status').notNull(),
	category: text('category').notNull(),
	progress: integer('progress'),
	priority: text('priority'),
	content: text('content'),
});

export const docEntries = sqliteTable('doc_entries', {
	id: text('id').primaryKey(),
	productId: text('product_id')
		.notNull()
		.references(() => products.id),
	title: text('title').notNull(),
	description: text('description').notNull(),
	category: text('category').notNull(),
	author: text('author'),
	updatedAt: integer('updated_at', { mode: 'timestamp' }),
	featuredImage: text('featured_image'),
	content: text('content').notNull(),
});
