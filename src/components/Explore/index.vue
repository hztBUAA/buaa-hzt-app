<template>
  <v-container>
    <!-- 顶部搜索区域 - 添加背景色和内边距 -->
    <v-card class="mb-5 rounded-lg" elevation="2">
      <v-card-text class="pa-4">
        <v-row>
          <v-col cols="12" sm="8">
            <v-text-field
              v-model="searchQuery"
              label="搜索内容"
              variant="outlined"
              prepend-inner-icon="mdi-magnify"
              clearable
              density="comfortable"
              @keyup.enter="searchContent"
              bg-color="white"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="4" class="d-flex align-center">
            <v-select
              v-model="selectedCategory"
              :items="categories"
              label="分类浏览"
              variant="outlined"
              density="comfortable"
              prepend-inner-icon="mdi-filter-variant"
              bg-color="white"
            ></v-select>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <!-- 视图切换器 -->
    <div class="d-flex justify-space-between align-center mb-4">
      <h2 class="text-h5 font-weight-medium">探索内容</h2>
      <v-btn-toggle v-model="viewType" color="primary" mandatory density="comfortable">
        <v-btn value="grid" icon="mdi-view-grid"></v-btn>
        <v-btn value="list" icon="mdi-view-list"></v-btn>
      </v-btn-toggle>
    </div>

    <!-- 空状态展示 -->
    <v-card v-if="!filteredCards.length" class="my-5 text-center pa-6" elevation="0" border>
      <v-icon size="64" color="grey-lighten-1">mdi-text-search</v-icon>
      <h3 class="text-h5 mt-4 text-grey-darken-1">暂无内容</h3>
      <p class="text-body-1 text-medium-emphasis mt-2">
        没有找到符合当前筛选条件的内容，请尝试更换关键词或分类
      </p>
      <v-btn color="primary" class="mt-4" prepend-icon="mdi-refresh" @click="resetFilters">
        重置筛选条件
      </v-btn>
    </v-card>

    <!-- 内容网格视图 -->
    <v-row v-else-if="viewType === 'grid'" dense>
      <v-col v-for="c in filteredCards" :key="c.id" cols="12" sm="6" md="4">
        <v-card class="h-100 card-hover" elevation="2">
          <v-img
            :src="getCardImage(c.id)"
            height="200"
            cover
          >
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular indeterminate color="primary"></v-progress-circular>
              </v-row>
            </template>
          </v-img>
          <v-card-title class="text-truncate">{{ c.title }}</v-card-title>
          <v-card-subtitle>{{ c.subtitle }}</v-card-subtitle>
          <v-card-text class="text-truncate-3">{{ c.content }}</v-card-text>
          <v-card-actions>
            <v-list-item class="w-100 card-footer">
              <template v-slot:prepend>
                <v-avatar size="36" color="grey-darken-3" :image="getRandomAvatar()">
                  <template v-slot:placeholder>
                    <v-row class="fill-height ma-0" align="center" justify="center">
                      <v-progress-circular indeterminate color="grey-lighten-3" size="20"></v-progress-circular>
                    </v-row>
                  </template>
                </v-avatar>
              </template>
              <v-list-item-subtitle>{{ c.category }}</v-list-item-subtitle>
              <template v-slot:append>
                <div>
                  <v-icon
                    class="me-1"
                    :color="c.liked ? 'red' : ''"
                    icon="mdi-heart"
                    @click="like(c.id)"
                  ></v-icon>
                  <span class="text-caption me-2">{{ c.likes }}</span>
                </div>
              </template>
            </v-list-item>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <!-- 内容列表视图 -->
    <v-list v-else lines="two" class="rounded-lg">
      <v-list-item
        v-for="c in filteredCards"
        :key="c.id"
        :title="c.title"
        :subtitle="c.subtitle"
        rounded="lg"
        class="mb-2"
      >
        <template v-slot:prepend>
          <v-avatar size="36" color="grey-darken-3" :image="getRandomAvatar()">
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular indeterminate color="grey-lighten-3" size="20"></v-progress-circular>
              </v-row>
            </template>
          </v-avatar>
        </template>
        <template v-slot:append>
          <div class="d-flex align-center">
            <v-icon
              size="small"
              class="me-1"
              :color="c.liked ? 'red' : ''"
              icon="mdi-heart"
              @click.stop="like(c.id)"
            ></v-icon>
            <span class="text-caption me-2">{{ c.likes }}</span>
            <v-chip size="small" :color="getCategoryColor(c.category)" text-color="white">
              {{ c.category }}
            </v-chip>
          </div>
        </template>
      </v-list-item>
    </v-list>

    <!-- 分页控件 -->
    <div class="d-flex justify-center mt-6">
      <v-pagination
        v-model="page"
        :length="2"
        rounded="circle"
        @update:model-value="handlePageChange"
        width="auto"
        class="pagination-container"
      ></v-pagination>
    </div>

    <!-- 发现更多卡片 -->
    <h2 class="text-h5 font-weight-medium mt-8 mb-4">发现更多</h2>
    <v-row>
      <v-col cols="12" sm="4" v-for="(item, index) in discoverItems" :key="index">
        <v-card class="h-100 card-hover" :to="item.route" hover elevation="3">
          <v-img :src="item.image" height="160" cover gradient="to bottom, rgba(0,0,0,0) 60%, rgba(0,0,0,0.7)">
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular indeterminate color="primary"></v-progress-circular>
              </v-row>
            </template>
          </v-img>
          <div class="position-relative">
            <v-card-title class="pb-1">{{ item.title }}</v-card-title>
            <v-card-subtitle>{{ item.description }}</v-card-subtitle>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn variant="text" color="primary" :to="item.route">
                查看
                <v-icon end>mdi-arrow-right</v-icon>
              </v-btn>
            </v-card-actions>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from '@/plugins/axios';
import card7 from './card7.vue';

// 防止 ResizeObserver 循环错误的函数
const debounce = (callback, delay) => {
  let tid;
  return function (...args) {
    const ctx = this;
    tid && clearTimeout(tid);
    tid = setTimeout(() => {
      callback.apply(ctx, args);
    }, delay);
  };
};

// 重写 ResizeObserver 以防止循环错误
if (typeof window !== 'undefined' && window.ResizeObserver) {
  const originalResizeObserver = window.ResizeObserver;
  window.ResizeObserver = class ResizeObserver extends originalResizeObserver {
    constructor(callback) {
      super(debounce(callback, 20));
    }
  };
}

export default {
  data: () => ({
    cards: [
      // 添加一些默认数据,避免空白状态
      {
        id: 1,
        title: '北航新闻',
        subtitle: '校园动态',
        content: '北京航空航天大学举办了一系列科技创新活动,吸引了众多学生参与...',
        likes: 45,
        liked: false,
        // avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
        category: '学习'
      },
      {
        id: 2,
        title: 'Vue.js 学习笔记',
        subtitle: '前端技术',
        content: 'Vue.js 是一个流行的前端框架,它的响应式系统和组件化设计使得开发更加高效...',
        likes: 56,
        liked: true,
        // avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
        category: '技术'
      },
      {
        id: 3,
        title: '校园周边美食推荐',
        subtitle: '生活指南',
        content: '分享几家北航周边好吃不贵的餐厅,让你的校园生活更加丰富多彩...',
        likes: 78,
        liked: false,
        // avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
        // avatar: this.getRandomAvatar(),
        category: '生活'
      }
    ],
    searchQuery: '',
    selectedCategory: '全部',
    categories: ['全部', '技术', '学习', '生活', '娱乐', '运动'],
    page: 1,
    resizeTimeout: null,
    discoverItems: [
      {
        title: '我的动态',
        description: '了解最新的我',
        image: 'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg',
        route: { name: 'About' }
      },
      {
        title: '家教服务',
        description: '寻找或提供家教服务',
        image: 'https://cdn.vuetifyjs.com/images/cards/house.jpg',
        route: { name: 'jiajiao' }
      },
      {
        title: '附近地点',
        description: '探索你周边的精彩',
        image: 'https://cdn.vuetifyjs.com/images/cards/road.jpg',
        route: { name: 'nearby' }
      }
    ],
    viewType: 'grid',
    loading: false
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
    
    // 使用 requestAnimationFrame 来避免频繁触发 resize 事件
    this.debouncedResize = debounce(this.handleResize, 200);
    window.addEventListener('resize', this.debouncedResize);
  },
  beforeUnmount() {
    // 移除事件监听器
    window.removeEventListener('resize', this.debouncedResize);
  },
  methods: {
    handleResize() {
      console.log('窗口大小已调整');
    },
    async fetchBlogs() {
      try {
        this.loading = true;
        // 模拟网络延迟
        setTimeout(async () => {
          try {
            const response = await axios.get('posts/');
            // 如果 API 返回数据,使用 API 数据
            if (response.data && response.data.length > 0) {
              this.cards = response.data.map((card) => ({
                ...card,
                avatar: this.getRandomAvatar(),
                liked: card.liked || false,
                category: this.getRandomCategory()
              }));
            }
            // 否则保留默认数据
          } catch (error) {
            console.error('Error fetching blogs:', error);
            // 保留默认数据,不需要额外操作
          } finally {
            this.loading = false;
          }
        }, 500);
      } catch (error) {
        console.error('Error in fetchBlogs:', error);
        this.loading = false;
      }
    },
    getRandomAvatar() {
      const seed = Math.random().toString(36).substring(7);
      // 只使用卡通风格的头像
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
          // 使用 try-catch 包裹,防止 API 不可用时报错
          await axios.post(`posts/${cardId}/likes`, { liked: card.liked })
            .catch(error => console.warn('API not available for likes:', error));
        } catch (error) {
          console.error('Error updating like status:', error);
        }
      }
    },
    async searchContent() {
      console.log('Searching for:', this.searchQuery);
      // 添加搜索功能的实现
      this.loading = true;
      try {
        // 简单实现：使用本地过滤，真实场景可能需要调用API
        // 这里只是为了演示，实际应用中可以调用后端API
        setTimeout(() => {
          // 如果搜索结果为空，尝试重置到默认状态
          if (!this.filteredCards.length && this.cards.length === 0) {
            this.resetFilters();
          }
          this.loading = false;
        }, 500);
      } catch (error) {
        console.error('搜索内容时出错:', error);
        this.loading = false;
      }
    },
    share() {
      console.log('分享内容');
    },
    handlePageChange(newPage) {
      // if(this.page >= 3) return;
      if (this.page === newPage) return; // 防止相同页码重复触发
      this.page = newPage;
      // 使用 setTimeout 确保状态更新后再滚动
      setTimeout(() => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }, 10);
    },
    resetFilters() {
      this.searchQuery = '';
      this.selectedCategory = '全部';
    },
    getCategoryColor(category) {
      const colorMap = {
        '技术': 'indigo',
        '学习': 'blue',
        '生活': 'green',
        '娱乐': 'purple',
        '运动': 'orange'
      };
      return colorMap[category] || 'grey';
    },
    getCardImage(id) {
      const images = [
        'https://cdn.vuetifyjs.com/images/cards/house.jpg',
        'https://cdn.vuetifyjs.com/images/cards/road.jpg',
        'https://cdn.vuetifyjs.com/images/cards/plane.jpg',
        'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg',
        'https://cdn.vuetifyjs.com/images/cards/docks.jpg'
      ];
      return images[id % images.length];
    }
  }
};
</script>

<style scoped>
.h-100 {
  height: 100%;
}
.pagination-container {
  max-width: 100%;
  overflow-x: auto;
  margin: 0 auto;
  width: max-content;
}
.text-truncate-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  min-height: 4.5em; /* 确保文本区域高度一致 */
}
.card-hover {
  transition: transform 0.2s, box-shadow 0.2s;
  display: flex;
  flex-direction: column;
}
.card-hover:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 12px rgba(0,0,0,0.15) !important;
}
.card-footer {
  margin-top: auto; /* 确保footer始终在底部 */
}

/* 隐藏开发服务器错误提示覆盖层 */
:global(#webpack-dev-server-client-overlay) {
  display: none !important;
}
</style>
