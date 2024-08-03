<template>
    <v-container fluid class="mt-8 fill-height1" >
      <v-row>
        <v-col xs12 sm8 md6 :style="{ minWidth:'400px'}">
          <v-card>
            <v-toolbar color="primary" dark>
              <v-toolbar-title>Login</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <v-form>
                <v-text-field
                  prepend-icon="person"
                  type="text"
                  v-model="user.email"
                  label="E-mail"
                ></v-text-field>
                <v-text-field
                  prepend-icon="lock"
                  type="password"
                  v-model="user.password"
                  label="Senha"
                ></v-text-field>
              </v-form>
              <v-alert type="error" v-if="errorLogin">
                Usuário ou senha inválidos
              </v-alert>
            </v-card-text>
            <v-card-actions>
              <div class="flex-grow-1"></div>
              <v-btn color="primary" @click="login">Login</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        user: {
          email: '',
          password: ''
        },
        errorLogin: false
      };
    },
    methods: {
      login() {
        // Add your login logic here
      }
    }
  };
  </script>