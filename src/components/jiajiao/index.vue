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
                  :lazy-src="`https://picsum.photos/10/6?image=${i * n * 5 + 10}`"
                  :src="`https://picsum.photos/500/300?image=${i * n * 5 + 10}`"
                  height="205"
                  cover
                ></v-img>
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
  data: () => ({
    tab: null
  }),
  methods: {
    go2profile() {
      this.$router.push({ name: 'profile' });
    },
    go2card9() {
      this.$router.push({ name: 'Post9' });
    },
    go2knowledge() {
      this.$router.push({ name: 'knowledge' });
    }
  }
};
</script>
