<template>
  <v-container>
    <v-app-bar>
      <v-app-bar-title>家教页面</v-app-bar-title>
    </v-app-bar>

    <v-sheet align="center">
      <v-text-field
        width="70%"
        label="搜索"
        variant="outlined"
        prepend-inner-icon="mdi-magnify"
      >
      </v-text-field>
    </v-sheet>

    <v-card align="center" flat>
      <v-btn
        size="large"
        prepend-icon="mdi-book"
        stacked
        variant="text"
        class="me-12"
        @click.stop="go2knowledge"
      >
        知识频道
      </v-btn>
      <v-btn
        size="large"
        prepend-icon="mdi-account"
        stacked
        variant="text"
        class="me-12"
      >
        查看附近
      </v-btn>
      <v-btn
        size="large"
        prepend-icon="mdi-message"
        stacked
        variant="text"
        class="me-12"
      >
        最近消息
      </v-btn>
    </v-card>

    <v-card flat>
      <v-tabs v-model="tab" align-tabs="center" color="deep-purple-accent-4">
        <v-tab :value="1">Landscape</v-tab>
        <v-tab :value="2">City</v-tab>
        <v-tab :value="3">Abstract</v-tab>
      </v-tabs>

      <v-tabs-window v-model="tab">
        <v-tabs-window-item v-for="n in 3" :key="n" :value="n">
          <v-container fluid>
            <v-row>
              <v-col v-for="i in 6" :key="i" cols="12" md="4">
                <v-img
                  :src="getJiajiaoPic(i, n)"
                  height="205"
                  cover
                >
                  <template v-slot:placeholder>
                    <v-row class="fill-height ma-0" align="center" justify="center">
                      <v-progress-circular indeterminate color="primary"></v-progress-circular>
                    </v-row>
                  </template>
                </v-img>
              </v-col>
            </v-row>
          </v-container>
        </v-tabs-window-item>
      </v-tabs-window>
    </v-card>
    <v-btn @click="go2profile">go to other's profile</v-btn>
    <v-btn @click="go2card9">go to card9</v-btn>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      tab: 1
    }
  },
  methods: {
    go2profile() {
      this.$router.push('/profile/')
    },
    go2card9() {
      this.$router.push('/card9/')
    },
    go2knowledge() {
      this.$router.push('/jiajiao/knowledge/')
    },
    getJiajiaoPic(index, tab) {
      // 创建一个包含 Vuetify 提供的可靠 CDN 图片的数组
      const imageGroups = [
        // 第一个标签页的图片集
        [
          'https://cdn.vuetifyjs.com/images/cards/house.jpg',
          'https://cdn.vuetifyjs.com/images/cards/road.jpg',
          'https://cdn.vuetifyjs.com/images/cards/plane.jpg',
          'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg',
          'https://cdn.vuetifyjs.com/images/cards/docks.jpg',
          'https://cdn.vuetifyjs.com/images/parallax/material.jpg'
        ],
        // 第二个标签页的图片集
        [
          'https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg',
          'https://cdn.vuetifyjs.com/images/backgrounds/bg.jpg',
          'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg',
          'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
          'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
          'https://cdn.vuetifyjs.com/images/parallax/material2.jpg'
        ],
        // 第三个标签页的图片集
        [
          'https://cdn.vuetifyjs.com/images/cards/kitchen.png',
          'https://cdn.vuetifyjs.com/images/cards/hotel.jpg',
          'https://cdn.vuetifyjs.com/images/cards/vacation.jpg',
          'https://cdn.vuetifyjs.com/images/cards/drop.jpg',
          'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg',
          'https://cdn.vuetifyjs.com/images/cards/mountain.jpg'
        ]
      ];
      
      // 根据标签和索引返回相应的图片
      const tabIndex = tab - 1; // 标签从1开始，数组从0开始
      return imageGroups[tabIndex][index % 6];
    }
  }
};
</script>
