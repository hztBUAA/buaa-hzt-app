<template>
  <v-container>
    <!-- 搜索区域 -->
    <v-card class="mb-4">
      <v-card-text>
        <v-row>
          <v-col cols="12" sm="8">
            <v-text-field
              v-model="searchQuery"
              label="搜索内容"
              variant="outlined"
              prepend-inner-icon="mdi-magnify"
              clearable
              @keyup.enter="searchContent"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="4">
            <v-select
              v-model="selectedCategory"
              :items="categories"
              label="分类浏览"
              variant="outlined"
              density="comfortable"
              prepend-inner-icon="mdi-filter-variant"
            ></v-select>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <!-- 内容卡片 -->
    <v-row dense>
      <v-col v-for="c in filteredCards" :key="c.id" cols="12" sm="6">
        <v-card :subtitle="c.subtitle" :title="c.title" :text="c.content" class="h-100">
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-list-item class="w-100">
              <template v-slot:prepend>
                <v-avatar color="grey-darken-3" :image="c.avatar"></v-avatar>
              </template>

              <v-list-item-title>{{ c.title }}</v-list-item-title>
              <v-list-item-subtitle>{{ c.subtitle }}</v-list-item-subtitle>

              <template v-slot:append>
                <div justify="left">
                  <v-icon
                    class="me-1"
                    :color="c.liked ? 'red' : ''"
                    icon="mdi-heart"
                    @click="like(c.id)"
                  ></v-icon>
                  <span class="subheading me-2" aria-label="like">{{
                    c.likes
                  }}</span>
                  <span class="me-1">·</span>
                  <v-icon
                    class="me-1"
                    icon="mdi-share-variant"
                    @click="share"
                  ></v-icon>
                  <span class="subheading">45</span>
                </div>
              </template>
            </v-list-item>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <!-- 分页控件 -->
    <div class="d-flex justify-center mt-4">
      <v-pagination
        v-model="page"
        :length="3"
        rounded="circle"
      ></v-pagination>
    </div>

    <!-- 发现更多 -->
    <v-card class="mt-4 mb-4">
      <v-card-title class="d-flex align-center">
        <v-icon start icon="mdi-compass" class="mr-2"></v-icon>
        发现更多
      </v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="12" sm="4" v-for="(item, index) in discoverItems" :key="index">
            <v-card class="h-100" :to="item.route" hover>
              <v-img :src="item.image" height="150" cover></v-img>
              <v-card-title>{{ item.title }}</v-card-title>
              <v-card-subtitle>{{ item.description }}</v-card-subtitle>
            </v-card>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <!-- 底部导航链接 -->
    <v-btn
      color="primary"
      class="mt-3"
      @click="$router.push({ name: 'About' })"
      append-icon="mdi-arrow-right"
      text="了解更多"
    />
    <card7></card7>
  </v-container>
</template>

<script>
import axios from '@/plugins/axios';
import card7 from './card7.vue';
export default {
  data: () => ({
    cards: [],
    searchQuery: '',
    selectedCategory: '全部',
    categories: ['全部', '技术', '学习', '生活', '娱乐', '运动'],
    page: 1,
    discoverItems: [
      {
        title: '北航动态',
        description: '了解最新校园活动和新闻',
        image: 'https://picsum.photos/id/10/500/300',
        route: { name: 'About' }
      },
      {
        title: '家教服务',
        description: '寻找或提供家教服务',
        image: 'https://picsum.photos/id/20/500/300',
        route: { name: 'jiajiao' }
      },
      {
        title: '附近地点',
        description: '探索你周边的精彩',
        image: 'https://picsum.photos/id/30/500/300',
        route: { name: 'nearby' }
      }
    ]
  }),
  components: {
    card7
  },
  computed: {
    filteredCards() {
      if (!this.cards.length) return [];
      
      let result = [...this.cards];
      
      // 应用分类过滤
      if (this.selectedCategory !== '全部') {
        result = result.filter(card => card.category === this.selectedCategory);
      }
      
      // 应用搜索过滤
      if (this.searchQuery) {
        const query = this.searchQuery.toLowerCase();
        result = result.filter(card => 
          card.title.toLowerCase().includes(query) || 
          card.content.toLowerCase().includes(query) ||
          card.subtitle.toLowerCase().includes(query)
        );
      }
      
      return result;
    }
  },
  mounted() {
    this.fetchBlogs();
  },
  methods: {
    async fetchBlogs() {
      try {
        const response = await axios.get('posts/');
        this.cards = response.data.map((card) => ({
          ...card,
          avatar: this.getRandomAvatar(),
          liked: card.liked || false,
          // 添加随机分类用于演示
          category: this.getRandomCategory()
        }));
      } catch (error) {
        console.error('Error fetching blogs:', error);
      }
    },
    getRandomAvatar() {
      const seed = Math.random().toString(36).substring(7);
      return `https://api.dicebear.com/9.x/pixel-art/svg?seed=${seed}`;
    },
    getRandomCategory() {
      const categories = this.categories.filter(c => c !== '全部');
      return categories[Math.floor(Math.random() * categories.length)];
    },
    async like(cardId) {
      const card = this.cards.find((c) => c.id === cardId);
      if (card) {
        card.liked = !card.liked;
        card.likes += card.liked ? 1 : -1;
        try {
          await axios.post(`posts/${cardId}/likes`, { liked: card.liked });
        } catch (error) {
          console.error('Error updating like status:', error);
        }
      }
    },
    searchContent() {
      console.log('Searching for:', this.searchQuery);
      // 实际搜索已通过计算属性 filteredCards 实现
    },
    share() {
      console.log('分享内容');
    }
  }
};
</script>

<style scoped>
.h-100 {
  height: 100%;
}
</style>
