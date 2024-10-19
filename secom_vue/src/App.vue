<template>
  <div id="app">
    <NavbarComponent />
    <LoginComponent />
  </div>
</template>

<script>
import NavbarComponent from './components/NavbarComponent.vue'
import LoginComponent from './components/LoginComponent.vue'

export default {
  name: 'App',
  components: {
    NavbarComponent,
    LoginComponent
  }
}
</script>

<style>
/*
#app {
  background-color: whitesmoke;
  font-family: 'Aldrich', sans-serif;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin-top: 60px;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
*/
</style>













<!--
<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <header>
    <img
      alt="Vue logo"
      class="logo"
      src="./assets/logo.svg"
      width="125"
      height="125"
    />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
-->