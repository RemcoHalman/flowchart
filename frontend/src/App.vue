<template>
  <div class="main">
    <div class="grid-container">
      <div class="nav">
        <router-link to="/">Home</router-link>
        <router-link to="/about">About</router-link>
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

<style lang="scss">
body {
  margin: 0;
  padding: 0;
}

.main {
  width: 100vw;
}

.grid-container {
  height: 100vh;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
  grid-template-rows: 1fr;
  gap: 0px 0px;
  grid-template-areas: "nav content content content content content";
  .nav {
    grid-area: nav;
  }

  .content {
    grid-area: content;
  }
}

.nav {
  width: 100%;
  background: #333;
  color: #fff;
  font-size: 1.3rem;
  margin: 0 auto;
  a {
    color: white;
  }
}

.content {
  padding: 0 0 0 9px;
  background: #fff;
  background-image: radial-gradient(#ccc 10%, #fff 10%);
  background-position: 0 0;
  background-size: 20px 20px;
}
</style>
