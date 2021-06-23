import http from "../http-common";

class RegistrationDataService {

    create(data) {
        return http.post("/create_user/", data);
    }
}

export default new RegistrationDataService();