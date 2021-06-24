<script>
import Logout from "@/views/Logout";

export default {
  name: "logout",
  components: {
    Logout
  },
  created() {
    this.$cookies.remove("jwt_token");
    this.$router.push("/login");
  }
};
</script>