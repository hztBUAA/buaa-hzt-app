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
          <div id="map-container" style="height: 300px; border-radius: 8px;"></div>
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
            v-for="(place, index) in filteredPlaces"
            :key="index"
            :title="place.name"
            :subtitle="`${place.distance || '未知距离'} · ${place.category || place.type}`"
          >
            <template v-slot:prepend>
              <v-avatar color="primary" :icon="getCategoryIcon(place.category || place.type)"></v-avatar>
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
            :length="Math.ceil(filteredPlaces.length / pageSize)"
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
      pageSize: 6,
      map: null,
      geolocation: null,
      currentPosition: null,
      nearbyPlaces: [],
      mockPlaces: [
        {
          name: '北航食堂',
          distance: '200米',
          category: '餐厅',
          location: [116.351462, 39.980476]
        },
        {
          name: '星巴克咖啡',
          distance: '350米',
          category: '咖啡店',
          location: [116.349784, 39.982310]
        },
        {
          name: '学生活动中心',
          distance: '500米',
          category: '学校',
          location: [116.353103, 39.979854]
        },
        {
          name: '知春路地铁站',
          distance: '800米',
          category: '交通',
          location: [116.347854, 39.976549]
        },
        {
          name: '北航图书馆',
          distance: '400米',
          category: '图书馆',
          location: [116.350678, 39.981236]
        },
        {
          name: '五道口购物中心',
          distance: '1.2公里',
          category: '购物',
          location: [116.338963, 39.991255]
        }
      ]
    };
  },
  computed: {
    filteredPlaces() {
      let places = this.nearbyPlaces.length > 0 ? this.nearbyPlaces : this.mockPlaces;
      
      if (this.selectedCategory !== '全部') {
        places = places.filter(place => 
          (place.category && place.category.includes(this.selectedCategory)) || 
          (place.type && place.type.includes(this.selectedCategory))
        );
      }
      
      if (this.searchQuery) {
        const query = this.searchQuery.toLowerCase();
        places = places.filter(place => 
          place.name.toLowerCase().includes(query) || 
          (place.address && place.address.toLowerCase().includes(query))
        );
      }
      
      // 分页处理
      const start = (this.page - 1) * this.pageSize;
      const end = start + this.pageSize;
      
      return places.slice(start, end);
    }
  },
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      // 如果在开发环境或者没有正确配置API，使用模拟数据
      if (!window.AMap) {
        this.loadAMapScript().then(() => {
          this.createMap();
        }).catch(err => {
          console.error('加载地图API失败:', err);
          this.mapLoaded = true; // 即使失败也标记为已加载，避免一直显示加载中
        });
      } else {
        this.createMap();
      }
    },
    
    loadAMapScript() {
      return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.type = 'text/javascript';
        script.async = true;
        script.src = 'https://webapi.amap.com/maps?v=2.0&key=您的高德地图key';
        script.onerror = reject;
        script.onload = resolve;
        document.head.appendChild(script);
      });
    },
    
    createMap() {
      try {
        // 创建地图实例
        this.map = new AMap.Map('map-container', {
          zoom: 15,
          viewMode: '3D'
        });
        
        // 添加控件
        this.map.plugin(['AMap.ToolBar', 'AMap.Scale'], () => {
          this.map.addControl(new AMap.ToolBar());
          this.map.addControl(new AMap.Scale());
        });
        
        // 添加定位控件
        this.map.plugin('AMap.Geolocation', () => {
          this.geolocation = new AMap.Geolocation({
            enableHighAccuracy: true,
            timeout: 10000,
            zoomToAccuracy: true
          });
          this.map.addControl(this.geolocation);
          
          // 获取当前位置
          this.getCurrentPosition();
        });
        
        this.mapLoaded = true;
      } catch (error) {
        console.error('创建地图失败:', error);
        // 使用模拟数据
        this.mapLoaded = true;
      }
    },
    
    getCurrentPosition() {
      if (this.geolocation) {
        this.geolocation.getCurrentPosition((status, result) => {
          if (status === 'complete') {
            this.currentPosition = result.position;
            // 在地图上标记当前位置
            const marker = new AMap.Marker({
              position: this.currentPosition,
              icon: 'https://webapi.amap.com/theme/v1.3/markers/n/mark_b.png',
              animation: 'AMAP_ANIMATION_BOUNCE'
            });
            this.map.add(marker);
            
            // 初始设置地图中心点
            this.map.setCenter(this.currentPosition);
            
            // 获取周边兴趣点
            this.searchNearbyPOI();
          } else {
            console.error('定位失败:', result);
            // 失败时使用默认位置(北航坐标)
            this.currentPosition = [116.351013, 39.980331];
            this.map.setCenter(this.currentPosition);
          }
        });
      }
    },
    
    searchNearbyPOI() {
      if (!this.currentPosition) return;
      
      this.loading = true;
      
      try {
        // 使用高德地图POI搜索服务
        AMap.service('AMap.PlaceSearch', () => {
          const placeSearch = new AMap.PlaceSearch({
            pageSize: 20,
            pageIndex: 1,
            extensions: 'all'
          });
          
          // 搜索周边兴趣点
          placeSearch.searchNearBy('', this.currentPosition, 1000, (status, result) => {
            this.loading = false;
            
            if (status === 'complete') {
              this.nearbyPlaces = result.poiList.pois.map(poi => {
                // 计算与当前位置的距离
                const distance = AMap.GeometryUtil.distance(
                  this.currentPosition,
                  [poi.location.lng, poi.location.lat]
                );
                
                let distanceText = '';
                if (distance < 1000) {
                  distanceText = `${Math.round(distance)}米`;
                } else {
                  distanceText = `${(distance / 1000).toFixed(1)}公里`;
                }
                
                return {
                  id: poi.id,
                  name: poi.name,
                  type: poi.type,
                  address: poi.address,
                  distance: distanceText,
                  location: [poi.location.lng, poi.location.lat]
                };
              });
              
              // 在地图上添加标记
              this.addMarkersToMap(this.nearbyPlaces);
            } else {
              console.error('搜索附近地点失败:', result);
              // 使用模拟数据
              this.nearbyPlaces = this.mockPlaces;
              this.addMarkersToMap(this.mockPlaces);
            }
          });
        });
      } catch (error) {
        console.error('搜索附近POI失败:', error);
        this.loading = false;
        // 使用模拟数据
        this.nearbyPlaces = this.mockPlaces;
        this.addMarkersToMap(this.mockPlaces);
      }
    },
    
    addMarkersToMap(places) {
      if (!this.map) return;
      
      // 添加标记之前先清除地图上已有的标记
      this.map.clearMap();
      
      // 重新添加当前位置标记
      if (this.currentPosition) {
        const currentMarker = new AMap.Marker({
          position: this.currentPosition,
          icon: 'https://webapi.amap.com/theme/v1.3/markers/n/mark_b.png',
          animation: 'AMAP_ANIMATION_BOUNCE'
        });
        this.map.add(currentMarker);
      }
      
      // 添加兴趣点标记
      places.forEach(place => {
        if (place.location) {
          const marker = new AMap.Marker({
            position: place.location,
            title: place.name
          });
          
          marker.on('click', () => {
            // 显示信息窗体
            const infoWindow = new AMap.InfoWindow({
              content: `
                <div class="info-window">
                  <h3>${place.name}</h3>
                  <p>${place.address || ''}</p>
                  <p>距离: ${place.distance}</p>
                </div>
              `,
              offset: new AMap.Pixel(0, -30)
            });
            
            infoWindow.open(this.map, place.location);
          });
          
          this.map.add(marker);
        }
      });
    },
    
    searchPlaces() {
      this.loading = true;
      
      if (this.map && this.currentPosition) {
        try {
          AMap.service('AMap.PlaceSearch', () => {
            const placeSearch = new AMap.PlaceSearch({
              pageSize: 20,
              pageIndex: 1,
              extensions: 'all'
            });
            
            // 搜索周边兴趣点
            placeSearch.searchNearBy(this.searchQuery, this.currentPosition, 5000, (status, result) => {
              this.loading = false;
              
              if (status === 'complete') {
                this.nearbyPlaces = result.poiList.pois.map(poi => {
                  const distance = AMap.GeometryUtil.distance(
                    this.currentPosition,
                    [poi.location.lng, poi.location.lat]
                  );
                  
                  let distanceText = '';
                  if (distance < 1000) {
                    distanceText = `${Math.round(distance)}米`;
                  } else {
                    distanceText = `${(distance / 1000).toFixed(1)}公里`;
                  }
                  
                  return {
                    id: poi.id,
                    name: poi.name,
                    type: poi.type,
                    address: poi.address,
                    distance: distanceText,
                    location: [poi.location.lng, poi.location.lat]
                  };
                });
                
                // 在地图上添加标记
                this.addMarkersToMap(this.nearbyPlaces);
                this.page = 1; // 重置到第一页
              } else {
                console.error('搜索地点失败:', result);
              }
            });
          });
        } catch (error) {
          console.error('搜索地点失败:', error);
          this.loading = false;
        }
      } else {
        // 模拟搜索延迟
        setTimeout(() => {
          this.loading = false;
          // 使用模拟数据进行过滤
          if (this.searchQuery) {
            const query = this.searchQuery.toLowerCase();
            this.nearbyPlaces = this.mockPlaces.filter(place => 
              place.name.toLowerCase().includes(query)
            );
          } else {
            this.nearbyPlaces = this.mockPlaces;
          }
          this.page = 1; // 重置到第一页
        }, 1000);
      }
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
        '购物': 'mdi-shopping',
        '美食': 'mdi-food-fork-drink',
        '酒店': 'mdi-bed',
        '银行': 'mdi-bank',
        '医院': 'mdi-hospital-building'
      };
      
      // 检查类别是否包含特定关键词
      if (category) {
        const lowerCaseCategory = category.toLowerCase();
        
        if (lowerCaseCategory.includes('餐')) return 'mdi-food';
        if (lowerCaseCategory.includes('咖啡')) return 'mdi-coffee';
        if (lowerCaseCategory.includes('超市') || lowerCaseCategory.includes('商场')) return 'mdi-store';
        if (lowerCaseCategory.includes('公园')) return 'mdi-nature';
        if (lowerCaseCategory.includes('学校') || lowerCaseCategory.includes('教育')) return 'mdi-school';
        if (lowerCaseCategory.includes('图书馆')) return 'mdi-library';
        if (lowerCaseCategory.includes('地铁') || lowerCaseCategory.includes('交通') || lowerCaseCategory.includes('公交')) return 'mdi-train';
        if (lowerCaseCategory.includes('购物') || lowerCaseCategory.includes('商店')) return 'mdi-shopping';
        if (lowerCaseCategory.includes('酒店') || lowerCaseCategory.includes('宾馆')) return 'mdi-bed';
        if (lowerCaseCategory.includes('银行') || lowerCaseCategory.includes('金融')) return 'mdi-bank';
        if (lowerCaseCategory.includes('医院') || lowerCaseCategory.includes('诊所')) return 'mdi-hospital-building';
      }
      
      return iconMap[category] || 'mdi-map-marker';
    },
    
    getDirections(place) {
      if (this.currentPosition && place.location) {
        // 使用高德地图导航
        const url = `https://uri.amap.com/navigation?from=${this.currentPosition.join(',')},我的位置&to=${place.location.join(',')},${place.name}&mode=car&policy=1&src=mypage&callnative=1`;
        window.open(url, '_blank');
      } else {
        console.log(`获取到 ${place.name} 的导航信息`);
        alert(`导航到: ${place.name}\n地址: ${place.address || '未知地址'}`);
      }
    },
    
    handlePageChange(newPage) {
      if (this.page === newPage) return; // 防止相同页码重复触发
      this.page = newPage;
      // 使用 setTimeout 确保状态更新后再滚动
      setTimeout(() => {
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      }, 10);
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
.info-window h3 {
  margin: 0 0 5px 0;
  font-size: 16px;
}
.info-window p {
  margin: 0 0 5px 0;
  font-size: 13px;
}
</style>
