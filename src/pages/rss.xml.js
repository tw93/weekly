import rss from "@astrojs/rss";
export async function GET() {
  let allPosts = import.meta.glob("./posts/*.md", { eager: true });
  let posts = Object.values(allPosts);

  posts = posts.sort((a, b) => {
    const getPostNumber = (url) =>
      parseInt(url.split("/posts/")[1].split("-")[0]);
    return getPostNumber(b.url) - getPostNumber(a.url);
  });

  // Only 12 are kept
  posts = posts.slice(0, 12);

  // 处理 Markdown 内容，确保视频内容不被过滤
  const processContent = async (item) => {
    const content = await item.compiledContent();
    // 如果需要额外处理来确保视频内容被保留，可以在这里添加逻辑
    return content;
  };
  
  return rss({
    title: "潮流周刊",
    description: "记录工程师 Tw93 的不枯燥生活",
    site: "https://weekly.tw93.fun/",
    customData: `<image><url>https://gw.alipayobjects.com/zos/k/qv/coffee-2-icon.png</url></image><follow_challenge><feedId>41147805276726275</feedId><userId>42909600318350336</userId></follow_challenge>`,
    items: await Promise.all(
      posts.map(async (item) => {
        const [issueNumber, issueTitle] = item.url
          .split("/posts/")[1]
          .split("-");
        const title = `第${issueNumber}期 - ${issueTitle}`;
        return {
          link: item.url,
          title,
          description: await processContent(item),
          pubDate: item.frontmatter.date,
        };
      }),
    ),
  });
}
