// @ts-check
import { defineConfig } from 'astro/config';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// https://astro.build/config
export default defineConfig({
  // TODO: 公開前に実際のユーザー名に置き換える。
  // リポジトリ名を <username>.github.io にしてルート公開する構成を前提としており、
  // base設定は不要（サブパス公開にすると画像/リンクパスの調整が別途必要になるため非推奨）。
  site: 'https://your-username.github.io',
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
    shikiConfig: {
      theme: 'nord',
      wrap: true,
    },
  },
});
