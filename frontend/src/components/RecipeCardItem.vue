<template>
  <div class="pb-2">
    <v-card
      rounded="xl"
      width="150"
      height="230"
      class="text-center mr-4 my-1"
      outlined
      @click="$emit('click')"
      :elevation="elevation ? 3 : 0"
    >
      <v-img :src="data['recipe-main-image']" max-height="150" min-height="150" />
      <v-container class="mb-3">
        <v-row>
          <v-col>
            <span class="font-weight-bold">
              {{ data['recipe-title'] | truncate(7, '..') }}
            </span>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="caption-1 pa-0">
            <v-icon small>mdi-timer</v-icon>
            <span>
              {{ data['recipe-time'].split(' ')[0] }}
            </span>
            <v-icon small>mdi-account-outline</v-icon>
            <span>
              {{
                data['recipe-person']
                  ? data['recipe-person'].replace('인기준', '인분')
                  : data['recipe-time'].split(' ')[1].replace('인기준', '인분')
              }}
            </span>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
  </div>
</template>

<script>
export default {
  components: {},
  props: {
    data: Object,
    elevation: Boolean,
  },
  data() {
    return {};
  },
  computed: {},
  watch: {},
  methods: {},
};
</script>

<style scoped></style>
