import rss from '@astrojs/rss';

let allPosts =  import.meta.glob('./posts/*.md', { eager: true });
let posts = Object.values(allPosts);
posts = posts.sort((a, b) => {
  return (
    parseInt(b.url.split('/posts/')[1].split('-')[0]) -
    parseInt(a.url.split('/posts/')[1].split('-')[0])
  );
});


export const get = () =>
  rss({
    title: '潮流周刊',
    description: '记录 Tw93 潮流前端的日常生活',
    site: 'https://weekly.tw93.fun/',
    items: posts.map((item) => {
      const url = item.url;
      const oldTitle = url.split('/posts/')[1];
      const title =
        '第' + oldTitle.split('-')[0] + '期 - ' + oldTitle.split('-')[1];
      return {
        link: url,
        title,
        pubDate: item.frontmatter.date,
      };
    }),
  });
