// rehype-customize-image-src.js
import { visit } from 'unist-util-visit';

export default function rehypeCustomizeImageSrc() {
	return (tree) => {
		visit(tree, 'raw', (node) => {
			// Match <img> tags excluding .gif and .svg images using regular expressions
			const imgRegex =
				/<img src="(https:\/\/cdn\.fliggy\.com\/[^"]+|https:\/\/gw\.alipayobjects\.com\/[^"]+)(?<!\.gif|\.svg|\.GIF|\.SVG)"/g;
			// Replace the src attribute of the matched <img> tag
			if (imgRegex.test(node.value)) {
				node.value = node.value.replace(imgRegex, (match, p1) => {
					// Check if the URL already contains query parameters
					const separator = p1.includes('?') ? '&' : '?';
					return `<img src="${p1}${separator}x-oss-process=image/resize,w_3600/format,webp"`;
				});
			}
		});
	};
}
