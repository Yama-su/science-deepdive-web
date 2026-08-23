import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    id: z.string(),
    title: z.string(),
    slug: z.string(),
    category: z.enum(['physics', 'chemistry', 'mathematics']),
    tags: z.array(z.string()),
    target_audience: z.array(
      z.enum(['小学生', '中高生', '大学生・一般', '研究者']),
    ),
    reading_time_minutes: z.number(),
    page_count_a4: z.number().optional(),
    published_at: z.coerce.date(),
    author: z.object({
      name: z.string(),
      avatar: z.string(),
    }),
    seo: z.object({
      meta_title: z.string(),
      meta_description: z.string(),
      og_image: z.string(),
    }),
    lead_excerpt: z.string(),
    table_of_contents: z.boolean().default(true),
    math: z.boolean().default(true),
    syntax_highlight: z.boolean().default(true),
    has_affiliate_links: z.boolean().default(false),
    draft: z.boolean().default(false),
  }),
});

export const collections = { blog };
