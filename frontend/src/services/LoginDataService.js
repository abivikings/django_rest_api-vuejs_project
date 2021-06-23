import http from "../http-common";

class LgoinDataService {

    login(data) {
        return http.post("/login/", data);
    }
}

export default new LgoinDataService();