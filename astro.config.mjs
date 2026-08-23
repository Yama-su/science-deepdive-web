// @ts-check
import { defineConfig } from 'astro/config';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { visit } from 'unist-util-visit';

const SITE = 'https://Yama-su.github.io';
const BASE = '/science-deepdive-web';

// public/ 配下の画像やページ内リンクは "/assets/..." のような絶対パスで
// Markdown記事に書く運用にしているため、GitHub Pagesのプロジェクトページ
// (サブパス配下)で公開してもリンク切れしないよう、ビルド時にBASEを前置する。
function rehypePrefixBase() {
  return (tree) => {
    visit(tree, 'element', (node) => {
      const attr = node.tagName === 'img' ? 'src' : node.tagName === 'a' ? 'href' : null;
      if (!attr) return;
      const value = node.properties?.[attr];
      if (typeof value === 'string' && value.startsWith('/') && !value.startsWith(BASE + '/')) {
        node.properties[attr] = BASE + value;
      }
    });
  };
}

// https://astro.build/config
export default defineConfig({
  site: SITE,
  base: BASE,
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex, rehypePrefixBase],
    shikiConfig: {
      theme: 'nord',
      wrap: true,
    },
  },
});
