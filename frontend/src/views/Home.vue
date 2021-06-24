<template>
  <div>
    <component :is="this.headerFooter.header"></component>
    <h1>home</h1>
  </div>
</template>
<script>
import Header from "../components/Header.vue";
import ProfileHeader from "@/components/ProfileHeader";

export default {
  name: "home",
  components: {
    Header,
    ProfileHeader
  },
  computed: {
    headerFooter() {
      return this.$cookies.get("jwt_token")
        ? {
            header: ProfileHeader
          }
        : {
            header: Header
          };
    }
  }
};
</script>