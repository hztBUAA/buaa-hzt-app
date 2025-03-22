<template>
  <v-layout>
    <!-- 个人资料卡片 -->
    <v-container>
      <v-row>
        <!-- 页面标题 -->
        <v-col cols="12" class="mb-4">
          <h1 class="text-h4 font-weight-bold">个人资料</h1>
          <p class="text-subtitle-1 text-medium-emphasis">执行力！</p>
        </v-col>
        
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

        <!-- 技能和兴趣爱好区域 -->
        <v-col cols="12" md="8">
          <!-- 技能展示卡片 -->
          <v-card class="mb-4">
            <v-card-title class="d-flex align-center">
              <v-icon start icon="mdi-lightbulb" class="mr-2"></v-icon>
              技能专长
            </v-card-title>
            <v-card-text>
              <div class="skills-container">
                <v-chip
                  v-for="skill in skills"
                  :key="skill.name"
                  :color="skill.color"
                  variant="elevated"
                  class="ma-1"
                >
                  {{ skill.name }}
                </v-chip>
              </div>
            </v-card-text>
          </v-card>

          <!-- 兴趣爱好卡片 -->
          <v-card>
            <v-card-title class="d-flex align-center">
              <v-icon start icon="mdi-heart" class="mr-2"></v-icon>
              生活 & 兴趣
            </v-card-title>
            <v-card-text>
              <v-row>
                <v-col 
                  v-for="(hobby, index) in hobbies" 
                  :key="index"
                  cols="12" 
                  sm="6"
                >
                  <v-card variant="outlined" class="hobby-card">
                    <v-card-item>
                      <template v-slot:prepend>
                        <v-icon
                          :icon="hobby.icon"
                          :color="hobby.color"
                          size="large"
                        ></v-icon>
                      </template>
                      <v-card-title>{{ hobby.name }}</v-card-title>
                      <v-card-subtitle>{{ hobby.description }}</v-card-subtitle>
                    </v-card-item>
                  </v-card>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-layout>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  setup() {
    const userProfile = ref({
      name: '黄振庭',
      title: '全(啥)栈(也)开(不)发(会)攻城狮',
      bio: '热爱编程，专注于Web开发和人工智能领域',
      avatar: '',
      coverImage: 'https://cdn.vuetifyjs.com/images/parallax/material.jpg'
    })

    const statistics = ref({
      projects: { value: 46, label: '仓库数' },
      // contributions: { value: 777, label: '贡献数' },
      followers: { value: 16, label: '关注者' },
      following: { value:57, label: '关注中' },
      stars: { value: 98, label: '获得星标（包括贡献者）' }
    })

    // 从GitHub API获取用户数据
    const fetchGitHubData = async () => {
      try {
        // 获取用户基本信息
        const userResponse = await fetch('https://api.github.com/users/hztBUAA')
        const userData = await userResponse.json()
        
        userProfile.value = {
          ...userProfile.value,
          avatar: userData.avatar_url,
          bio: userData.bio || userProfile.value.bio
        }

        // 更新基础统计数据
        statistics.value = {
          projects: { value: userData.public_repos, label: '仓库数' },
          followers: { value: userData.followers, label: '关注者' },
          following: { value: userData.following, label: '关注中' },
          stars: { value: 0, label: '获得星标（包括贡献者）' },
          // contributions: { value: 0, label: '贡献数' }
        }

        // 获取完整的star数据
        await fetchAllStars()
        
        // 获取贡献数据
        // await fetchContributions()

      } catch (error) {
        console.error('获取GitHub数据失败:', error)
      }
    }

    // const fetchContributions = async () => {
    //   const query = `
    //     query {
    //       user(login: "hztBUAA") {
    //         contributionsCollection {
    //           totalCommitContributions
    //           totalIssueContributions
    //           totalPullRequestContributions
    //           totalPullRequestReviewContributions
    //           contributionCalendar {
    //             totalContributions
    //             weeks {
    //               contributionDays {
    //                 contributionCount
    //                 date
    //               }
    //             }
    //           }
    //         }
    //       }
    //     }
    //   `

    // //   try {
    // //     const response = await fetch('https://api.github.com/graphql', {
    // //       method: 'POST',
    // //       headers: {
    // //         'Authorization': `bearer ${process.env.VUE_APP_GITHUB_TOKEN}`,
    // //         'Content-Type': 'application/json',
    // //       },
    // //       body: JSON.stringify({ query })
    // //     })

    // //     const data = await response.json()
    // //     console.log('data', data)
    // //     const contributions = data.data.user.contributionsCollection
        
    // //     // 更新统计数据
    // //     statistics.value.contributions.value = 
    // //       contributions.contributionCalendar.totalContributions
    // //   } catch (error) {
    // //     console.error('获取贡献数据失败:', error)
    // //   }
    // }

    const fetchAllStars = async () => {
      try {
        // 1. 获取用户自己的仓库的star
        const ownReposResponse = await fetch('https://api.github.com/users/hztBUAA/repos');
        const ownRepos = await ownReposResponse.json();
        const ownStars = ownRepos.reduce((sum, repo) => sum + repo.stargazers_count, 0);

        // 2. 获取你作为贡献者的项目的star
        const contributedRepoResponse = await fetch('https://api.github.com/repos/DocAILab/XRAG');
        const contributedRepo = await contributedRepoResponse.json();
        const contributedStars = contributedRepo.stargazers_count;

        // 更新总star数
        statistics.value.stars.value = ownStars + contributedStars;
      } catch (error) {
        console.error('获取star数据失败:', error);
      }
    };

    // 组件挂载时获取数据
    onMounted(() => {
      fetchGitHubData()
    })

    // 其他代码保持不变...
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

    const skills = ref([

      { name: 'Python', color: 'blue' },
      { name: 'JavaScript', color: 'indigo' },
      { name: 'Go', color: 'green' },
      { name: 'Pytorch', color: 'red' },
      { name: 'Linux', color: 'purple' },
      { name: 'Docker', color: 'orange' },
      // { name: '后端开发', color: 'indigo' },
      // { name: '前端开发', color: 'deep-purple' },
      // { name: '数据库', color: 'orange' },
      // { name: 'DevOps', color: 'red' }
    ])

    // 兴趣爱好数据
    const hobbies = ref([
      {
        name: '编程',
        description: '探索新技术，创造有趣的项目',
        icon: 'mdi-laptop',
        color: 'primary'
      },
      {
        name: '运动',
        description: '篮球和健身',
        icon: 'mdi-basketball',
        color: 'warning'
      }
    ])

    return {
      userProfile,
      socialLinks,
      statistics,
      skills,
      hobbies
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

.hobby-card {
  transition: transform 0.2s;
}

.hobby-card:hover {
  transform: translateY(-4px);
}

/* 确保卡片高度一致 */
.v-card-item {
  min-height: 100px;
}

/* 添加一些间距 */
.mb-4 {
  margin-bottom: 16px;
}

.skills-container {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: center;
}

/* 确保卡片内容区域有合适的内边距 */
.v-card-text {
  padding: 16px;
}
</style>
