// Convert to title
export const parseTitle = (currentPage: string) => {
	const oldTitle = decodeURIComponent(currentPage.split('/posts/')[1]);
	let title = '第' + oldTitle.split('-')[0] + '期 - ' + oldTitle.split('-')[1];
	if (title.slice(-1) == '/') {
		title = title.substring(0, title.length - 1);
	}
	return title;
};

// Get the current article number.
export const getIndex = (currentPage: string) => {
	const oldTitle = decodeURIComponent(currentPage.split('/posts/')[1]);
	return parseInt(oldTitle.split('-')[0]);
};

// Sort all articles.
export const sortPosts = (allPosts: any) => {
	return allPosts.sort((a, b) => {
		return parseInt(b.url.split('/posts/')[1].split('-')[0]) - parseInt(a.url.split('/posts/')[1].split('-')[0]);
	});
};
