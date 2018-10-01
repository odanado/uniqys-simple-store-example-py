<template>
  <div id="app">
    <input type="text" v-model="value" />
    <input type="button" @click="post" value="post" />
  </div>
</template>

<script>
import SimpleStore from './api/simple_store.js'

export default {
  name: 'App',
  mounted() {
    this.store = new SimpleStore();
    this.store.get().then(res => {
      const { data } = res;
      this.value = data;
    })
  },
  data: () => ({
    value: null,
  }),
  methods: {
    async post() {
      await this.store.set(this.value);
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
