<template>
  <v-container>
    <v-row class="mb-4">
      <v-col cols="12" md="8">
        <v-carousel hide-delimiters>
          <v-carousel-item
            v-for="(item, i) in images"
            :key="i"
            :src="item.src"
            cover
          ></v-carousel-item>
        </v-carousel>
      </v-col>
      <v-col cols="12" md="4">
        <v-card>
          <v-card-title class="text-h6">
            <v-icon start color="primary" icon="mdi-timeline-text"></v-icon>
            选择时间线
          </v-card-title>
          <v-card-text>
            <v-select
              v-model="selectedTimeline"
              :items="availableTimelines"
              item-title="name"
              item-value="id"
              label="选择时间线"
              variant="outlined"
              density="comfortable"
              return-object
            ></v-select>
            
            <v-divider class="my-4"></v-divider>
            
            <v-btn 
              color="primary" 
              prepend-icon="mdi-upload" 
              variant="tonal"
              block
              class="mb-2"
              @click="showImportDialog = true"
            >
              导入时间线数据
            </v-btn>
            
            <v-btn 
              color="secondary" 
              prepend-icon="mdi-plus" 
              variant="tonal"
              block
              @click="showAddEntryDialog = true"
            >
              添加新事件
            </v-btn>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    
    <v-card class="mb-4">
      <v-card-title class="d-flex align-center">
        <v-icon start color="primary" class="mr-2">{{ selectedTimeline.icon }}</v-icon>
        <h2>{{ selectedTimeline.name }}</h2>
        <v-spacer></v-spacer>
        <v-btn-toggle
          v-model="timelineView"
          color="primary"
          density="comfortable"
          rounded="pill"
        >
          <v-btn value="vertical" icon="mdi-format-list-bulleted"></v-btn>
          <v-btn value="horizontal" icon="mdi-timeline-outline"></v-btn>
        </v-btn-toggle>
      </v-card-title>
      <v-card-subtitle>{{ selectedTimeline.description }}</v-card-subtitle>
    </v-card>
    
    <!-- 垂直时间线视图 -->
    <v-timeline 
      v-if="timelineView === 'vertical'"
      align="start" 
      justify="center"
      line-thickness="2"
      line-color="primary"
    >
      <v-timeline-item
        v-for="(event, i) in currentTimelineData"
        :key="i"
        :dot-color="event.color || 'primary'"
        size="small"
        fill-dot
      >
        <template v-slot:opposite>
          <div
            :class="`pt-1 headline font-weight-bold text-${event.color || 'primary'}`"
            v-text="event.year || event.date"
          ></div>
        </template>
        <div>
          <h2
            :class="`mt-n1 headline font-weight-light mb-2 text-${event.color || 'primary'}`"
          >
            {{ event.title }}
          </h2>
          <div class="text-body-1">
            {{ event.content }}
          </div>
          <v-chip-group v-if="event.tags && event.tags.length > 0" class="mt-2">
            <v-chip
              v-for="(tag, tagIndex) in event.tags"
              :key="tagIndex"
              size="small"
              color="grey-lighten-3"
            >
              {{ tag }}
            </v-chip>
          </v-chip-group>
        </div>
      </v-timeline-item>
    </v-timeline>
    
    <!-- 横向时间线视图 -->
    <div v-else-if="timelineView === 'horizontal'" class="horizontal-timeline">
      <div class="timeline-scroll-container">
        <div class="timeline-track">
          <div 
            v-for="(event, i) in currentTimelineData" 
            :key="i"
            class="timeline-event"
            :class="{'active': selectedEvent === i}"
            @click="selectedEvent = i"
          >
            <div class="timeline-date">{{ event.year || event.date }}</div>
            <div 
              class="timeline-dot" 
              :style="{backgroundColor: getColor(event.color || 'primary')}"
            ></div>
            <div class="timeline-title">{{ event.title }}</div>
          </div>
        </div>
      </div>
      
      <v-card v-if="selectedEvent !== null" class="mt-4">
        <v-card-title :class="`text-${currentTimelineData[selectedEvent].color || 'primary'}`">
          {{ currentTimelineData[selectedEvent].title }}
        </v-card-title>
        <v-card-subtitle>{{ currentTimelineData[selectedEvent].year || currentTimelineData[selectedEvent].date }}</v-card-subtitle>
        <v-card-text>{{ currentTimelineData[selectedEvent].content }}</v-card-text>
        <v-card-actions v-if="currentTimelineData[selectedEvent].tags && currentTimelineData[selectedEvent].tags.length > 0">
          <v-chip
            v-for="(tag, tagIndex) in currentTimelineData[selectedEvent].tags"
            :key="tagIndex"
            size="small"
            color="grey-lighten-3"
            class="mr-2"
          >
            {{ tag }}
          </v-chip>
        </v-card-actions>
      </v-card>
    </div>
    
    <!-- 导入时间线对话框 -->
    <v-dialog v-model="showImportDialog" max-width="600">
      <v-card>
        <v-card-title class="text-h5">导入时间线数据</v-card-title>
        <v-card-text>
          <v-tabs v-model="importTab">
            <v-tab value="file">文件导入</v-tab>
            <v-tab value="text">文本导入</v-tab>
          </v-tabs>
          
          <v-window v-model="importTab">
            <v-window-item value="file">
              <v-file-input
                v-model="importFile"
                accept=".json, .txt"
                label="选择JSON文件"
                prepend-icon="mdi-file-document"
                variant="outlined"
                class="mt-4"
                show-size
                @change="onFileSelected"
              ></v-file-input>
              
              <div class="text-caption text-grey">
                支持JSON格式的时间线数据文件。
                <a href="#" @click.prevent="downloadSampleFile">下载示例文件</a>
              </div>
            </v-window-item>
            
            <v-window-item value="text">
              <v-textarea
                v-model="importText"
                label="粘贴JSON数据"
                variant="outlined"
                hint="粘贴符合格式的JSON时间线数据"
                persistent-hint
                rows="10"
                class="mt-4"
              ></v-textarea>
            </v-window-item>
          </v-window>
          
          <v-text-field
            v-model="newTimelineName"
            label="时间线名称"
            variant="outlined"
            class="mt-4"
            density="comfortable"
          ></v-text-field>
          
          <v-select
            v-model="newTimelineIcon"
            :items="availableIcons"
            label="选择图标"
            variant="outlined"
            item-props
            density="comfortable"
          >
            <template v-slot:item="{ item, props }">
              <v-list-item v-bind="props">
                <template v-slot:prepend>
                  <v-icon :icon="item.raw"></v-icon>
                </template>
                <v-list-item-title>{{ item.raw }}</v-list-item-title>
              </v-list-item>
            </template>
            <template v-slot:selection="{ item }">
              <v-icon :icon="item.value" class="mr-2"></v-icon>
              {{ item.value }}
            </template>
          </v-select>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="grey" variant="text" @click="showImportDialog = false">取消</v-btn>
          <v-btn 
            color="primary" 
            variant="tonal" 
            @click="importTimelineData"
            :disabled="!canImport"
          >
            导入
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    
    <!-- 添加新事件对话框 -->
    <v-dialog v-model="showAddEntryDialog" max-width="600">
      <v-card>
        <v-card-title class="text-h5">添加新事件</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="newEvent.title"
            label="事件标题"
            variant="outlined"
            density="comfortable"
            class="mb-2"
          ></v-text-field>
          
          <v-text-field
            v-model="newEvent.date"
            label="日期/年份"
            variant="outlined"
            density="comfortable"
            class="mb-2"
          ></v-text-field>
          
          <v-textarea
            v-model="newEvent.content"
            label="事件内容"
            variant="outlined"
            density="comfortable"
            class="mb-2"
            rows="3"
          ></v-textarea>
          
          <v-select
            v-model="newEvent.color"
            :items="availableColors"
            label="选择颜色"
            variant="outlined"
            density="comfortable"
            class="mb-2"
          >
            <template v-slot:item="{ item, props }">
              <v-list-item v-bind="props">
                <template v-slot:prepend>
                  <v-avatar :color="item.raw" size="24"></v-avatar>
                </template>
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item>
            </template>
            <template v-slot:selection="{ item }">
              <v-avatar :color="item.value" size="24" class="mr-2"></v-avatar>
              {{ item.title }}
            </template>
          </v-select>
          
          <v-combobox
            v-model="newEvent.tags"
            label="标签（按回车添加）"
            variant="outlined"
            density="comfortable"
            chips
            multiple
            clearable
          ></v-combobox>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="grey" variant="text" @click="showAddEntryDialog = false">取消</v-btn>
          <v-btn 
            color="primary" 
            variant="tonal" 
            @click="addNewEvent"
            :disabled="!newEvent.title || !newEvent.date"
          >
            添加
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
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
    images: [],
    // 时间线相关数据
    timelineView: 'vertical', // 默认垂直视图
    selectedEvent: null, // 当前选中的事件（用于横向视图）
    selectedTimeline: null, // 当前选中的时间线
    availableTimelines: [
      { 
        id: 'personal', 
        name: '个人历程', 
        description: '我的个人成长轨迹',
        icon: 'mdi-account-school', 
        data: [] // 会在created中填充
      },
      { 
        id: 'tech', 
        name: '技术成长', 
        description: '我的技术学习历程',
        icon: 'mdi-code-tags', 
        data: [
          {
            title: '开始学习HTML和CSS',
            date: '2022.3',
            content: '接触前端开发的起点，开始了解网页结构和样式',
            color: 'blue',
            tags: ['HTML', 'CSS', '前端']
          },
          {
            title: '学习JavaScript',
            date: '2022.5',
            content: '开始学习JavaScript，为动态网页开发打下基础',
            color: 'yellow-darken-2',
            tags: ['JavaScript', '前端']
          },
          {
            title: '接触Vue框架',
            date: '2023.2',
            content: '开始学习Vue.js框架，感受到现代前端框架的魅力',
            color: 'green',
            tags: ['Vue', '前端框架']
          },
          {
            title: '使用Vuetify',
            date: '2023.8',
            content: '开始使用Vuetify组件库，加速UI开发效率',
            color: 'indigo',
            tags: ['Vuetify', 'UI']
          }
        ]
      },
    ],
    // 导入相关
    showImportDialog: false,
    importTab: 'file',
    importFile: null,
    importText: '',
    newTimelineName: '',
    newTimelineIcon: 'mdi-timeline-clock',
    // 添加事件相关
    showAddEntryDialog: false,
    newEvent: {
      title: '',
      date: '',
      content: '',
      color: 'primary',
      tags: []
    },
    // 颜色和图标选项
    availableColors: [
      { title: '主色调', value: 'primary' },
      { title: '蓝色', value: 'blue' },
      { title: '绿色', value: 'green' },
      { title: '红色', value: 'red' },
      { title: '橙色', value: 'orange' },
      { title: '紫色', value: 'purple' },
      { title: '青色', value: 'cyan' },
      { title: '粉色', value: 'pink' },
      { title: '琥珀色', value: 'amber' },
      { title: '茶色', value: 'brown' }
    ],
    availableIcons: [
      'mdi-timeline-clock',
      'mdi-timeline-text',
      'mdi-timeline-outline',
      'mdi-account-school',
      'mdi-code-tags',
      'mdi-heart',
      'mdi-star',
      'mdi-book-open',
      'mdi-rocket-launch',
      'mdi-map-marker',
      'mdi-briefcase',
      'mdi-lightbulb'
    ]
  }),
  computed: {
    // 当前时间线的数据
    currentTimelineData() {
      if (!this.selectedTimeline) return [];
      return this.selectedTimeline.data;
    },
    // 判断是否可以导入
    canImport() {
      if (this.importTab === 'file' && !this.importFile) return false;
      if (this.importTab === 'text' && !this.importText.trim()) return false;
      return !!this.newTimelineName.trim();
    }
  },
  created() {
    this.loadImages();
    // 初始化个人历程数据
    this.availableTimelines[0].data = this.years;
    this.selectedTimeline = this.availableTimelines[0];
  },
  methods: {
    loadImages() {
      try {
        const requireContext = require.context('./', false, /\.(png|jpe?g|svg)$/);
        this.images = requireContext.keys().map(file => ({
          src: requireContext(file)
        }));
      } catch (error) {
        console.error('加载图片失败:', error);
        // 使用一些默认图片
        this.images = [
          { src: 'https://picsum.photos/id/11/500/300' },
          { src: 'https://picsum.photos/id/12/500/300' },
          { src: 'https://picsum.photos/id/13/500/300' }
        ];
      }
    },
    // 获取颜色样式
    getColor(colorName) {
      const colorMap = {
        'primary': '#1976D2',
        'blue': '#2196F3',
        'green': '#4CAF50',
        'red': '#F44336',
        'orange': '#FF9800',
        'purple': '#9C27B0',
        'cyan': '#00BCD4',
        'pink': '#E91E63',
        'amber': '#FFC107',
        'brown': '#795548'
      };
      return colorMap[colorName] || colorMap['primary'];
    },
    // 文件选择处理
    onFileSelected(file) {
      if (!file) return;
      
      const reader = new FileReader();
      reader.onload = (e) => {
        try {
          const content = e.target.result;
          // 尝试解析JSON
          const jsonData = JSON.parse(content);
          // 预览导入的数据
          this.importText = JSON.stringify(jsonData, null, 2);
          // 如果文件名中包含时间线名称，则自动填充
          const fileName = file.name.replace(/\.(json|txt)$/, '');
          if (!this.newTimelineName && fileName) {
            this.newTimelineName = fileName;
          }
        } catch (error) {
          console.error('解析JSON失败:', error);
          alert('文件格式不正确，请上传有效的JSON数据');
        }
      };
      reader.readAsText(file);
    },
    // 下载示例文件
    downloadSampleFile() {
      const sampleData = [
        {
          title: '示例事件1',
          date: '2022.1',
          content: '这是示例事件1的详细描述内容',
          color: 'blue',
          tags: ['标签1', '标签2']
        },
        {
          title: '示例事件2',
          date: '2022.6',
          content: '这是示例事件2的详细描述内容',
          color: 'green',
          tags: ['标签3']
        },
        {
          title: '示例事件3',
          date: '2023.1',
          content: '这是示例事件3的详细描述内容',
          color: 'red',
          tags: []
        }
      ];
      
      const dataStr = JSON.stringify(sampleData, null, 2);
      const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);
      
      const exportFileDefaultName = '时间线示例数据.json';
      
      const linkElement = document.createElement('a');
      linkElement.setAttribute('href', dataUri);
      linkElement.setAttribute('download', exportFileDefaultName);
      linkElement.click();
    },
    // 导入时间线数据
    importTimelineData() {
      try {
        let timelineData;
        
        if (this.importTab === 'file' && this.importFile) {
          // 已经在onFileSelected中解析了，直接使用importText
          timelineData = JSON.parse(this.importText);
        } else if (this.importTab === 'text' && this.importText) {
          timelineData = JSON.parse(this.importText);
        } else {
          alert('请提供有效的时间线数据');
          return;
        }
        
        // 验证数据格式
        if (!Array.isArray(timelineData)) {
          alert('时间线数据必须是数组格式');
          return;
        }
        
        // 创建新的时间线
        const newTimeline = {
          id: 'timeline_' + Date.now(),
          name: this.newTimelineName,
          description: `导入的时间线：${this.newTimelineName}`,
          icon: this.newTimelineIcon || 'mdi-timeline-clock',
          data: timelineData
        };
        
        // 添加到可用时间线列表
        this.availableTimelines.push(newTimeline);
        
        // 切换到新导入的时间线
        this.selectedTimeline = newTimeline;
        
        // 关闭对话框并重置表单
        this.showImportDialog = false;
        this.importFile = null;
        this.importText = '';
        this.newTimelineName = '';
        
        // 提示成功
        alert('时间线数据导入成功！');
      } catch (error) {
        console.error('导入数据失败:', error);
        alert('导入失败，请检查数据格式是否正确');
      }
    },
    // 添加新事件
    addNewEvent() {
      if (!this.newEvent.title || !this.newEvent.date) {
        alert('请填写事件标题和日期');
        return;
      }
      
      // 复制事件对象
      const eventToAdd = { ...this.newEvent };
      
      // 添加到当前时间线
      this.selectedTimeline.data.push(eventToAdd);
      
      // 按日期排序
      this.selectedTimeline.data.sort((a, b) => {
        const dateA = a.date || a.year || '';
        const dateB = b.date || b.year || '';
        return dateA.localeCompare(dateB);
      });
      
      // 关闭对话框并重置表单
      this.showAddEntryDialog = false;
      this.newEvent = {
        title: '',
        date: '',
        content: '',
        color: 'primary',
        tags: []
      };
    }
  }
};
</script>

<style scoped>
.horizontal-timeline {
  position: relative;
  margin: 40px 0;
  padding: 20px 0;
}

.timeline-scroll-container {
  width: 100%;
  overflow-x: auto;
  margin-bottom: 20px;
}

.timeline-track {
  display: flex;
  position: relative;
  min-width: 100%;
  padding: 40px 20px 20px;
}

.timeline-track::before {
  content: '';
  position: absolute;
  top: 40px;
  left: 0;
  right: 0;
  height: 2px;
  background-color: rgba(0, 0, 0, 0.12);
  z-index: 1;
}

.timeline-event {
  position: relative;
  flex: 1;
  min-width: 120px;
  text-align: center;
  cursor: pointer;
  padding: 0 10px;
  transition: all 0.3s;
}

.timeline-event.active .timeline-dot {
  transform: scale(1.5);
  box-shadow: 0 0 0 4px rgba(25, 118, 210, 0.2);
}

.timeline-date {
  margin-bottom: 15px;
  font-size: 12px;
  font-weight: 500;
}

.timeline-dot {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background-color: #1976D2;
  margin: 0 auto;
  position: relative;
  z-index: 2;
  transition: transform 0.3s;
}

.timeline-title {
  margin-top: 15px;
  font-size: 14px;
  font-weight: 500;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* 响应式调整 */
@media (max-width: 600px) {
  .timeline-event {
    min-width: 100px;
  }
  
  .timeline-title {
    font-size: 12px;
  }
}
</style>
