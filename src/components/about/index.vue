<template>
  <v-container>
    <v-row class="mb-4">
      <!-- 页面标题 -->
      <v-col cols="12" class="mb-4">
        <h1 class="text-h4 font-weight-bold">关于我</h1>
        <p class="text-subtitle-1 text-medium-emphasis">个人时间线和成长历程</p>
      </v-col>

      <v-col cols="12" md="8">
        <!-- 媒体类型选择器 -->
        <v-card class="mb-4 pa-3">
          <div class="d-flex align-center justify-space-between flex-wrap">
            <div>
              <v-btn-toggle 
                v-model="selectedMediaType" 
                color="primary"
                density="comfortable"
                mandatory
              >
                <v-btn value="all" variant="text">
                  <v-icon start>mdi-image-multiple</v-icon>
                  全部
                </v-btn>
                <v-btn value="image" variant="text">
                  <v-icon start>mdi-image</v-icon>
                  图片
                </v-btn>
                <v-btn value="gif" variant="text">
                  <v-icon start>mdi-animation</v-icon>
                  动图
                </v-btn>
                <v-btn value="video" variant="text">
                  <v-icon start>mdi-video</v-icon>
                  视频
                </v-btn>
              </v-btn-toggle>
            </div>
            
            <div class="mt-2 mt-sm-0">
              <v-btn 
                color="primary" 
                prepend-icon="mdi-image-plus" 
                size="small"
                @click="showMediaUploadDialog = true"
              >
                上传媒体文件
              </v-btn>
            </div>
          </div>
        </v-card>
        
        <!-- 媒体轮播 -->
        <v-carousel v-if="filteredImages.length > 0" hide-delimiters show-arrows="hover">
          <v-carousel-item
            v-for="(item, i) in filteredImages"
            :key="i"
          >
            <!-- 图片显示 -->
            <v-img
              v-if="item.type === 'image'"
              :src="item.src"
              :alt="`轮播图`"
              height="100%"
              class="d-flex align-center justify-center"
              contain
            >
              <!-- <div class="media-caption">{{ item.name || `图片 ${i+1}` }}</div> -->
            </v-img>
            
            <!-- GIF显示 -->
            <v-img
              v-else-if="item.type === 'gif'"
              :src="item.src"
              :alt="`动态图`"
              height="100%"
              class="d-flex align-center justify-center"
              contain
            >
              <!-- <div class="media-caption">{{ item.name || `动图 ${i+1}` }}</div> -->
            </v-img>
            
            <!-- 视频显示 -->
            <div class="video-wrapper" v-else-if="item.type === 'video'">
              <video
                :src="item.src"
                height="100%"
                class="d-flex align-center justify-center video-container"
                controls
                muted
                autoplay
                loop
              ></video>
              <!-- <div class="media-caption">{{ item.name || `视频 ${i+1}` }}</div> -->
            </div>
          </v-carousel-item>
        </v-carousel>
        
        <!-- 无匹配媒体时显示 -->
        <v-card v-else class="pa-4 d-flex align-center justify-center" height="400">
          <div class="text-center">
            <v-icon icon="mdi-image-off" size="x-large" color="grey" class="mb-4"></v-icon>
            <h3 class="text-h6 text-grey">没有{{ mediaTypeText }}可显示</h3>
            <p class="text-body-2 text-grey-darken-1">嘿嘿，可以点击"上传媒体文件"按钮添加新的{{ mediaTypeText }}</p>
            <v-btn 
              color="primary" 
              prepend-icon="mdi-image-plus" 
              variant="tonal"
              class="mt-4"
              @click="showMediaUploadDialog = true"
            >
              上传媒体文件
            </v-btn>
          </div>
        </v-card>
      </v-col>
      <v-col cols="12" md="4">
        <v-card>
          <v-card-title class="text-h6">
            <v-icon start color="primary" icon="mdi-timeline-text"></v-icon>
            选择时间线
          </v-card-title>
          <v-card-text>
            <v-select
              v-model="currentTimeline"
              :items="availableTimelines"
              item-title="name"
              item-value="id"
              label="选择时间线"
              variant="outlined"
              density="comfortable"
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
              prepend-icon="mdi-download" 
              variant="tonal"
              block
              class="mb-2"
              @click="exportCurrentTimeline"
            >
              导出当前时间线
            </v-btn>
            <v-btn 
              color="primary" 
              prepend-icon="mdi-notebook-plus" 
              variant="tonal"
              block
              class="mb-2"
              @click="openDiaryImportDialog"
            >
              导入日记数据
            </v-btn>
            <v-btn 
              color="primary" 
              prepend-icon="mdi-image-plus" 
              variant="tonal"
              block
              class="mb-2"
              @click="showMediaUploadDialog = true"
            >
              上传媒体文件
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
    
    <!-- 导入日记数据对话框 -->
    <v-dialog v-model="showDiaryImportDialog" max-width="600">
      <v-card>
        <v-card-title class="text-h5">导入日记数据</v-card-title>
        <v-card-text>
          <v-alert
            v-if="diaryImportError"
            type="error"
            variant="tonal"
            density="comfortable"
            class="mb-3"
          >
            {{ diaryImportError }}
          </v-alert>
          
          <v-alert
            v-if="diaryImportSuccess"
            type="success"
            variant="tonal"
            density="comfortable"
            class="mb-3"
          >
            {{ diaryImportSuccess }}
          </v-alert>
          
          <v-form @submit.prevent="importDiaryToTimeline">
            <v-file-input
              v-model="diaryImportFile"
              accept=".json"
              label="选择日记数据文件"
              prepend-icon="mdi-file-document"
              variant="outlined"
              class="mb-4"
              hint="请选择由日记解析脚本生成的JSON文件"
              persistent-hint
              @change="handleDiaryFileSelect"
            ></v-file-input>
            
            <v-row>
              <v-col cols="8">
                <v-text-field
                  v-model="diaryTimelineName"
                  label="时间线名称"
                  variant="outlined"
                  hint="为导入的日记时间线取个名字"
                  persistent-hint
                ></v-text-field>
              </v-col>
              
              <v-col cols="4">
                <v-select
                  v-model="diaryTimelineIcon"
                  :items="availableIcons"
                  label="选择图标"
                  variant="outlined"
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
                  </template>
                </v-select>
              </v-col>
            </v-row>
            
            <div class="text-right mt-2">
              <v-btn
                variant="text"
                color="secondary"
                prepend-icon="mdi-download"
                @click="downloadSampleDiaryData"
              >
                下载示例数据
              </v-btn>
            </div>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            variant="tonal"
            @click="importDiaryToTimeline"
            :disabled="!diaryImportResult"
            :loading="diaryImportLoading"
          >
            导入到时间线
          </v-btn>
          <v-btn
            color="grey"
            variant="text"
            @click="showDiaryImportDialog = false"
          >
            取消
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    
    <!-- 媒体上传对话框 -->
    <v-dialog v-model="showMediaUploadDialog" max-width="600">
      <v-card>
        <v-card-title class="text-h5">
          上传媒体文件
          <v-btn icon @click="showMediaUploadDialog = false" class="float-right">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-card-title>
        
        <v-card-text>
          <v-form ref="uploadForm" @submit.prevent="uploadMedia">
            <v-file-input
              v-model="mediaFile"
              accept="image/*, video/*"
              placeholder="选择图片或视频文件"
              prepend-icon="mdi-file-upload"
              label="媒体文件"
              :rules="[v => !!v || '请选择一个文件']"
              @change="previewMedia"
            ></v-file-input>
            
            <v-text-field
              v-model="mediaName"
              label="媒体名称"
              placeholder="为您的媒体文件起个名字"
              prepend-icon="mdi-tag"
              :rules="[v => !!v || '请输入媒体名称']"
            ></v-text-field>
            
            <!-- 预览区域 -->
            <div v-if="mediaPreview" class="media-preview my-4">
              <p class="text-subtitle-2 mb-2">预览:</p>
              <v-card class="pa-2" flat>
                <div class="d-flex justify-center">
                  <img v-if="mediaType === 'image' || mediaType === 'gif'" :src="mediaPreview" class="preview-image" />
                  <video v-else-if="mediaType === 'video'" :src="mediaPreview" controls class="preview-video"></video>
                </div>
              </v-card>
            </div>
          </v-form>
        </v-card-text>
        
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="grey-darken-1" variant="text" @click="showMediaUploadDialog = false">
            取消
          </v-btn>
          <v-btn 
            color="primary" 
            @click="uploadMedia"
            :disabled="!mediaFile || !mediaName"
            :loading="uploadingMedia"
          >
            上传
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  name: "About",
  data() {
    return {
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
      currentTimeline: 'personal', // 当前选中的时间线ID
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
        {
          id: 'diary',
          name: '我的日记',
          description: '从日记中提取的记录',
          icon: 'mdi-notebook-outline',
          data: []
        }
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
      ],
      // 日记解析相关
      showDiaryImportDialog: false,
      diaryImportFile: null,
      diaryImportResult: null,
      diaryTimelineName: '我的日记',
      diaryTimelineIcon: 'mdi-notebook-outline',
      diaryImportLoading: false,
      diaryImportError: '',
      diaryImportSuccess: '',
      // 媒体上传相关
      showMediaUploadDialog: false,
      mediaFile: null,
      mediaName: '',
      mediaPreview: null,
      mediaType: null,
      uploadingMedia: false,
      // 媒体类型选择
      selectedMediaType: 'all',
    };
  },
  computed: {
    // 当前时间线的数据
    currentTimelineData() {
      if (!this.currentTimeline) return [];
      return this.availableTimelines.find(t => t.id === this.currentTimeline).data;
    },
    // 判断是否可以导入
    canImport() {
      if (this.importTab === 'file' && !this.importFile) return false;
      if (this.importTab === 'text' && !this.importText.trim()) return false;
      return !!this.newTimelineName.trim();
    },
    // 选择当前时间线
    selectedTimeline() {
      // 从availableTimelines中查找时间线
      const timeline = this.availableTimelines.find(t => t.id === this.currentTimeline);
      return timeline || this.availableTimelines[0];
    },
    // 根据选择的媒体类型筛选图片
    filteredImages() {
      if (this.selectedMediaType === 'all') {
        return this.images;
      }
      return this.images.filter(item => item.type === this.selectedMediaType);
    },
    // 获取当前媒体类型的文字描述
    mediaTypeText() {
      switch(this.selectedMediaType) {
        case 'image': return '图片';
        case 'gif': return '动图';
        case 'video': return '视频';
        default: return '媒体文件';
      }
    }
  },
  created() {
    this.loadImages();
    // 初始化个人历程数据
    this.availableTimelines[0].data = this.years;
    // 设置当前选中的时间线
    this.currentTimeline = 'personal';
  },
  methods: {
    loadImages() {
      try {
        // 加载图片
        const imageContext = require.context('./', false, /\.(png|jpe?g|svg)$/);
        const images = imageContext.keys().map(file => ({
          src: imageContext(file),
          type: 'image',
          name: file.replace('./', '').replace(/\.(png|jpe?g|svg)$/, '')
        }));
        
        // 尝试加载视频和GIF (如果存在)
        let mediaFiles = [];
        try {
          const mediaContext = require.context('./', false, /\.(mp4|gif)$/);
          mediaFiles = mediaContext.keys().map(file => {
            const isGif = file.endsWith('.gif');
            return {
              src: mediaContext(file),
              type: isGif ? 'gif' : 'video',
              name: file.replace('./', '').replace(/\.(mp4|gif)$/, '')
            };
          });
        } catch (mediaError) {
          console.log('没有找到视频或GIF文件:', mediaError);
        }
        
        // 合并图片和媒体文件
        this.images = [...images, ...mediaFiles];
        
        // 如果没有找到任何媒体文件，使用默认图片
        if (this.images.length === 0) {
          this.useDefaultImages();
        }
      } catch (error) {
        console.error('加载媒体文件失败:', error);
        this.useDefaultImages();
      }
    },
    
    useDefaultImages() {
      this.images = [
        {
          src: 'https://cdn.pixabay.com/photo/2016/11/19/14/00/code-1839406_1280.jpg',
          name: '编程示例',
          type: 'image',
          date: '2023-01-01'
        },
        {
          src: 'https://cdn.pixabay.com/photo/2018/09/27/09/22/artificial-intelligence-3706562_1280.jpg',
          name: '人工智能',
          type: 'image',
          date: '2023-02-01'
        },
        {
          src: 'https://cdn.pixabay.com/animation/2022/11/10/09/20/09-20-06-161_512.gif',
          name: '电子技术',
          type: 'gif',
          date: '2023-03-01'
        },
        {
          src: 'https://cdn.pixabay.com/animation/2023/02/12/05/47/05-47-36-198_512.gif',
          name: '图表动画',
          type: 'gif',
          date: '2023-04-01'
        }
      ];
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
        this.currentTimeline = newTimeline.id;
        
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
      const timeline = this.availableTimelines.find(t => t.id === this.currentTimeline);
      timeline.data.push(eventToAdd);
      
      // 按日期排序
      timeline.data.sort((a, b) => {
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
    },
    // 添加导出当前时间线方法
    exportCurrentTimeline() {
      if (!this.selectedTimeline || !this.currentTimelineData.length) {
        alert('当前时间线没有数据可供导出');
        return;
      }
      
      // 创建导出数据
      const exportData = [...this.currentTimelineData];
      
      // 转换为JSON字符串
      const dataStr = JSON.stringify(exportData, null, 2);
      const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);
      
      // 设置文件名
      const exportFileDefaultName = `${this.selectedTimeline.name}_时间线数据.json`;
      
      // 创建下载链接并触发下载
      const linkElement = document.createElement('a');
      linkElement.setAttribute('href', dataUri);
      linkElement.setAttribute('download', exportFileDefaultName);
      linkElement.click();
    },
    // 导入日记数据
    openDiaryImportDialog() {
      this.showDiaryImportDialog = true;
      this.diaryImportFile = null;
      this.diaryImportResult = null;
      this.diaryImportError = '';
      this.diaryImportSuccess = '';
      this.diaryTimelineName = '我的日记';
      this.diaryTimelineIcon = 'mdi-notebook-outline';
    },
    
    handleDiaryFileSelect(e) {
      const file = e.target.files[0];
      if (!file) return;
      
      if (file.name.endsWith('.json')) {
        const reader = new FileReader();
        reader.onload = (event) => {
          try {
            const jsonData = JSON.parse(event.target.result);
            if (Array.isArray(jsonData)) {
              this.diaryImportResult = jsonData;
              this.diaryImportError = '';
              this.diaryImportSuccess = `成功解析 ${jsonData.length} 条日记记录，可以导入到时间线`;
            } else {
              this.diaryImportError = '日记数据格式错误，应为事件数组';
              this.diaryImportSuccess = '';
            }
          } catch (error) {
            this.diaryImportError = '解析日记数据失败: ' + error.message;
            this.diaryImportSuccess = '';
          }
        };
        reader.readAsText(file);
      } else {
        this.diaryImportError = '仅支持JSON格式的日记数据文件';
        this.diaryImportSuccess = '';
      }
    },
    
    importDiaryToTimeline() {
      if (!this.diaryImportResult || !Array.isArray(this.diaryImportResult)) {
        this.diaryImportError = '没有有效的日记数据可导入';
        return;
      }
      
      // 查找或创建日记时间线
      let diaryTimeline = this.availableTimelines.find(t => t.id === 'diary');
      
      if (!diaryTimeline) {
        diaryTimeline = {
          id: 'diary',
          name: this.diaryTimelineName,
          description: '从日记中提取的记录',
          icon: this.diaryTimelineIcon,
          data: []
        };
        this.availableTimelines.push(diaryTimeline);
      } else {
        // 更新现有时间线
        diaryTimeline.name = this.diaryTimelineName;
        diaryTimeline.icon = this.diaryTimelineIcon;
      }
      
      // 转换日记数据为时间线事件
      const timelineEvents = this.diaryImportResult.map(entry => {
        // 处理日期格式 (YYYY.MM.DD -> YYYY.MM.DD)
        const date = entry.date || '未知';
        
        return {
          date: date,
          title: entry.title || `日记: ${date}`,
          content: entry.content || '',
          color: entry.color || 'blue',
          tags: entry.tags || []
        };
      });
      
      // 更新时间线事件
      diaryTimeline.data = timelineEvents;
      
      // 选择日记时间线
      this.currentTimeline = diaryTimeline.id;
      
      // 关闭对话框
      this.diaryImportSuccess = `成功导入 ${timelineEvents.length} 个日记事件到时间线`;
      setTimeout(() => {
        this.showDiaryImportDialog = false;
      }, 1500);
    },
    
    // 下载示例日记数据
    downloadSampleDiaryData() {
      const sampleData = [
        {
          "date": "2023.10.15",
          "title": "日记: 2023.10.15",
          "content": "完成了Python项目重构。阅读了《原子习惯》，思考了如何通过微习惯堆叠来实现大目标。发现自己经常陷入\"忙碌但不高效\"的状态，决定尝试番茄工作法。",
          "color": "blue",
          "tags": ["编程", "阅读", "时间管理"]
        },
        {
          "date": "2023.10.16",
          "title": "日记: 2023.10.16",
          "content": "尝试了番茄工作法，效果不错。完成了新功能开发，解决了几个棘手的bug。晚上参加了技术分享会，学习了新的设计模式。",
          "color": "green",
          "tags": ["工作", "学习", "技术"]
        }
      ];
      
      const dataStr = JSON.stringify(sampleData, null, 2);
      const dataUri = `data:application/json;charset=utf-8,${encodeURIComponent(dataStr)}`;
      
      const linkElement = document.createElement('a');
      linkElement.setAttribute('href', dataUri);
      linkElement.setAttribute('download', 'diary_sample.json');
      linkElement.click();
    },
    // 判断是否为视频或GIF
    isVideoOrGif(src) {
      const videoExtensions = ['.mp4', '.avi', '.mov', '.wmv', '.mkv'];
      const gifExtensions = ['.gif'];
      const ext = src.substring(src.lastIndexOf('.')).toLowerCase();
      return videoExtensions.includes(ext) || gifExtensions.includes(ext);
    },
    // 判断是否为GIF
    isGif(src) {
      const ext = src.substring(src.lastIndexOf('.')).toLowerCase();
      return ext === '.gif';
    },
    // 预览选择的媒体文件
    previewMedia(file) {
      if (!file) {
        this.mediaPreview = null;
        this.mediaType = null;
        return;
      }
      
      // 确定媒体类型
      if (file.type.startsWith('image/gif')) {
        this.mediaType = 'gif';
      } else if (file.type.startsWith('image/')) {
        this.mediaType = 'image';
      } else if (file.type.startsWith('video/')) {
        this.mediaType = 'video';
      } else {
        this.mediaType = null;
      }
      
      // 创建预览URL
      this.mediaPreview = URL.createObjectURL(file);
    },
    // 上传媒体文件
    async uploadMedia() {
      if (!this.mediaFile || !this.mediaName) return;
      
      this.uploadingMedia = true;
      
      try {
        // 在实际应用中，这里应该是将文件上传到服务器的代码
        // 由于这是前端模拟，我们直接使用本地URL
        
        const newMedia = {
          src: this.mediaPreview,
          name: this.mediaName,
          type: this.mediaType,
          date: new Date().toISOString()
        };
        
        // 添加到图片列表
        this.images.push(newMedia);
        
        // 关闭对话框并重置
        this.showMediaUploadDialog = false;
        this.mediaFile = null;
        this.mediaName = '';
        this.mediaPreview = null;
        
        // 显示成功消息
        this.showSuccessToast('媒体文件上传成功');
      } catch (error) {
        console.error('上传失败:', error);
        this.showErrorToast('媒体文件上传失败');
      } finally {
        this.uploadingMedia = false;
      }
    },
    // 上传成功消息
    showSuccessToast(message) {
      if (this.$toast) {
        this.$toast.success(message);
      } else {
        alert(message);
      }
    },
    // 错误消息
    showErrorToast(message) {
      if (this.$toast) {
        this.$toast.error(message);
      } else {
        alert(message);
      }
    },
  }
};
</script>

<style scoped>
/* 轮播图相关样式 */
.v-carousel {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.v-carousel-item .v-img {
  object-fit: contain;
  width: 100%;
  background-color: #f5f5f5;
}

.v-img__img--contain {
  object-position: center;
}

/* 视频容器样式 */
.video-container {
  width: 100%;
  height: 400px;
  object-fit: contain;
  background-color: #000;
  display: block;
  margin: 0 auto;
}

/* 响应式调整 */
@media (max-width: 960px) {
  .v-carousel, .video-container {
    height: 300px !important;
  }
  
  .v-carousel-item .v-img {
    height: 300px !important;
  }
}

@media (max-width: 600px) {
  .v-carousel, .video-container {
    height: 250px !important;
  }
  
  .v-carousel-item .v-img {
    height: 250px !important;
  }
}

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

.timeline-controls {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 16px;
}

.timeline-select {
  max-width: 250px;
}

.timeline-actions {
  display: flex;
  gap: 8px;
}

/* 垂直时间线样式 */
.timeline-container {
  margin-top: 20px;
  position: relative;
}

.timeline-item {
  position: relative;
  padding-left: 30px;
  margin-bottom: 24px;
}

.timeline-dot {
  position: absolute;
  left: 0;
  top: 6px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
}

.timeline-date {
  font-weight: bold;
  margin-bottom: 4px;
}

.timeline-card {
  border-radius: 8px;
}

/* 水平时间线样式 */
.horizontal-timeline {
  position: relative;
  padding-top: 40px;
  margin-bottom: 30px;
  overflow-x: auto;
}

.timeline-line {
  position: absolute;
  top: 20px;
  left: 0;
  right: 0;
  height: 4px;
  background-color: #e0e0e0;
}

.timeline-items {
  display: flex;
  flex-wrap: nowrap;
  padding-bottom: 20px;
}

.horizontal-item {
  flex: 0 0 300px;
  position: relative;
  margin-right: 30px;
}

.horizontal-item .timeline-dot {
  top: -30px;
  left: 10px;
}

.horizontal-item .timeline-year {
  margin-bottom: 10px;
  font-weight: bold;
}

.media-preview {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 16px;
  background-color: #f9f9f9;
}

.preview-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 200px;
  overflow: hidden;
}

.preview-image, .preview-video {
  max-width: 100%;
  max-height: 300px;
  object-fit: contain;
}

.media-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  padding: 8px 16px;
  text-align: center;
  font-size: 14px;
  backdrop-filter: blur(4px);
}

.video-wrapper {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #000;
}

@media (max-width: 960px) {
  .video-wrapper {
    height: 300px !important;
  }
}

@media (max-width: 600px) {
  .video-wrapper {
    height: 250px !important;
  }
}
</style>
