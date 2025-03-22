<template>
  <v-layout>
    <!-- 个人资料卡片 -->
    <v-container>
      <v-row>
        <!-- 顶部背景卡片 -->
        <v-col cols="12">
          <v-card class="profile-card">
            <!-- 背景封面 -->
            <v-img
              height="200"
              :src="userProfile.coverImage"
              cover
            >
              <template v-slot:placeholder>
                <v-row
                  class="fill-height ma-0"
                  align="center"
                  justify="center"
                >
                  <v-progress-circular
                    indeterminate
                    color="grey-lighten-5"
                  ></v-progress-circular>
                </v-row>
              </template>
            </v-img>

            <!-- 个人信息区域 -->
            <v-card-text class="profile-info">
              <!-- 头像 -->
              <v-avatar
                size="120"
                class="profile-avatar"
              >
                <v-img
                  :src="userProfile.avatar"
                  alt="黄振庭"
                ></v-img>
              </v-avatar>

              <!-- 基本信息 -->
              <div class="profile-details mt-4">
                <h2 class="text-h4 font-weight-bold">{{ userProfile.name }}</h2>
                <p class="text-subtitle-1 text-medium-emphasis">{{ userProfile.title }}</p>
                <p class="text-body-1 mt-2">{{ userProfile.bio }}</p>
                
                <!-- 联系方式和社交媒体 -->
                <v-row class="mt-4">
                  <v-col v-for="(link, index) in socialLinks" 
                         :key="index" 
                         cols="12" sm="6" md="4">
                    <v-btn
                      :prepend-icon="link.icon"
                      :href="link.url"
                      target="_blank"
                      variant="tonal"
                      block
                    >
                      {{ link.text }}
                    </v-btn>
                  </v-col>
                </v-row>
              </div>
            </v-card-text>
          </v-card>
        </v-col>

        <!-- 数据统计卡片 -->
        <v-col cols="12" md="4">
          <v-card>
            <v-card-title class="d-flex align-center">
              <v-icon start icon="mdi-chart-line" class="mr-2"></v-icon>
              数据统计
            </v-card-title>
            <v-card-text>
              <v-row>
                <v-col v-for="(stat, key) in statistics" 
                       :key="key" 
                       cols="6">
                  <div class="text-center">
                    <div class="text-h4">{{ stat.value }}</div>
                    <div class="text-caption">{{ stat.label }}</div>
                  </div>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>

        <!-- 技能展示卡片 -->
        <v-col cols="12" md="8">
          <v-card>
            <v-card-title class="d-flex align-center">
              <v-icon start icon="mdi-lightbulb" class="mr-2"></v-icon>
              技能专长
            </v-card-title>
            <v-card-text>
              <v-chip-group>
                <v-chip
                  v-for="skill in skills"
                  :key="skill.name"
                  :color="skill.color"
                  variant="elevated"
                >
                  {{ skill.name }}
                </v-chip>
              </v-chip-group>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-layout>
</template>

<script>
import { ref } from 'vue'

export default {
  setup() {
    // 用户基本信息
    const userProfile = ref({
      name: '黄振庭',
      title: '全栈开发工程师',
      bio: '热爱编程，专注于Web开发和人工智能领域',
      avatar: 'https://avatars.githubusercontent.com/u/your-username',
      coverImage: 'https://cdn.vuetifyjs.com/images/cards/dark-beach.jpg'
    })

    // 社交媒体链接
    const socialLinks = ref([
      {
        icon: 'mdi-github',
        text: 'GitHub',
        url: 'https://github.com/hztBUAA'
      },
      {
        icon: 'mdi-email',
        text: '发送邮件',
        url: 'mailto:zhentinghng@buaa.edu.cn'
      },
      {
        icon: 'mdi-web',
        text: '个人网站(正是本站)',
        url: 'https://hztbuaa.github.io/buaa-hzt-app'
      }
    ])

    // 统计数据
    const statistics = ref({
      projects: { value: 12, label: '项目数' },
      contributions: { value: 328, label: '贡献数' },
      followers: { value: 56, label: '关注者' },
      following: { value: 23, label: '关注中' }
    })

    // 技能列表
    const skills = ref([
      { name: 'Vue.js', color: 'success' },
      { name: 'JavaScript', color: 'warning' },
      { name: 'Node.js', color: 'green' },
      { name: 'Python', color: 'blue' },
      { name: '后端开发', color: 'indigo' },
      { name: '前端开发', color: 'deep-purple' },
      { name: '数据库', color: 'orange' },
      { name: 'DevOps', color: 'red' }
    ])

    return {
      userProfile,
      socialLinks,
      statistics,
      skills
    }
  }
}
</script>

<style scoped>
.profile-card {
  position: relative;
  overflow: visible;
}

.profile-info {
  position: relative;
  margin-top: -60px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 16px;
}

.profile-avatar {
  position: absolute;
  top: -60px;
  left: 24px;
  border: 4px solid white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.profile-details {
  padding-top: 48px;
}

/* 响应式调整 */
@media (max-width: 600px) {
  .profile-avatar {
    position: relative;
    top: -40px;
    left: 50%;
    transform: translateX(-50%);
  }
  
  .profile-details {
    text-align: center;
  }
}
</style>
