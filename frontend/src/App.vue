<template>
  <NavbarHeaderComponents/>
  <router-view/>
  <FooterComponent/>
</template>
<script>
import NavbarHeaderComponents from './components/navbarHeaderComponents.vue';
import FooterComponent from './components/footerComponent.vue';

export default {
  components: {
    NavbarHeaderComponents,
    FooterComponent
  }
}
</script>