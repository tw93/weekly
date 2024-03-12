// rehype-customize-image-src.js
import { visit } from 'unist-util-visit';

export default function rehypeCustomizeImageSrc() {
  return (tree) => {
    visit(tree, 'raw', (node) => {
      // Match <img> tags using regular expressions
      const imgRegex = /<img src="(https:\/\/cdn\.fliggy\.com\/[^"]+|https:\/\/gw\.alipayobjects\.com\/[^"]+)"/g;
      // Replace the src attribute of the matched <img> tag
      if (imgRegex.test(node.value)) {
        node.value = node.value.replace(imgRegex, (match, p1) => {
          return `<img src="${p1}?x-oss-process=image/resize,w_3600/format,webp"`;
        });
      }
    });
  };
}
