<template>

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
    

</template>

<script>
import axios from '@/plugins/axios';

export default {
  data: () => ({
    dialog: false,
    form: {
      title: '',
      subtitle: '',
      visibility: '',
      content: ''
    }
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
    async submitForm() {
      // Form validation logic
      // if (
      //   !this.form.firstName ||
      //   !this.form.lastName ||
      //   !this.form.email ||
      //   !this.form.password ||
      //   !this.form.confirmPassword ||
      //   !this.form.age
      // ) {
      //   alert('Please fill out all required fields.');
      //   return;
      // }

      // Submit form data (for example, using an HTTP request)
      const response = await axios.post('posts/', this.form);

      // console.log('Form submitted with data:', this.form, 'Response:', response);

      // Reset the form fields
      this.form = this.getInitialFormState();

      // Close dialog after submission
      this.dialog = false;
    }
  }
};
</script>
