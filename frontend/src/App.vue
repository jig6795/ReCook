<template>
  <div id="app">
    <v-app>
      <router-view class="fill-height"></router-view>
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {},
};
</script>

<style>
* {
  font-family: 'Spoqa Han Sans Neo', 'sans-serif' !important;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}

::-webkit-scrollbar {
  display: none; /* Chrome, Safari, Opera*/
}

.h1 {
  font-weight: 300;
  font-size: 6rem;
  letter-spacing: -0.015625em;
  line-height: 1.1;
}
.h2 {
  font-weight: 300;
  font-size: 3.75rem;
  letter-spacing: -0.05em;
  line-height: 1.1;
}
.h3 {
  font-weight: 400;
  font-size: 3rem;
  letter-spacing: normal;
  line-height: 1.1;
}
.h4 {
  font-weight: 400;
  font-size: 2.125rem;
  letter-spacing: -0.0073529412em;
  line-height: 1.1;
}
.h5 {
  font-weight: 400;
  font-size: 1.5rem;
  letter-spacing: normal;
  line-height: 1.2;
}
.h6 {
  font-weight: 500;
  font-size: 1.25rem;
  letter-spacing: -0.0125em;
}
.sub-title-1 {
  font-weight: 400;
  font-size: 1.1rem;
  letter-spacing: -0.009375em;
}
.sub-title-2 {
  font-weight: 500;
  font-size: 0.875rem;
  letter-spacing: -0.0071428571em;
}
.caption-1 {
  font-weight: 400;
  font-size: 0.75rem;
  letter-spacing: -0.0333333333em;
}
.pointer {
  cursor: pointer;
}
.bg-color {
  background-color: #f8f9fb;
}
</style>
