<template>
  <div>
    <component :is="this.headerFooter.header"></component>
    <h1>Hello profile</h1>
  </div>
</template>
<script>
import Header from "../components/Header.vue";
import ProfileHeader from "@/components/ProfileHeader";
// import ProfileService from "@/services/ProfileService";

export default {
  name: "profile",
  components: {
    ProfileHeader
  },
  created() {
    if (this.$cookies.get("jwt_token")) {
      this.$router.push("/profile");
    } else {
      this.$router.push("/login");
    }
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