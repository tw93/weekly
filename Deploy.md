# 开发教程

### 一、准备工作

1. Fork 本仓库到自己 Github 仓库下
2. 将代码 Clone 到本地，并确定已经安装好 node / npm 环境
3. 执行 `npm i` 安装模块依赖，然后执行 `npm run dev` 看是否可以跑起来

### 二、文档格式说明

1. 假如可以跑起来，可以去 `src/pages/posts` 只留一个 markdown 文件用于格式参考，或者加入自己的文件，文档说明如下
2. 第一行的文档建议是一个图片的展示，这样代码会自动取第一行为你的头图，也可以已通过 front matter 规范用 pic 字段表示，假如都没有填写，会使用默认的图片
3. 中间空一行，第三行是文档的描述，可以用 `small` 标签包裹，用于文字的描述部分，也可用 front matter 规范中 desc 字段表示，假如没有，会使用默认描述
4. 关于文档的时间，也是默认通过 node 取到文档的创建时间，假如不想要这个，也可用 front matter 规范中 date 字段表示
5. 关于文章的标题，可以用 `数字-标题` 的方式，方便很多地方的统一处理

### 部署说明

1. 由于 astro 最终打包出来是静态的文件，按理所有支持资源部署的平台都支持的，比如说 Github Pages、Vercel、Netlify 都可以的，此次重点推荐用 Vercel 部署，很简单高效，其他的平台可以参考 [astro](https://docs.astro.build/en/guides/deploy/) 文档，以下说明的是 Vercel 的部署教程
2. 首先确保 Fork 的代码已经传到 Github 中了, 然后进入 [Vercel](https://vercel.com/new) 选择 `Continue with GitHub`，将对应的仓库 import 进去
3. 导入后，确定 FRAMEWORK PRESET 是 Astro（[截图](https://gw.alipayobjects.com/zos/k/ic/0BffKE.png)），一般会默认选中，没有的话请选择这个，选择后，点击 Deploy 即可，稍等片刻，等待部署
4. 过了一会儿部署完成了，参考[截图](https://gw.alipayobjects.com/zos/k/e3/QLS7dG.png)位置，就是你的域名地址好了，点击进去就可以访问了，是不是很简单
5. 由于评论系统使用的是我自己的 key，假如需要自用，辛苦参考 [giscus](https://giscus.app/zh-CN) 自己去配置一个，这样就和你的绑定了

### 最后

1. 假如你不是程序员同学，遇到不懂的名词，请谷歌解决，这个过程很有趣，假如还是不行，可以直接问问程序员，或者直接提交 issue 来问我
2. 期待你玩得开心，也欢迎给我提建议，或者推荐「潮流周刊」给你的朋友
