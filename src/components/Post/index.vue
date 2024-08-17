<template>
  <v-container fluid>
    <v-row dense>
      <v-col v-for="c in cards" :key="c.id" cols="12">
        <v-card :subtitle="c.subtitle" :title="c.title" :text="c.content">
          <v-card-actions>
            <v-row>
              <v-spacer></v-spacer>

              <v-col class="text-center" :cols="1">
                <v-btn density icon @click="like">
                  <v-icon color="red">mdi-heart</v-icon>{{ 1 }}
                </v-btn>
              </v-col>

              <v-col class="text-center" :cols="1">
                <v-btn density icon @click="bookmark">
                  <v-icon>mdi-bookmark</v-icon>{{ 2 }}
                </v-btn>
              </v-col>

              <v-col class="text-center" :cols="1">
                <v-btn density icon @click="share">
                  <v-icon>mdi-share-variant</v-icon>
                </v-btn>
              </v-col>

              <v-col class="text-center" :cols="1">
                <v-btn density icon @click="refresh">
                  <v-icon>mdi-refresh</v-icon>
                </v-btn>
              </v-col>
            </v-row>
            <!-- <v-btn color="red" icon="mdi-heart" size="small"></v-btn>

            <div align="center" justify="center">
              <v-btn
                density
                color="medium-emphasis"
                icon="mdi-heart"
                size="small"
              >
              </v-btn
              ><br />
              <span>30</span>
            </div>
            <v-btn color="medium-emphasis" icon="mdi-bookmark" size="small">
            </v-btn>
            <span>30</span>

            <v-btn
              color="medium-emphasis"
              icon="mdi-share-variant"
              size="small"
            ></v-btn>
            <v-btn aria-label="Refresh" icon="mdi-refresh"></v-btn> -->
          </v-card-actions>
        </v-card>
      </v-col>
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
