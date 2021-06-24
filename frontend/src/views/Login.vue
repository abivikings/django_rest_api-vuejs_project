<template>
  <div>
    <component :is="this.headerFooter.header"></component>
    <br /><br />
    <div class="row">
      <div class="col-md-4"></div>
      <div class="col-md-4">
        <div class="form-group">
          <h3>Login</h3>
        </div>
        <div class="form-group">
          <input
            v-model="user_data.username"
            type="text"
            class="form-control"
            placeholder="Username"
          />
        </div>
        <div class="form-group">
          <input
            v-model="user_data.password"
            type="password"
            class="form-control"
            placeholder="Password"
          />
        </div>
        <div class="form-group justify-content-center">
          <input
            type="submit"
            class="btn btn-info mx-auto d-block"
            value="Login"
            @click="login"
          />
        </div>
      </div>
      <div class="col-md-4"></div>
    </div>
  </div>
</template>

<script>
import Header from "../components/Header.vue";
import ProfileHeader from "@/components/ProfileHeader";
import LoginDataService from "../services/LoginDataService";

export default {
  name: "login",
  components: {
    Header,
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
  },
  data() {
    return {
      user_data: {
        username: "",
        password: null
      },
      submitted: false
    };
  },
  methods: {
    login() {
      var data = {
        username: this.user_data.username,
        password: this.user_data.password
      };

      LoginDataService.login(data).then(response => {
        if (response.data["error"]) {
          this.$toast.error(response.data["error"]);
        } else {
          this.$cookies.set("jwt_token", response.data["access_token"]);
          this.$router.push("/profile");
        }
      });
    }
  }
};
</script>