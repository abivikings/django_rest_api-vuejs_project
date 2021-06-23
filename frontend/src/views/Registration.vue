<template>
  <div>
    <br /><br />
    <div class="row">
      <div class="col-md-4"></div>
      <div class="col-md-4">
        <div class="form-group">
          <h3>Registration</h3>
        </div>
        <div class="form-group">
          <input
            v-model="user_data.first_name"
            type="text"
            class="form-control"
            placeholder="First Name"
          />
        </div>
        <div class="form-group">
          <input
            v-model="user_data.last_name"
            type="text"
            class="form-control"
            placeholder="Last Name"
          />
        </div>
        <div class="form-group">
          <input
            v-model="user_data.email"
            type="email"
            class="form-control"
            placeholder="Email"
          />
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
            value="Registration"
            @click="registration"
          />
        </div>
      </div>
      <div class="col-md-4"></div>
    </div>
  </div>
</template>

<script>
import RegistrationDataService from "../services/RegistrationDataService";

export default {
  name: "add-user",
  data() {
    return {
      user_data: {
        first_name: "",
        last_name: "",
        email: "",
        username: "",
        password: null
      },
      submitted: false
    };
  },
  methods: {
    registration() {
      var data = {
        first_name: this.user_data.first_name,
        last_name: this.user_data.last_name,
        email: this.user_data.email,
        username: this.user_data.username,
        password: this.user_data.password
      };

      RegistrationDataService.create(data).then(response => {
        if (response.data["error"]) {
          this.$toast.error(response.data["error"]);
        } else {
          this.user_data = {};
          this.$toast.success("User Created");
        }
      });
    }
  }
};
</script>