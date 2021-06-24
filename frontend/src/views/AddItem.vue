<template>
  <div>
    <component :is="this.headerFooter.header"></component>
    <br /><br />
    <div class="row">
      <div class="col-md-4"></div>
      <div class="col-md-4">
        <div class="form-group">
          <h3>Add Item</h3>
        </div>
        <div class="form-group">
          <input
            v-model="item_data.item_name"
            type="text"
            class="form-control"
            placeholder="Item Name"
          />
        </div>
        <div class="form-group">
          <input
            v-model="item_data.item_no"
            type="text"
            class="form-control"
            placeholder="Item Number"
          />
        </div>
        <div class="form-group">
          <input
            v-model="item_data.item_desc"
            type="text"
            class="form-control"
            placeholder="Item Description"
          />
        </div>
        <div class="form-group">
          <input
            v-model="item_data.item_price"
            type="email"
            class="form-control"
            placeholder="Item Price"
          />
        </div>
        <div class="form-group justify-content-center">
          <input
            type="submit"
            class="btn btn-info mx-auto d-block"
            value="Add Item"
            @click="add_item"
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
import AddItemService from "../services/AddItemService";

export default {
  name: "add-user",
  data() {
    return {
      item_data: {
        item_name: "",
        item_no: "",
        item_desc: "",
        item_price: ""
      },
      submitted: false
    };
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
  methods: {
    add_item() {
      var data = {
        item_name: this.item_data.item_name,
        item_no: this.item_data.item_no,
        item_desc: this.item_data.item_desc,
        item_price: this.item_data.item_price
      };

      AddItemService.create(data).then(response => {
        if (response.data["error"]) {
          this.$toast.error(response.data["error"]);
        } else {
          this.user_data = {};
          this.$toast.success("Item Created");
        }
      });
    }
  }
};
</script>