import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import react from '@astrojs/react';
import { parse } from 'node-html-parser';
import dayjs from 'dayjs';

function defaultLayoutPlugin() {
  return function (tree, file) {
    const headHtml = tree.children[0].value;
    let image;
    if (headHtml) {
      image = parse(headHtml).querySelector('img').getAttribute('src');
    }
    file.data.astro.frontmatter.layout = '@layouts/post.astro';
    file.data.astro.frontmatter.pic = image;
    file.data.astro.frontmatter.desc = tree.children[1].children[1].value;

    const num = file.history[0].split('/posts/')[1].split('-')[0];
    if (num < 99) {
      file.data.astro.frontmatter.date = dayjs('2022-10-10')
        .subtract(100 - num, 'week')
        .format('YYYY/MM/DD');
    } else if (num == 99) {
      file.data.astro.frontmatter.date = '2022-10-10';
    } else {
      file.data.astro.frontmatter.date = dayjs().format('YYYY/MM/DD');
    }
  };
}

// https://astro.build/config
export default defineConfig({
  integrations: [react(), tailwind()],
  markdown: {
    remarkPlugins: [defaultLayoutPlugin],
    extendDefaultPlugins: true,
  },
});
