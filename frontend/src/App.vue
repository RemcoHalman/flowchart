<template>
  <div class="main">
    <div class="grid-container">
      <div class="nav">
        <router-link to="/">Start</router-link>
      </div>
      <div class="content">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
};
</script>

<style lang="scss"></style>
