<template>
  <v-layout>
    <v-navigation-drawer absolute permanent>
      <v-list>
        <v-list-item
          prepend-avatar="https://cdn.vuetifyjs.com/images/john.png"
          subtitle="john@google.com"
          title="John Leider"
        >
          <template v-slot:append>
            <v-btn icon="mdi-menu-down" size="small" variant="text"></v-btn>
          </template>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list :lines="false" density="compact" nav>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :value="item"
          color="primary"
        >
          <template v-slot:prepend>
            <v-icon :icon="item.icon"></v-icon>
          </template>

          <v-list-item-title>{{ item.text }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main style="height: 100%">
      <v-container>
        <v-row>
          <v-col cols="12">
            <v-card hover image="https://cdn.vuetifyjs.com/docs/images/cards/dark-beach.jpg">
              <v-card-title>My Files</v-card-title>
              <v-card-text>
                <v-row>
                  <v-col cols="12">
                    <v-sparkline
                      :auto-line-width="autoLineWidth"
                      :fill="fill"
                      :gradient="gradient"
                      :gradient-direction="gradientDirection"
                      :line-width="width"
                      :model-value="value"
                      :padding="padding"
                      :smooth="radius || false"
                      :stroke-linecap="lineCap"
                      :type="type"
                      auto-draw
                    ></v-sparkline>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="12">
            <v-card>
              <v-card-title>My Files</v-card-title>
              <v-card-text>
                <v-row>
                  <v-col cols="12">
                    <v-sparkline
                      :auto-line-width="autoLineWidth"
                      :fill="fill"
                      :gradient="gradient"
                      :gradient-direction="gradientDirection"
                      :line-width="width"
                      :model-value="value"
                      :padding="padding"
                      :smooth="radius || false"
                      :stroke-linecap="lineCap"
                      :type="type"
                      auto-draw
                    ></v-sparkline>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col>
            <v-card
              class="mx-auto"
              color="surface-variant"
              image="https://cdn.vuetifyjs.com/docs/images/cards/dark-beach.jpg"
              max-width="97%"
              subtitle="Take a walk down the beach"
              title="Evening sunset"
            >
              <template v-slot:actions>
                <v-btn
                  append-icon="mdi-chevron-right"
                  color="red-lighten-2"
                  text="Book Activity"
                  variant="outlined"
                  block
                ></v-btn>
              </template>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-layout>
</template>
<script>
export default {
  data: () => ({
    items: [
      { text: 'My Files', icon: 'mdi-folder' },
      { text: 'Shared with me', icon: 'mdi-account-multiple' },
      { text: 'Starred', icon: 'mdi-star' },
      { text: 'Recent', icon: 'mdi-history' },
      { text: 'Offline', icon: 'mdi-check-circle' },
      { text: 'Uploads', icon: 'mdi-upload' },
      { text: 'Backups', icon: 'mdi-cloud-upload' }
    ]
  })
};
</script>
