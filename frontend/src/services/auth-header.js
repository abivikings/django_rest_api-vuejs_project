export default function authHeader() {
    let jwt_token = $cookies.get('jwt_token')

    if (jwt_token) {
        return { Authorization: 'jwt' + jwt_token };
    } else {
        return {};
    }
}