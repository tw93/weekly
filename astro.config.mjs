import fs from "fs";
import dayjs from "dayjs";
import tailwind from "@astrojs/tailwind";
import remarkBreaks from "remark-breaks";

import { defineConfig } from "astro/config";
import { parse } from "node-html-parser";
import { SITE } from "./src/config";
import rehypeImage from "./rehype-image.js";

// Markdown 配置 - 控制换行行为
const markdownConfig = {
  hardBreaks: true, // 设置为 true 启用硬换行 (类似 CMARK_OPT_HARDBREAKS)
  gfm: true,
  smartypants: true,
  allowDangerousHtml: true
};

const DEFAULT_FORMAT = "YYYY/MM/DD";
const WEEKLY_REPO_NAME = "tw93/weekly";
const START_DATE = "2022-10-10";

function formatDate(date) {
  return dayjs(date).format(DEFAULT_FORMAT);
}

function getFileCreateDate(filePath) {
  return formatDate(fs.statSync(filePath).birthtime);
}

function getWeeklyDate(num) {
  return num < 100
    ? formatDate(dayjs(START_DATE).subtract(100 - num, "week"))
    : getFileCreateDate(filePath);
}

function getTwitterImage(num) {
  return num >= 110 ? `https://weekly.tw93.fun/assets/${num}.jpg` : undefined;
}

function defaultLayoutPlugin() {
  return function (tree, file) {
    const filePath = file.history[0];
    const { frontmatter } = file.data.astro;
    frontmatter.layout = "@layouts/post.astro";

    if (tree.children[0]?.value && !frontmatter.image) {
      const imageElement = parse(tree.children[0].value).querySelector("img");
      frontmatter.image = imageElement.getAttribute("src");
    }

    if (tree.children[1]?.children[1]?.value) {
      frontmatter.description = tree.children[1].children[1].value;
    }

    frontmatter.description = frontmatter.description || SITE.description;
    frontmatter.image = frontmatter.image || SITE.image;

    if (!frontmatter.date) {
      const postNumber = filePath.split(/[\/\\]posts[\/\\]/)[1]?.split("-")[0];
      frontmatter.date =
        SITE.repo === WEEKLY_REPO_NAME
          ? getWeeklyDate(postNumber)
          : getFileCreateDate(filePath);
    }

    if (SITE.repo === WEEKLY_REPO_NAME) {
      const postNumber = filePath.split(/[\/\\]posts[\/\\]/)[1]?.split("-")[0];
      frontmatter.socialImage = getTwitterImage(postNumber);
    }
  };
}

export default defineConfig({
  prefetch: true,
  integrations: [tailwind()],
  markdown: {
    remarkPlugins: [
      defaultLayoutPlugin,
      // 根据配置决定是否启用硬换行
      ...(markdownConfig.hardBreaks ? [remarkBreaks] : [])
    ],
    rehypePlugins: [rehypeImage],
    remarkRehype: {
      handlers: {},
      allowDangerousHtml: markdownConfig.allowDangerousHtml
    },
    gfm: markdownConfig.gfm,
    smartypants: markdownConfig.smartypants
  },
});
