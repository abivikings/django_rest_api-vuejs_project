import http from "../http-common";

class AddItemService {

    create(data) {
        return http.post("/add_item/", data);
    }
}

export default new AddItemService();