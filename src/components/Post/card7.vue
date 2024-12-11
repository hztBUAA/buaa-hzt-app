<template>
  <v-container>
    <v-dialog v-model="dialog" max-width="600" persistent>
      <template v-slot:activator="{ props: activatorProps }">
        <v-btn
          class="text-none font-weight-regular"
          prepend-icon="mdi-pencil-box-outline"
          text="创建"
          variant="tonal"
          v-bind="activatorProps"
        ></v-btn>
      </template>

      <v-card prepend-icon="mdi-account" title="User Profile">
        <v-card-text>
          <v-row dense>
            <v-col cols="6" md="6">
              <v-text-field
                v-model="form.title"
                label="标题"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="6`" sm="6">
              <v-select
                v-model="form.visibility"
                :items="['公开', '私密', '部分好友可见', '部分好友不可见']"
                label="可见性"
                required
              ></v-select>
            </v-col>
            <v-col cols="12">
              <v-text-field
                v-model="form.subtitle"
                label="副标题"
                hint="可空"
                persistent-hint
                required
              ></v-text-field>
            </v-col>
                  <v-col cols:="12">
              <v-textarea
                                    v-model="form.content"
      label="写些文字吧~"
      counter
    ></v-textarea>
            </v-col>
            
      </v-row>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn text="Close" variant="plain" @click="dialog = false"></v-btn>

          <v-btn
            color="primary"
            text="Save"
            variant="tonal"
            @click="submitForm"
          ></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-snackbar v-model="snackbar" :timeout="3000" top>
      {{ snackbarMessage }}
    </v-snackbar>
  </v-container>
    

</template>

<script>
import axios from '@/plugins/axios';
// import { Message } from 'element-ui';
// import 'element-ui/lib/theme-chalk/message.css';

const visibilityMap = {
  公开: 'public',
  私密: 'private',
  // TODO
  // 部分好友可见: 'friends',
  // 部分好友不可见: 'exclude'
};
export default {
  data: () => ({
    dialog: false,
    form: {
      title: '',
      subtitle: '',
      visibility: '',
      content: ''
    },
    snackbar: false,
    snackbarMessage: ''
  }),
  methods: {
    getInitialFormState() {
      return {
        firstName: '',
        lastName: '',
        email: '',
        password: '',
        confirmPassword: '',
        age: ''
      };
    },
    showSnackbar(message) {
      this.snackbarMessage = message;
      this.snackbar = true;
    },
    async submitForm() {
      try {
        this.form.visibility = visibilityMap[this.form.visibility];
        // 提交表单数据（例如，使用 HTTP 请求）
        const response = await axios.post('posts/', this.form);
        
        if (response.status === 200) {
          // 成功，跳转到主页
          this.$router.push('/');
          // 显示成功消息
          this.showSnackbar('Post created successfully');
        } else if (response.status === 500) {
          // 服务器错误，显示错误消息
          this.showSnackbar('Server error');
        } else if (response.status === 400 || response.status === 404 || response.status === 401) {
          // 错误请求，显示错误消息
          this.showSnackbar('Bad request');
        }
      } catch (error) {
        if (error.response && error.response.status === 403) {
          // 未授权，跳转到登录页面
          this.$router.push('/login/1');
          this.showSnackbar('请先登录');
        } else {
          // 处理其他错误
          this.showSnackbar('An error occurred');
        }
      }
    },
    
  }
};
</script>
