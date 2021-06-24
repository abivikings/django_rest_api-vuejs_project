import http from "../http-common";

class ProfileDataService {

    profile() {
        return http.get("/profile/", {
            headers: {
                Authorization: 'Bearer' + this.$cookies.get('jwt_token')
            }
        });
    }
}

export default new ProfileDataService();