<template>
  <v-container>
    <v-carousel hide-delimiters>
      <v-carousel-item
        v-for="(item, i) in images"
        :key="i"
        :src="item.src"
        cover
      ></v-carousel-item>
    </v-carousel>
    <v-timeline align="start"  justify="center">
      <v-timeline-item
        v-for="(year, i) in years"
        :key="i"
        :dot-color="year.color"
        size="small"
      >
        <template v-slot:opposite>
          <div
            :class="`pt-1 headline font-weight-bold text-${year.color}`"
            v-text="year.year"
          ></div>
        </template>
        <div>
          <h2
            :class="`mt-n1 headline font-weight-light mb-4 text-${year.color}`"
          >
            {{ year.title }}
          </h2>
          <div>
            {{ year.content }}
          </div>
        </div>
      </v-timeline-item>
    </v-timeline>
  </v-container>
</template>
<script>
export default {
  data: () => ({
    years: [
      {
        color: 'cyan',
        year: '2021.9',
        title: '进入北航',
        content: '在信息大类开始卷啦~'
      },
      {
        color: 'green',
        year: '2022.6',
        title: '卷进计算机学院',
        content:
          '继续卷，平庸过了一年，发现保研无望，体会到各科分数无法拿到顶尖的无力感~'
      },
      {
        color: 'pink',
        year: '2023.6',
        title: '接触了web相关的技术',
        content:
          '数据库课设做了一些东西，ruby程序设计也是体会到敏捷开发的成绩感，开始不断学习相关的技术，但总是学不精，也开始逐渐了解前端的概念，尽管现在都还是不太懂css的细节'
      },
      {
        color: 'amber',
        year: '2024.6',
        title: '参加实习',
        content:
          '远程实习：为此担心过，也中途害怕过；最后也坚持下来，总结了一些生存之道。'
      },
      {
        color: 'orange',
        year: '2024.8',
        title: '心血来潮',
        content:
          '想用django加上vuetify加快自己开发web app的节奏，想把自己的想法和平时生活中思考的一些好点子和信息紫苑进行分享————大学这几年，深刻体会到信息差的重要性，也希望自己能够分享一些有用的信息~'
      }
    ],
    images: []
  }),
  created() {
    this.loadImages();
  },
  methods: {
    loadImages() {
      const requireContext = require.context('./', false, /\.(png|jpe?g|svg)$/);
      this.images = requireContext.keys().map(file => ({
        src: requireContext(file)
      }));
    }
  }
};
</script>
