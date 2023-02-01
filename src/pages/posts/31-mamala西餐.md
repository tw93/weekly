<img src=https://gw.alipayobjects.com/zos/k/6f/L3GWS7.jpg width=600/>  

<small>封面图摄于 mamala 家的牛排，挺不错的一家西餐厅，窗外风景极其不错，适合在有仪式感的日子去吃一次~ </small>  

> **记录每周看到的前端潮流技术，筛选后用接地气方式发布于此，关注此专栏可以及时收到更新~**  

## 前端技术

**JavaScript Debugger 原理揭秘**  
<https://juejin.cn/post/6961790494514872333>  
代码写完会运行一下看下效果，开发的时候我们更多都是通过 debugger 来单步或断点运行，你知道它的原理吗？

**携程火车票 Flutter 最佳实践**  
<https://mp.weixin.qq.com/s/VP6WEQkEel3W4tdo3ThYDw>  
原来携程也在弄 Flutter，将历史过程中一些经验沉淀还是很赞的。

**聊聊 Deno 的那些事**  
<https://mp.weixin.qq.com/s/6tXZYQ8SBvIrhhsZEKVZqQ>  
政采云前端关于 Deno 的介绍文章，很适合不懂的同学了解和练手。

**算法平台在线服务体系的演进与实践**  
<https://tech.meituan.com/2021/05/13/turing-os-online-serving.html>  
美团技术的图灵平台功能和技术原理的介绍，很干货，值得一读。

## 开源资讯

**rust-raspberrypi-OS-tutorials：树莓派教程**  
<https://github.com/rust-embedded/rust-raspberrypi-OS-tutorials>  
真心很潮流，有空很有必要去玩一玩这个东西。  
<img src=https://cdn.fliggy.com/upic/ZzivqL.gif width=600/>  

**playground-macos：用前端实现 macOS's GUI**  
<https://github.com/Renovamen/playground-macos>  
挺牛逼的，可访问 <https://portfolio.zxh.io/> 查看。  
<img src=https://cdn.fliggy.com/upic/Dmuo5D.gif width=600/>  

**getx：Flutter 中的状态管理工具**  
<https://github.com/jonataslaw/getx/blob/master/README.zh-cn.md>  
GetX 是 Flutter 上的一个轻量且强大的解决方案：高性能的状态管理、智能的依赖注入和便捷的路由管理。  
<img src=https://cdn.fliggy.com/upic/ORcYpo.jpg width=600/>  

**slidev：用 Markdown 来快速写 PPT**  
<https://github.com/slidevjs/slidev>  
写 ppt 很容易浪费太多事情，更好的内部表达方式应该是语雀，假如需要对外分享，但不想麻烦，可以试试 Anthony Fu 的新作品。  
<img src=https://cdn.fliggy.com/upic/asxsQu.gif width=600/>  

**terminal-kit：命令行工具包**  
<https://github.com/cronvel/terminal-kit>  
可以用命令行工作写出类似这样的效果。  
<img src=https://cdn.fliggy.com/upic/B5rzQI.gif width=600/>  

**zx：一个更好的写脚本的工具**  
<https://github.com/google/zx>  

```shell
#!/usr/bin/env zx

await $`cat package.json | grep name`

let branch = await $`git branch --show-current`
await $`dep deploy --branch=${branch}`

await Promise.all([
  $`sleep 1; echo 1`,
  $`sleep 2; echo 2`,
  $`sleep 3; echo 3`,
])

let name = 'foo bar'
await $`mkdir /tmp/${name}`
```

## 他山之石

**关于自由**  
https://www.v2ex.com/t/775584?p=1
V2EX 上面关于自由的一个讨论，里面有几个观点值得一读，比知乎接地气。

**Babel is used by millions, so why are we running out of money?**  
<https://babeljs.io/blog/2021/05/10/funding-update.html>  
Babel 被大家使用了数亿次，居然快没钱了，你敢信，吃个瓜（原作者吐槽维护者 Henry Zhu 拿钱不写代码，十几万刀的年薪去年只解决了 12 个 issue 和 29 个 PR...）。

**96% of US users opt out of app tracking in iOS 14.5, analytics find**  
<https://arstechnica.com/gadgets/2021/05/96-of-us-users-opt-out-of-app-tracking-in-ios-14-5-analytics-find/>  
ios 在 14.5 的时候做了限制跟踪的选择，当前美国有 96%都选择了拒绝 app 跟踪，不知中国用户数据如何，这个能力对于拉新下载类广告影响很大。

**软件工程的最大难题**  
<http://www.ruanyifeng.com/blog/2021/05/scaling-problem.html>  
阮一峰最近一篇关于软件工程由于人数增加后造成难题的文章，包括提供了不少团队解耦的方法。

**从长征 5B 再入的新闻谈起**  
<https://mp.weixin.qq.com/s/Dx0lWSGRZGZIrA8pAkn2ug>  
一篇严肃的科普文，关于长征 5B（CZ-5B）火箭的非受控再入的问题解释。
