<template>
  <NavbarHeaderComponents/>
  <router-view/>
</template>
<script>
import NavbarHeaderComponents from './components/navbarHeaderComponents.vue';

export default {
  components: {
    NavbarHeaderComponents
  }
}
</script>