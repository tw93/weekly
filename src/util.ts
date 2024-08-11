// Helper function to extract and decode the title part from the URL
const extractTitlePart = (currentPage: string) => {
  return decodeURIComponent(currentPage.split('/posts/')[1]);
};

// Convert to title
export const parseTitle = (currentPage: string) => {
  const oldTitle = extractTitlePart(currentPage);
  let title = `第${oldTitle.split('-')[0]}期 - ${oldTitle.split('-')[1]}`;
  if (title.endsWith('/')) {
    title = title.slice(0, -1);
  }
  return title;
};

// Get the current article number.
export const getIndex = (currentPage: string) => {
  const oldTitle = extractTitlePart(currentPage);
  return parseInt(oldTitle.split('-')[0]);
};

// Sort all articles.
export const sortPosts = (allPosts: any) => {
  return allPosts.sort((a, b) => {
    const getIndexFromUrl = (url: string) => parseInt(extractTitlePart(url).split('-')[0]);
    return getIndexFromUrl(b.url) - getIndexFromUrl(a.url);
  });
};
