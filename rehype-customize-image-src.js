// rehype-customize-image-src.js
import { visit } from 'unist-util-visit';

export default function rehypeCustomizeImageSrc() {
  return (tree) => {
    visit(tree, 'raw', (node) => {
      // 使用正则表达式匹配<img>标签
      const imgRegex = /<img src="(https:\/\/cdn\.fliggy\.com\/[^"]+|https:\/\/gw\.alipayobjects\.com\/[^"]+)"/g;
      // 替换匹配到的<img>标签的src属性
      if (imgRegex.test(node.value)) {
        node.value = node.value.replace(imgRegex, (match, p1) => {
          return `<img src="${p1}?x-oss-process=image/resize,w_3600/format,webp"`;
        });
      }
    });
  };
}
