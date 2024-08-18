<template>
  <v-container fluid>
    <v-row dense>
      <v-col v-for="c in cards" :key="c.id" cols="6">
        <v-card
          :subtitle="c.subtitle"
          :title="c.title"
          :text="c.content"
          max-width="300"
        >
          <v-card-actions >
            <v-row>
              <v-spacer></v-spacer>

              <v-col class="text-center pa-0 ml-2" :cols="2" >
                <v-btn density icon @click="like">
                  <v-icon color="red">mdi-heart</v-icon>{{ 1 }}
                </v-btn>
              </v-col>

              <v-col class="text-center pa-0 ml-2" :cols="2">
                <v-btn density icon @click="bookmark">
                  <v-icon>mdi-bookmark</v-icon>{{ 2 }}
                </v-btn>
              </v-col>

              <v-col class="text-center pa-0 ml-2" :cols="2">
                <v-btn density icon @click="share">
                  <v-icon>mdi-share-variant</v-icon>
                </v-btn>
              </v-col>

              <v-col class="text-center pa-0 ml-2" :cols="2">
                <v-btn density icon @click="refresh">
                  <v-icon>mdi-refresh</v-icon>
                </v-btn>
              </v-col>
            </v-row>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col v-for="c in cards" :key="c.id" cols="6">
        <v-card
          :subtitle="c.subtitle"
          :title="c.title"
          :text="c.content"
          width="800"
        >
          <v-card-actions>
            <v-row>
              <v-spacer></v-spacer>

              <v-col class="text-center" :cols="12">
                <v-btn density icon @click="like">
                  <v-icon color="red">mdi-heart</v-icon>{{ 1 }}
                </v-btn>
              </v-col>

              <v-col class="text-center" :cols="12">
                <v-btn density icon @click="bookmark">
                  <v-icon>mdi-bookmark</v-icon>{{ 2 }}
                </v-btn>
              </v-col>

              <v-col class="text-center" :cols="12">
                <v-btn density icon @click="share">
                  <v-icon>mdi-share-variant</v-icon>
                </v-btn>
              </v-col>

              <v-col class="text-center" :cols="12">
                <v-btn density icon @click="refresh">
                  <v-icon>mdi-refresh</v-icon>
                </v-btn>
              </v-col>
            </v-row>
          </v-card-actions>
        </v-card></v-col
      >
    </v-row>
    <v-row>
      <router-view></router-view>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    cards: [
      {
        id: 1,
        title: 'Pre-fab homes',
        subtitle: 'Number 10',
        content: 'https://cdn.vuetifyjs.com/images/cards/house.jpg'
      },
      {
        id: 2,
        title: 'Favorite road trips',
        subtitle: 'Number 10',
        content: 'https://cdn.vuetifyjs.com/images/cards/road.jpg'
      },
      {
        id: 3,
        title: 'Best airlines',
        subtitle: 'Number 10',
        content: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg'
      }
    ]
  })
};
</script>
>
