<template>
  <v-container>
    <v-card class="mb-4">
      <v-card-title class="d-flex align-center">
        <v-icon start icon="mdi-map-marker" class="mr-2"></v-icon>
        <h1>附近地点</h1>
      </v-card-title>
      <v-card-text>
        <!-- 地图区域 -->
        <div class="map-container mb-4">
          <div v-if="!mapLoaded" class="d-flex justify-center align-center flex-column" style="height: 300px;">
            <v-progress-circular indeterminate color="primary" size="64"></v-progress-circular>
            <div class="mt-4">地图加载中...</div>
          </div>
          <div v-else class="mock-map" style="height: 300px; background-color: #f5f5f5; border-radius: 8px; position: relative; background-image: url('https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg'); background-size: cover; background-position: center;">
            <div class="text-center position-absolute" style="top: 50%; left: 50%; transform: translate(-50%, -50%); background: rgba(255,255,255,0.8); padding: 16px; border-radius: 8px;">
              <v-icon size="64" color="primary">mdi-map</v-icon>
              <div class="mt-2">地图将在此处显示</div>
            </div>
            <div class="position-absolute" style="bottom: 16px; right: 16px;">
              <v-btn icon variant="tonal" color="primary">
                <v-icon>mdi-crosshairs-gps</v-icon>
              </v-btn>
            </div>
          </div>
        </div>
      </v-card-text>
    </v-card>

    <!-- 搜索区域 -->
    <v-card class="mb-4">
      <v-card-text>
        <v-row align="center">
          <v-col cols="12" sm="8">
            <v-text-field
              v-model="searchQuery"
              label="搜索附近地点"
              variant="outlined"
              density="comfortable"
              prepend-inner-icon="mdi-magnify"
              clearable
              @keyup.enter="searchPlaces"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="4">
            <v-select
              v-model="selectedCategory"
              :items="categories"
              label="分类"
              variant="outlined"
              density="comfortable"
              prepend-inner-icon="mdi-filter-variant"
            ></v-select>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <!-- 地点列表 -->
    <v-card>
      <v-card-title class="d-flex align-center">
        <v-icon start icon="mdi-format-list-bulleted" class="mr-2"></v-icon>
        附近地点列表
      </v-card-title>
      <v-card-text v-if="loading">
        <div class="d-flex justify-center my-4">
          <v-progress-circular indeterminate color="primary"></v-progress-circular>
        </div>
      </v-card-text>
      <template v-else>
        <v-list lines="two">
          <v-list-item
            v-for="(place, index) in nearbyPlaces"
            :key="index"
            :title="place.name"
            :subtitle="`${place.distance} · ${place.category}`"
          >
            <template v-slot:prepend>
              <v-avatar color="primary" :icon="getCategoryIcon(place.category)"></v-avatar>
            </template>
            <template v-slot:append>
              <v-btn
                icon="mdi-directions"
                variant="text"
                color="primary"
                @click="getDirections(place)"
              ></v-btn>
            </template>
          </v-list-item>
        </v-list>

        <div class="d-flex justify-center pa-4">
          <v-pagination
            v-model="page"
            :length="3"
            rounded="circle"
            width="auto"
            class="pagination-container"
            @update:model-value="handlePageChange"
          ></v-pagination>
        </div>
      </template>
    </v-card>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      mapLoaded: false,
      searchQuery: '',
      selectedCategory: '全部',
      categories: ['全部', '餐厅', '咖啡店', '超市', '公园', '学校', '图书馆'],
      loading: false,
      page: 1,
      nearbyPlaces: [
        {
          name: '北航食堂',
          distance: '200米',
          category: '餐厅'
        },
        {
          name: '星巴克咖啡',
          distance: '350米',
          category: '咖啡店'
        },
        {
          name: '学生活动中心',
          distance: '500米',
          category: '学校'
        },
        {
          name: '知春路地铁站',
          distance: '800米',
          category: '交通'
        },
        {
          name: '北航图书馆',
          distance: '400米',
          category: '图书馆'
        },
        {
          name: '五道口购物中心',
          distance: '1.2公里',
          category: '购物'
        }
      ]
    };
  },
  mounted() {
    // 模拟地图加载
    setTimeout(() => {
      this.mapLoaded = true;
    }, 1500);
  },
  methods: {
    searchPlaces() {
      this.loading = true;
      // 模拟搜索延迟
      setTimeout(() => {
        this.loading = false;
        // 这里可以添加实际的搜索逻辑
      }, 1000);
    },
    getCategoryIcon(category) {
      const iconMap = {
        '餐厅': 'mdi-food',
        '咖啡店': 'mdi-coffee',
        '超市': 'mdi-store',
        '公园': 'mdi-nature',
        '学校': 'mdi-school',
        '图书馆': 'mdi-library',
        '交通': 'mdi-train',
        '购物': 'mdi-shopping'
      };
      return iconMap[category] || 'mdi-map-marker';
    },
    getDirections(place) {
      // 获取导航信息的方法
      console.log(`获取到 ${place.name} 的导航信息`);
      // 实际项目中可以跳转到导航页面或打开地图应用
    },
    handlePageChange(newPage) {
      console.log(`切换到第 ${newPage} 页的附近地点`);
      this.page = newPage;
      
      // 使用 requestAnimationFrame 避免循环错误
      window.requestAnimationFrame(() => {
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      });
    }
  }
};
</script>

<style scoped>
.map-container {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
}
.position-absolute {
  position: absolute;
}
.pagination-container {
  max-width: 100%;
  overflow-x: auto;
  margin: 0 auto;
  width: max-content;
}
</style>
