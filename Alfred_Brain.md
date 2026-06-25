<!-- ⚠️ 此文件由 sync_alfred_prompts.py 自动生成，请勿手动编辑 -->
<!-- 修改请编辑 Alfred snippets，然后运行脚本重新生成 -->

# Alfred AI Prompt - Brain

### 1通用000_通用思考(7/10)

	请先理解我的问题，如有歧义请先提问澄清。然后分步骤思考并给出推理过程，最后总结答案。使用中文回答。

### 1通用002_下一步

简单描述下之前做了什么，下一步你建议做什么？

### 2问000_理清问的问题

使用 ask-first skill。

### 2问001_不停的询问问题

使用 grill-with-docs skill 开始。

### 2问002_抽象问题

I don't know this area of code well. Go up a layer of abstraction. Give me a map of all the relevant modules and callers, using the project's domain glossary vocabulary.

### 3学新东西001_领域寓言讲解

我希望你从 {cursor} 领域里选一个大概研究生水平的概念。然后我希望你通过写一个寓言的方式，间接地把这个概念完整讲出来。最好一直到快结尾时，人才会慢慢意识到这个概念究竟是什么。然后在故事之后，再补一段解释，把你刚才真正要讲的概念说清楚。

### 3学新东西002_圆桌讨论

使用 ljg-roundtable skill ，讨论一下 {cursor}

### 3学新东西004_问好几层再书写

先用 ljg-think skill 分析，再用 ljg-plain skill 把问题和分析内容写成 markdown 格式的文章。

### 4理解001_12岁男孩听懂

使用 ljg-plain skill 解释一下。

### 4理解002_苏格拉底考试

【指令】回答后即刻切换为[苏格拉底严师模式]：请基于核心逻辑向我抛出1个具有陷阱性的场景反问或意图挖掘（测试我是否真懂）；必须暂停等待我回复；收到回复后请评分(0-10)并毫不留情地指出我的思维盲区，循环追问直到我完全通透。
